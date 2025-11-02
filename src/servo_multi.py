#!/usr/bin/env python3
"""
複数サーボモーター同期制御プログラム
2つのサーボモーターを同期させて様々なパターンで動作させるデモンストレーション
要件定義書: docs/requirements.md
"""

import time
from adafruit_servokit import ServoKit

# 定数
CHANNELS = 16                  # PCA9685のチャンネル数
SERVO_CHANNELS = [0, 1]        # 使用するサーボのチャンネル番号リスト
PATTERN_DELAY = 3              # 各パターンの実行時間（秒）
CENTER_ANGLE = 90              # サーボの中央位置角度

# サーボの動作パターン定義
# 各パターンは [チャンネル0の角度, チャンネル1の角度] の形式
MOVEMENT_PATTERNS = [
    [0, 180],      # パターン1: 対向（0度と180度）
    [45, 135],     # パターン2: 斜め対向（45度と135度）
    [180, 0],      # パターン3: 逆対向（180度と0度）
    [90, 90],      # パターン4: 両方とも中央位置
]


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


def move_servos_to_pattern(kit, channels, angles):
    """
    複数のサーボを指定された角度に同時に移動する

    Args:
        kit (ServoKit): ServoKitオブジェクト
        channels (list): サーボのチャンネル番号リスト
        angles (list): 各サーボの目標角度リスト
    """
    # zip関数で各チャンネルと対応する角度をペアにして処理
    for channel, angle in zip(channels, angles):
        kit.servo[channel].angle = angle
        print(f"  チャンネル{channel}: {angle}度")


def demo_multi_servo(kit, channels, patterns):
    """
    複数サーボの同期動作デモを実行する

    Args:
        kit (ServoKit): ServoKitオブジェクト
        channels (list): 使用するサーボのチャンネル番号リスト
        patterns (list): 動作パターンのリスト
    """
    print(f"チャンネル{', '.join(map(str, channels))}のサーボを同期制御します")

    # enumerate関数でパターン番号と角度リストを取得（1から開始）
    for pattern_num, angles in enumerate(patterns, 1):
        print(f"パターン{pattern_num}: {angles}")

        # パターンに従って全サーボを同時に移動
        move_servos_to_pattern(kit, channels, angles)

        # 次のパターンまで待機
        time.sleep(PATTERN_DELAY)

    # 全パターン終了後、全サーボを中央位置に戻す
    print("全サーボを中央位置に戻します")
    center_angles = [CENTER_ANGLE] * len(channels)
    move_servos_to_pattern(kit, channels, center_angles)


def cleanup_servos(kit, channels):
    """
    全サーボを安全な位置（中央）に戻す

    Args:
        kit (ServoKit): ServoKitオブジェクト
        channels (list): サーボのチャンネル番号リスト
    """
    # 全サーボを中央位置（90度）に戻す
    # これにより機械的な負担を軽減
    for channel in channels:
        kit.servo[channel].angle = CENTER_ANGLE
    print("全サーボを中央位置に設定しました")


def main():
    """
    メイン関数：複数サーボモーターの同期制御デモを実行
    """
    print("2つのサーボモーター同期制御")

    # ServoKitの初期化
    kit = setup_servo()

    try:
        # 複数サーボの同期動作デモを実行
        demo_multi_servo(kit, SERVO_CHANNELS, MOVEMENT_PATTERNS)

    except KeyboardInterrupt:
        # Ctrl+Cによる中断を検知
        print("\nプログラムを終了します")

    finally:
        # 必ず全サーボを安全な位置に戻す
        cleanup_servos(kit, SERVO_CHANNELS)


if __name__ == "__main__":
    main()
