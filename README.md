# TTS with Github Actions

## What

It is an open-source (Apache License) free Text To Speech (TTS) service, that takes the text information from an issue request, as long as the issue title starts with `TTS:`, `TTS-F:` or `TTS-CN:`. After a few minutes, it generates audio, and the audio link would be added into the issue comment.

Samples are [Alice’s Adventures in Wonderland](https://github.com/l-O-O-l/TTS-action/issues/5), [The Tyger By William Blake](https://github.com/l-O-O-l/TTS-action/issues/2) and [Psalms](https://github.com/l-O-O-l/TTS-action/issues/4) . 

Chinese sample [朱自清 背影](https://github.com/l-O-O-l/TTS-action/issues/11) [叶挺 囚歌](https://github.com/l-O-O-l/TTS-action/issues/10) [余光中 乡愁](https://github.com/l-O-O-l/TTS-action/issues/8) [关雎](https://github.com/l-O-O-l/TTS-action/issues/9)

More ones can be found [here](https://github.com/l-O-O-l/TTS-action/issues?q=is%3Aissue+is%3Aclosed++TTS)

## Usage
Create a new issue start with `TTS:` (English best quality),  `TTS-F:` (English quick response) or `TTS-CN:` (Chinese Mandarin) with a body text. After a few minutes, the issue would be closed with a ready-to-download link of the audio.

You can also choose 20+ different voices for `TTS-CN:` by using like `TTS-CN: 1$`, `TTS-CN: 30$` more information can be found at [docker/ttskit](https://github.com/privapps/docker-ttskit)

## How
This application uses all open-source projects and free services. There are three TTS engines. 
* One is based on https://github.com/iclementine/Parakeet, which is arguably the best open source TTS engine that I can find at the moment. Yes, it is slow, but yields much better quality. (If you find a better one/balance, please let me know). 
* The other one is https://github.com/MycroftAI/mimic1 , it is faster and more robotic. 
* The Chinese Mandarin is using https://github.com/KuangDD/ttskit, it has great voice with 20+ different voice

Once an issue is created, GitHub action would be triggered: It first reads the body of the issue; next either use pre-trained data powered by Python Machine Learning (Parakeet), or built-in CPP voice (Mimic) to create the audio; then it compresses wave to mp3 and merges to mp3 branch; Finally, it links to the issue and closes the issue.

### Why
As an AI hobbyist, I am always amazed by Google, Alexia, and Siri. Those TTS help me a lot when reading books. However, those are commercial apps that can not be used freely. In addition, I also want to take advantage of GitHub action, a free service that has been out for quite a while, to create new toys.

Since I have played with different TTS engines before, it only took me about two days to wire those up with Github actions. And another couple of days to add Chinese Mandarin. I personally really like this **TOY**.

### Known issue
* For Parakeet, due to model/pre-trained limitation, the sentence (row) is limited to 10 seconds. Longer ones are cut off. Mimic does not have this issue
* Both Parakeet and ttskit are slow
* There is also a runtime limitation for GitHub actions.

### Donation
```
bitcoin:bc1qc2rpn0x0lzv8gdgx8nvhsrkx3jm3s0kpql4tfk?time=1614371095
```
