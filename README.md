# getkeyframe_with_ffprobe_and_python

* 環境
  * ffprobeをインストールしておく
  * `pip install ffprobe`
  
* 使い方
  1. キーフレームを抽出したい動画を同じディレクトリに保存
  2. `$python getkeyframe.py -v=./Fireworks-348.mp4 -o=output_with_cli.json`を実行 (-v:ビデオファイルパス、-o：出力ファイルパス)  
  3. 出力されたjsonファイルのkey_frame:0 (or 1)となっているところを確認。1ならIフレーム（キーフレーム）  
  
