import numpy as np
import paddle
from parakeet.utils import display
from parakeet.utils import layer_tools

import sys
sys.path.append("../..")
import examples
from parakeet.models.tacotron2 import Tacotron2
from parakeet.frontend import EnglishCharacter
from examples.tacotron2 import config as tacotron2_config

# text to bin model
synthesizer_config = tacotron2_config.get_cfg_defaults()
synthesizer_config.merge_from_file("../../../tacotron2_ljspeech_ckpt_0.3/config.yaml")
frontend = EnglishCharacter()
model = Tacotron2.from_pretrained(
    synthesizer_config, "../../../tacotron2_ljspeech_ckpt_0.3/step-179000")
model.eval()

with open('../../../__input__.txt', 'rt') as f:
    lines = f.readlines()

from parakeet.models.waveflow import ConditionalWaveFlow
from examples.waveflow import config as waveflow_config

# bin to wav model
vocoder_config = waveflow_config.get_cfg_defaults()
vocoder = ConditionalWaveFlow.from_pretrained(
    vocoder_config,
    "../../../waveflow_ljspeech_ckpt_0.3/step-2000000")
layer_tools.recursively_remove_weight_norm(vocoder)
vocoder.eval()

def one_by_one(line, arr):
    text = line.strip()
    if(len(text)<=1):
        return
    sentence = paddle.to_tensor(frontend(line)).unsqueeze(0)

    with paddle.no_grad():
        outputs = model.infer(sentence)
    mel_output = outputs["mel_outputs_postnet"][0].numpy().T
    alignment = outputs["alignments"][0].numpy().T

    #now bin to audio
    audio = vocoder.infer(paddle.transpose(outputs["mel_outputs_postnet"], [0, 2, 1]))
    arr.append(audio[0].numpy())

npwav = []
for line in lines:
    try:
        one_by_one(line, npwav)
    except Exception as inst:
        print("Unexpected error:", sys.exc_info()[0])

print(len(npwav))

# wav to file
from scipy.io.wavfile import write as wvwrite
file_name='__out__.wav'
wvwrite(file_name, 22050, np.concatenate(npwav))
