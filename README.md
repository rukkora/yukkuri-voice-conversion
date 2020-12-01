# yukkuri-voice-conversion

# 使用方法

## 前提条件
-Python(3系)をインストールしてあること
-ffmpegをインストールしてあること

```bash
pip install soundfile
ffmpeg -i yukkuri.wav -ar 44100 yukkuri2.wav #yukkuri.wavは変換したいファイル名
python convert.py
Input a file name to convert.
yukkuri2.wav #先ほど変換したファイル名を入力
```

## 使用した結果

[YouTube　サンプル](https://www.youtube.com/watch?v=hkj5O3c4ATU&feature=youtu.be)