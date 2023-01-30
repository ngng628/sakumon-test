# リポジトリ管理者向けチュートリアル

## リポジトリ管理者は何をする？

リポジトリの雛形を作ります。

## 環境構築

以下の環境を作りましょう。

- GCC環境
- Python3環境
- Rimeのインストール
   - Rimeについては[こちら](./rime.md)

## やるべきこと

1. GitHub上でリポジトリを作成
2. ローカル環境にディレクトリを作る
3. このサンプルリポジトリのうち、以下をコピペ

   ```
   .github/
   docs/
   scripts/
   .gitignore
   ```

4. `rime_init --git` をする
5. 不都合がなければ `rime add . problem name` もしてあげる
6. GitHub Actions のトリガーを適宜変更する
