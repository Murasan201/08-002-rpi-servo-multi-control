# セットアップガイド

## ハードウェアの準備

### 必要な部品

1. Raspberry Pi本体
2. サーボモーター（SG90など）
3. ジャンパーワイヤー
4. ブレッドボード（オプション）
5. 外部電源（サーボモーターが複数の場合推奨）

### 配線

サーボモーターの接続：
- 赤線（VCC）: 5V電源
- 茶線（GND）: GND
- 橙線（信号）: GPIO端子

## ソフトウェアのセットアップ

### 1. Raspberry Pi OSの更新

```bash
sudo apt update
sudo apt upgrade -y
```

### 2. 必要なパッケージのインストール

```bash
# pigpioデーモンのインストール
sudo apt install pigpio python3-pigpio -y

# pigpioデーモンの起動
sudo systemctl enable pigpiod
sudo systemctl start pigpiod
```

### 3. Pythonパッケージのインストール

```bash
pip install -r requirements.txt
```

## 動作確認

セットアップが完了したら、`examples/`ディレクトリのサンプルスクリプトで動作確認を行ってください。
