#coding:utf-8
import codecs
import json
import subprocess
import argparse

def get_parser():
    parser = argparse.ArgumentParser(description='Get Keyframe with ffprobe')
    parser.add_argument('--video_path', '-v', type=str, help='video path')
    parser.add_argument('--output_path', '-o', type=str, default='output_with_cli.json', help='output path')
    opt = parser.parse_args()
    print(opt)
    return opt

def detect_keyframe_with_ffprobe(video_path, output_path):
    command = 'ffprobe -show_frames -select_streams v -print_format json "{}" > {}'.format(video_path, output_path)

    try:
        response = subprocess.run(
            command, # 実行コマンド
            shell = True, #shellで実行
            check=True, # 終了コードが0でないとき、CalledProcessErrorをraise
            stdout= subprocess.PIPE, # 処理結果をPIPEに渡す
        )
    except CalledProcessError as e:
        raise e

    #フレームの情報を抽出
    frames = json.loads(response.stdout)['frames']

    # フレームの順番が狂ってしまう場合はソート
    frames = sorted(frames, key=lambda f: f['pkt_pts'])
    return [f['pkt_pts'] for f in frames if f['key_frame']]

if __name__ == '__main__':
    opt = get_parser()
    detect_keyframe_with_ffprobe(opt.video_path, opt.output_path)
