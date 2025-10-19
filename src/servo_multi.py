import time
from adafruit_servokit import ServoKit

# ServoKitを初期化
kit = ServoKit(channels=16)

print("2つのサーボモーター同期制御")
print("チャンネル0、1のサーボを同期制御します")

# 使用するサーボチャンネル
servo_channels = [0, 1]

# サーボの動作パターン
patterns = [
    [0, 180],      # パターン1: 0度と180度
    [45, 135],     # パターン2: 45度と135度
    [180, 0],      # パターン3: 180度と0度
    [90, 90],      # パターン4: 両方とも中央位置
]

try:
    for pattern_num, angles in enumerate(patterns, 1):
        print(f"パターン{pattern_num}: {angles}")

        # 全サーボを同時に移動
        for channel, angle in zip(servo_channels, angles):
            kit.servo[channel].angle = angle
            print(f"  チャンネル{channel}: {angle}度")

        time.sleep(3)  # 各パターンの実行時間

    print("全サーボを中央位置に戻します")
    for channel in servo_channels:
        kit.servo[channel].angle = 90

except KeyboardInterrupt:
    print("プログラムを終了します")
    # 全サーボを中央位置に戻す
    for channel in servo_channels:
        kit.servo[channel].angle = 90
    print("全サーボを中央位置に設定しました")
