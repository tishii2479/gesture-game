# ジェスチャーゲームのお題スライドを作成するやつ

## 手順

[marp](https://marp.app/)を使ってスライドを生成しています。
[marp-cli](https://github.com/marp-team/marp-cli)などをインストールする必要があります。

1. `words.txt`にお題を追加する
    - お題は改行区切りで追加する
2. `python3 a.py`を実行して、`content.md`を生成する
3. `content.md`を`content.pdf`に変換する
    - [marp-cli](https://github.com/marp-team/marp-cli)を使う場合
        - `marp --pdf content.md`を実行すると、`content.pdf`が生成される
