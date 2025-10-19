# トラブルシューティング

このドキュメントでは、Raspberry Pi サーボモーター制御アプリケーションの開発中に発生する可能性がある問題とその解決策を記載しています。

## 目次

- [インストール時のエラー](#インストール時のエラー)
  - [Error 1: externally-managed-environment](#error-1-externally-managed-environment)
  - [Error 2: ModuleNotFoundError](#error-2-modulenotfounderror)
- [実行時のエラー](#実行時のエラー)

---

## インストール時のエラー

### Error 1: externally-managed-environment

#### エラー内容

```bash
$ pip install -r requirements.txt

error: externally-managed-environment

× This environment is externally managed
╰─> To install Python packages system-wide, try apt install
    python3-xyz, where xyz is the package you are trying to
    install.

    If you wish to install a non-Debian-packaged Python package,
    create a virtual environment using python3 -m venv path/to/venv.
    Then use path/to/venv/bin/python and path/to/venv/bin/pip. Make
    sure you have python3-full installed.
```

#### 原因

このエラーは **PEP 668** による保護機能によるものです。最近のRaspberry Pi OS（Python 3.11以降）では、システムのPython環境を保護するため、pipでのグローバルインストールが制限されています。これはシステムパッケージマネージャ（apt）との競合を防ぐための措置です。

#### 解決策

**仮想環境（virtual environment）を使用する**ことで、この問題を解決できます。

##### 手順

1. プロジェクトディレクトリに移動

```bash
cd /path/to/08-002-rpi-servo-multi-control
```

2. 仮想環境を作成

```bash
python3 -m venv venv
```

3. 仮想環境を有効化

```bash
source venv/bin/activate
```

有効化後、コマンドプロンプトの先頭に `(venv)` が表示されます：

```bash
(venv) pi@raspberrypi:~/work/project/08-002-rpi-servo-multi-control $
```

4. 依存関係をインストール

```bash
pip install -r requirements.txt
```

#### 補足情報

- **仮想環境を無効化する場合**: `deactivate` コマンドを実行
- **新しいターミナルセッションを開始した場合**: 再度 `source venv/bin/activate` を実行する必要があります
- 詳細は [README.md](../README.md) のInstallationセクションを参照してください

#### 代替案（非推奨）

以下の方法もありますが、推奨しません：

1. **--break-system-packages フラグを使用**（システムを破損する可能性があります）
2. **apt でシステムパッケージをインストール**（全パッケージが利用可能とは限りません）

---

### Error 2: ModuleNotFoundError

#### エラー内容

```bash
(venv) pi@raspberrypi:~/work/project/08-002-rpi-servo-multi-control/src $ python servo_basic.py
Traceback (most recent call last):
  File "/home/pi/work/project/08-002-rpi-servo-multi-control/src/servo_basic.py", line 2, in <module>
    from adafruit_servokit import ServoKit
ModuleNotFoundError: No module named 'adafruit_servokit'
```

#### 原因

`requirements.txt` に必要なパッケージが記載されていなかったため、`adafruit_servokit` モジュールがインストールされていませんでした。

プロジェクト初期状態では、以下のような誤った内容になっていました：

```txt
# 誤った requirements.txt の例
RPi.GPIO>=0.7.1    # servo_basic.py では使用していない
pigpio>=1.78        # servo_basic.py では使用していない
```

#### 解決策

`requirements.txt` に正しいパッケージを記載し、再インストールします。

##### 手順

1. `requirements.txt` を確認

正しい内容：

```txt
# サーボモーター制御用ライブラリ
adafruit-circuitpython-servokit>=1.3.0
```

2. 仮想環境を有効化（まだの場合）

```bash
source venv/bin/activate
```

3. パッケージをインストール

```bash
pip install -r requirements.txt
```

4. インストールを確認

```bash
pip list
```

以下のようなパッケージがインストールされていれば成功です：

```
Package                          Version
-------------------------------- -------
adafruit-circuitpython-servokit  1.3.21
Adafruit-Blinka                  8.66.2
adafruit-circuitpython-pca9685   3.4.19
...（その他の依存パッケージ）
```

5. 動作確認

```bash
python -c "from adafruit_servokit import ServoKit; print('Import successful!')"
```

成功すると以下のように表示されます：

```
Import successful!
```

#### 追加情報

**adafruit-circuitpython-servokit とは？**

このライブラリは、Adafruit PCA9685 PWMサーボドライバボードを使用してサーボモーターを制御するためのPythonライブラリです。

主な機能：
- 最大16個のサーボモーターを同時制御
- 角度指定による簡単な位置制御
- I2C通信によるRaspberry Piとの接続

---

## 実行時のエラー

### （今後のエラーがあればここに追記）

---

## よくある質問（FAQ）

### Q1: 仮想環境を作成したのに、ターミナルを再起動すると `(venv)` が表示されなくなった

**A:** 新しいターミナルセッションでは、毎回仮想環境を有効化する必要があります。

```bash
cd /path/to/08-002-rpi-servo-multi-control
source venv/bin/activate
```

### Q2: `pip install` 時に DEPRECATION 警告が表示される

**A:** 一部のパッケージが古いインストール方式を使用しているための警告です。動作には影響ありませんので、無視して問題ありません。

例：
```
DEPRECATION: RPi.GPIO is being installed using the legacy 'setup.py install' method...
```

### Q3: 仮想環境のディレクトリ名を変更したい

**A:** `venv` という名前は慣習的なものです。好きな名前に変更できますが、その場合は `.gitignore` にも追加してください。

例：
```bash
python3 -m venv my_custom_venv
source my_custom_venv/bin/activate
```

### Q4: 実際にサーボモーターが動かない

**A:** 以下を確認してください：

1. **ハードウェア接続**: PCA9685サーボドライバボードが正しく接続されているか
2. **電源供給**: サーボモーターに適切な電源が供給されているか
3. **I2C有効化**: Raspberry PiのI2Cインターフェースが有効になっているか

```bash
# I2Cが有効か確認
sudo raspi-config
# Interface Options → I2C → Enable を選択
```

4. **I2Cデバイスの検出**:

```bash
sudo apt install i2c-tools
i2cdetect -y 1
```

PCA9685のデフォルトアドレス `0x40` が表示されるはずです。

---

## 参考リンク

- [Python仮想環境について](https://docs.python.org/ja/3/tutorial/venv.html)
- [PEP 668 – Marking Python base environments as "externally managed"](https://peps.python.org/pep-0668/)
- [Adafruit ServoKit ライブラリドキュメント](https://docs.circuitpython.org/projects/servokit/en/latest/)
- [Raspberry Pi I2C設定ガイド](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c)

---

## サポート

問題が解決しない場合は、以下の情報を添えてお問い合わせください：

1. Raspberry Pi のモデルとOSバージョン
2. Pythonのバージョン（`python3 --version`）
3. エラーメッセージの全文
4. 実行したコマンドの履歴

```bash
# システム情報の確認
uname -a
python3 --version
pip --version
```
