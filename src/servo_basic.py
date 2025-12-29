#!/usr/bin/env python3
"""
サーボモーター基本制御プログラム
"""

import time
from adafruit_servokit import ServoKit

# 定数
SERVO_CHANNEL = 0    # 使用するサーボのチャンネル番号
DELAY_TIME = 2       # 動作間の待機時間（秒）


def demo_servo_movement(kit):
    """サーボを0度→90度→180度→90度の順に繰り返し動かす"""
    angles = [0, 90, 180, 90]

    while True:
        for angle in angles:
            kit.servo[SERVO_CHANNEL].angle = angle
            time.sleep(DELAY_TIME)


def main():
    """メイン関数：サーボモーター制御のデモを実行"""
    kit = ServoKit(channels=16)

    try:
        demo_servo_movement(kit)
    except KeyboardInterrupt:
        pass
    finally:
        kit.servo[SERVO_CHANNEL].angle = 90


if __name__ == "__main__":
    main()
