import time
from adafruit_servokit import ServoKit

# ServoKitを16チャンネルで初期化
kit = ServoKit(channels=16)

print("SG90サーボモーター制御を開始します")
print("チャンネル0のサーボを動かします")

try:
    while True:
        # 0度に移動
        print("角度: 0度")
        kit.servo[0].angle = 0
        time.sleep(2)

        # 90度に移動
        print("角度: 90度")
        kit.servo[0].angle = 90
        time.sleep(2)

        # 180度に移動
        print("角度: 180度")
        kit.servo[0].angle = 180
        time.sleep(2)

        # 90度に戻る
        print("角度: 90度（中央位置）")
        kit.servo[0].angle = 90
        time.sleep(2)

except KeyboardInterrupt:
    print("プログラムを終了します")
    # サーボを中央位置に戻す
    kit.servo[0].angle = 90
    print("サーボを中央位置に設定しました")
