# 作問リポジトリサンプル

このリポジトリがそのままサンプルとして利用できます。

- リポジトリを運用する人向け => [docs/admin.md](./docs/admin.md)
- Rimeの使い方 => [docs/rime.md](./docs/rime.md)
- Git/GitHubの使い方 => [docs/git.md](./docs/git.md)

## 対応していないこと

- C/C++/Ruby/Python以外の言語でのジャッジ
- Python3.6系サポート（なんかエラー言われたので3.8にしました）
- 入力のファイルが `*.in` であることの確認（できればしたい）
- 問題文に関する校閲・HTMLのLint
   - **ただし、一部対応しています**
      - 「問題」「制約」「入力」「出力」「入力例1」「出力例1」の流れで書かれているか
      - タイトルのみで `<h2>` を使っているか
      - `<code></code>` や `\(\)` の前後で空白を入れているか
- GitHub Actions をたっっっくさん実行する
   - Private リポジトリにするので、あまりに酷使すると使えなくなります
   - https://docs.github.com/ja/billing/managing-billing-for-github-actions/about-billing-for-github-actions
   - 一回のテストで5分消費するとしても400回は耐えるので、よほどのことが無い限り大丈夫だとは思います

## 情報
- [AOJの実行環境 _ Aizu Online Judge](https://onlinejudge.u-aizu.ac.jp/system_info)
