# TTS with Github Actions

## What

一个开源(Apache License)免费的文字转语音服务，支持中英文。

英文样例： [Alice’s Adventures in Wonderland](https://github.com/l-O-O-l/TTS-action/issues/5), [The Tyger By William Blake](https://github.com/l-O-O-l/TTS-action/issues/2) and [Psalms](https://github.com/l-O-O-l/TTS-action/issues/4) . 

中文样例 [朱自清 背影](https://github.com/l-O-O-l/TTS-action/issues/11) [叶挺 囚歌](https://github.com/l-O-O-l/TTS-action/issues/10) [余光中 乡愁](https://github.com/l-O-O-l/TTS-action/issues/8) [关雎](https://github.com/l-O-O-l/TTS-action/issues/9)

更多样例 [在这里](https://github.com/l-O-O-l/TTS-action/issues?q=is%3Aissue+is%3Aclosed++TTS)

## Usage
在这个项目里面，新建一个issue 以 `TTS:` (优质英文),  `TTS-F:` (快速英文) or `TTS-CN:` (中文普通话)，把需要转的文字写在 issue 里面. 几分钟以后，语音就会生成，链接会在回复里面

中文里面有二十多个不同的声音， 你可以用 `TTS-CN: 1$`, `TTS-CN: 30$` 来转换不同的语音。 具体信息在 [docker/ttskit](https://github.com/privapps/docker-ttskit/tree/action)

## How
这个项目用的都是开源内容和免费服务，采用了三个不同的引擎
* https://github.com/iclementine/Parakeet 英文，拥有非常好的音质和效果，虽然比较慢
* https://github.com/MycroftAI/mimic1 英文，很快，一听就知道是电脑合成的
* https://github.com/KuangDD/ttskit 中文，音质效果不错，就是有点慢

一旦 issue 建立， Github Action 会触发: 首先读需要转换的文字; 然后用引擎生成语音; 再压缩成 mp3 然后 merge; 最后加上链接，关闭 issue.


### Known issue
* Parakeet 英文每行有10秒钟的限制，所以要多分行 (这个有时间我自动分拆一下)
* Parakeet and ttskit 很慢
* GitHub actions 有运行时间的限制

### Donation
```
bitcoin:bc1qc2rpn0x0lzv8gdgx8nvhsrkx3jm3s0kpql4tfk?time=1614371095
```
