# 作問リポジトリサンプル

このリポジトリがそのままサンプルとして利用できます。

- リポジトリを運用する人向け => [docs/admin.md](./docs/admin.md)
- Rimeの使い方 => [docs/rime.md](./docs/rime.md)
- Git/GitHubの使い方 => [docs/git.md](./docs/git.md)

## 制約

リポジトリは以下の制約を満たしている前提でテストを行っています。

- 作問ディレクトリ直下に問題ディレクトリが存在する
- generator / validation は C++ で記述されている

## 対応していないこと

- C/C++/Ruby/Python以外の言語でのジャッジ
- GitHub Actions をたっっっくさん実行する
   - Private リポジトリにするので、あまりに酷使すると使えなくなります
   - https://docs.github.com/ja/billing/managing-billing-for-github-actions/about-billing-for-github-actions
   - 一回のテストで5分消費するとしても400回は耐えるので、よほどのことが無い限り大丈夫だとは思います

## 情報
- [AOJの実行環境 _ Aizu Online Judge](https://onlinejudge.u-aizu.ac.jp/system_info)