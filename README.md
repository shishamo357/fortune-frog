# Fortune Frog 

「カエルがあみだくじ」の簡単なミニゲームです。  
クリックでカエルをスタートさせ、あみだくじのルートを行き、おみくじを引いてきてくれます。
結果はランダムで表示です。（カエル任せ）

---

## ゲームの流れ

1. スタート画面で「スタート」ボタンをクリック
2. あみだくじの任意の棒をクリック
3. カエルがルートをたどって移動
4. 一番下に到達すると「運勢」を表示

---

## 参考書

- 『Pythonで学ぶデータ構造とアルゴリズム』
・著：廣瀬　豪

## 使用素材について

このゲーム内の可愛すぎるカエルのドット絵は以下のフリー素材を使用しています：

- 素材提供：[ピクセルガロー](https://hpgpixer.jp/)
  - 利用条件：https://hpgpixer.jp/infomation/info_sozai_condition.html
  - ※非商用利用・リンク掲載による使用が認められています

---

## 制作期間

- 2025年7月10日 昼〜夕方、7月11日 昼〜夜の2日間
実質10〜12時間ほどで一気に企画〜完成まで行いました。

---

## 技術・使用ライブラリ

- Python 3.x
- Pyxel（レトロ風ゲームライブラリ）
- オブジェクト指向設計（クラス分割）

---

## 学び・苦戦したポイント ~ 予定

- Pyxelは日本語非対応のため、結果表示などは英語表記で対応しました。
この仕様に気づくまで1〜2時間ほどハマってしまいました（笑）
- アニメーション処理（カエルの動き）に試行錯誤した
- 状態遷移管理（title → game → result）に時間をかけた
スタート画面押したらそのまま次の画面にまで影響しだした

- 予定があり2日間しか時間が取れなかったので、完成度が低くなってしまいましたので、いつかレベルアップさせます！

---

## その他のファイル

- `prototype.py`: 開発初期に試作したクリック・表示の簡易版です。動作確認用。

---

## 実行方法

1. Python をインストール  
2. `pip install pyxel`
3. このリポジトリをクローン  
4. `frog.pyxres` を Pyxel Editor で編集することでキャラ変更も可能
5. 以下で実行：

```bash
python app.py

