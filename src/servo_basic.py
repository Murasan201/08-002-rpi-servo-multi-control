#!/usr/bin/env python3
"""
サーボモーター基本制御プログラム
SG90サーボモーターを使用した基本的な角度制御のデモンストレーション
要件定義書: docs/requirements.md
"""

import time
from adafruit_servokit import ServoKit

# 定数
CHANNELS = 16           # PCA9685のチャンネル数
SERVO_CHANNEL = 0       # 使用するサーボのチャンネル番号
DELAY_TIME = 2          # 各動作間の待機時間（秒）


def setup_servo():
    """
    サーボモーターを初期化する

    Returns:
        ServoKit: 初期化されたServoKitオブジェクト
    """
    # PCA9685ボードを16チャンネルで初期化
    # ServoKitライブラリがI²C通信を自動的に設定
    kit = ServoKit(channels=CHANNELS)
    print(f"ServoKitを{CHANNELS}チャンネルで初期化しました")
    return kit


def move_servo_to_angle(kit, channel, angle):
    """
    サーボを指定角度に移動する

    Args:
        kit (ServoKit): ServoKitオブジェクト
        channel (int): サーボのチャンネル番号（0-15）
        angle (int): 目標角度（0-180度）
    """
    print(f"角度: {angle}度")
    kit.servo[channel].angle = angle


def demo_servo_movement(kit, channel):
    """
    サーボの基本動作デモを実行する

    Args:
        kit (ServoKit): ServoKitオブジェクト
        channel (int): サーボのチャンネル番号
    """
    print(f"チャンネル{channel}のサーボを動かします")

    while True:
        # 0度に移動（最小角度）
        move_servo_to_angle(kit, channel, 0)
        time.sleep(DELAY_TIME)

        # 90度に移動（中央位置）
        move_servo_to_angle(kit, channel, 90)
        time.sleep(DELAY_TIME)

        # 180度に移動（最大角度）
        move_servo_to_angle(kit, channel, 180)
        time.sleep(DELAY_TIME)

        # 90度に戻る（中央位置）
        print("角度: 90度（中央位置）")
        kit.servo[channel].angle = 90
        time.sleep(DELAY_TIME)


def cleanup_servo(kit, channel):
    """
    サーボを安全な位置（中央）に戻す

    Args:
        kit (ServoKit): ServoKitオブジェクト
        channel (int): サーボのチャンネル番号
    """
    # サーボを中央位置（90度）に戻す
    # これにより機械的な負担を軽減
    kit.servo[channel].angle = 90
    print("サーボを中央位置に設定しました")


def main():
    """
    メイン関数：サーボモーター制御のデモを実行
    """
    print("SG90サーボモーター制御を開始します")

    # ServoKitの初期化
    kit = setup_servo()

    try:
        # デモ動作を実行（Ctrl+Cで中断されるまで継続）
        demo_servo_movement(kit, SERVO_CHANNEL)

    except KeyboardInterrupt:
        # Ctrl+Cによる中断を検知
        print("\nプログラムを終了します")

    finally:
        # 必ずサーボを安全な位置に戻す
        cleanup_servo(kit, SERVO_CHANNEL)


if __name__ == "__main__":
    main()
