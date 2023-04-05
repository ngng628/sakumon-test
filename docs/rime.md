# Rime の使い方

## はじめに

コンテストを開くためには問題とデータセットを作らないといけません。データセットを一から作るのは大変です。
この記事ではデータセット作成の助けになるツールであるRimeの説明をします。

説明の殆どはbeetさんのブログ記事を参考にして執筆しています。


## リポジトリの作成

GitHubを使うと良いです。

部外者から見られるとまずいので、🔒Privateで作成すると良いです。

リポジトリを作成したら、このリポジトリの以下のフォルダ・ファイルをコピペすると良いです。
 - `docs/**`
 - `.github/**`
 - `README.md`

Git・GitHubの使い方はこちら => [Git/GitHubの使い方](./git.md)

> **Note**
> Private にすると GitHub Actions の無料枠に制限ができるので注意してください。
> どうしても枠が足りない場合は、課金するか、トリガーを減らすなどすると良いです。

## Rimeのインストール

Rimeのドキュメント : https://rime-doc.readthedocs.io/ja/latest/

**Python/Pipの環境を用意してください。**

Rimeはpipでインストールします。

```sh
$ pip3 install git+https://github.com/icpc-jag/rime
```

Rimeが自動でエディタが開くことがありますが、環境変数 `$EDITOR` で指定されたエディタが使用されます。
デフォルトでは `vim` が使用されている場合が多いため、苦手な人は変更しておくと良いです。


```sh
# `~/.bashrc` または `~/.zshrc` に使いたいエディタへのパスを追記
# パスは `which code` で検索できます。
export EDITOR=/usr/local/bin/code
```

> **Note**
> `rime` が使えるようにならない場合は、Pythonのパスが通っていないかもしれません。
>
> `~/.bashrc` または `~/.zshrc` に以下を追記してください。（Macの場合は `.zshrc` がデフォルトです）
> ```sh
> # 自分の環境に合わせてパスは変更してください
> $ export PATH=/Users/{ngng628}/Library/Python/3.10/bin:$PATH
> ```

## 作問用ディレクトリの作成

作業用のディレクトリを作ります。GitHubでリポジトリを作ってからそれをcloneすると良いと思います。

```sh
$ rime_init --git
```

で `PROJECT` ファイルと `common/` ディレクトリが作成されます。
`common/` ディレクトリの下にはtestlib.hが入っているはずです。

この作業はリポジトリ管理者がはじめに行っておくと良いです。

## 問題用ディレクトリの作成

```sh
$ rime add . problem <problem_dir_name>
```

で、`problem_dir_name` というディレクトリが作成されます。
例えば AplusB という問題を作るなら、

```
$ rime add . problem AplusB
```

となります。上のコマンドを打つと `PROBLEM` ファイルが開かれます。

`reference_solution` は基準となるAC解（想定解）のディレクトリ名を設定します。
例えば `AC-writer/` が想定の場合、

```py
# -*- coding: utf-8; mode: python -*-

pid='X'

problem(
  time_limit=1.0,
  id=pid,
  title=pid + ": Your Problem Name",
  #wiki_name="Your pukiwiki page name", # for wikify plugin
  #assignees=['Assignees', 'for', 'this', 'problem'], # for wikify plugin
  #need_custom_judge=True, # for wikify plugin
  reference_solution='AC-writer',
  )

atcoder_config(
  task_id=None # None means a spare
)
```

となります。この作業を行わないと、辞書順で最小のものが想定解となってしまいます。

## 解答用ディレクトリの作成

想定解・嘘解法を追加します。

```sh
$ rime add <parent_problem_dir_name> solution <solution_dir_name>
```

で、`parent_problem_dir_name/` 下に `solution_dir_name/` というディレクトリが作成されます。

例えば先ほど作成したukukuがカレントディレクトリの時に `AC-writer/` という解答用ディレクトリを作りたいなら

```sh
$ rime add . solution AC-writer
```

となります。上のコマンドを実行すると `SOLUTION` ファイルが開きます。

ここで解答プログラムの名前を設定します。たとえば `main.cpp` という名前にするなら

```py
# -*- coding: utf-8; mode: python -*-

## Solution
#c_solution(src='main.c') # -lm -O2 as default
cxx_solution(src='main.cpp', flags=['-std=c++17', '-O2']) # -std=c++11 -O2 as default
#java_solution(src='Main.java', encoding='UTF-8', mainclass='Main')
#java_solution(src='Main.java', encoding='UTF-8', mainclass='Main',
#              challenge_cases=[])
#java_solution(src='Main.java', encoding='UTF-8', mainclass='Main',
#              challenge_cases=['10_corner*.in'])
#script_solution(src='main.sh') # shebang line is required
#script_solution(src='main.pl') # shebang line is required
#script_solution(src='main.py') # shebang line is required
#script_solution(src='main.rb') # shebang line is required
#js_solution(src='main.js') # javascript (nodejs)
#hs_solution(src='main.hs') # haskell (stack + ghc)
#cs_solution(src='main.cs') # C# (mono)

## Score
#expected_score(100)
```

となります。`flags` の中身はジャッジ環境に合わせて変更してください。

**想定嘘解法**の場合は、`challenge_cases=[]` を追記します。

```py
cxx_solution(src='main.cpp', flags=['-std=c++17', '-O2'], challenge_cases=[]) # -std=c++11 -O2 as default
```

## 解答プログラムの作成

先ほど作った解答用ディレクトリの下（`AplusB/AC-writer/main.cpp`）に書きます。

以降の説明では $2$ つの整数 $a,b$ を入力し、その和を出力する問題を考えます。

C++で実装すると以下のようになります。

```cpp
# include <bits/stdc++.h>
using namespace std;

int main() {
   int a, b;
   cin >> a >> b;
   cout << a + b << '\n';
}
```

## テスト用ディレクトリの作成

```sh
$ rime add <parent_problem_dir_name> testset <testset_dir_name>
```

で、`parent_problem_dir_name/` 下に `testset_dir_name/` というディレクトリが作成されます。

例えば先ほど作成した `AplusB/` がカレントディレクトリの時に `tests/` というテスト用ディレクトリを作りたいなら、

```
$ rime add . testset tests
```

となります。上のコマンドを実行するとTESTSETファイルが開きます。

ここで generator と validator の設定をします。generator は入力の生成を行い、validator は入力の検証を行います。

**validator を用意しないと入力がバグっていて悲しいことになる可能性があるので必ず用意しましょう。
できれば複数人で独立に用意するべきです。**

ここでは `generator.cpp` と `validator.cpp` というファイル名にすることにします。


```py
# -*- coding: utf-8; mode: python -*-

## Input generators.
#c_generator(src='generator.c')
cxx_generator(src='generator.cpp', dependency=['testlib.h'])
#java_generator(src='Generator.java', encoding='UTF-8', mainclass='Generator')
#script_generator(src='generator.pl')

## Input validators.
#c_validator(src='validator.c')
cxx_validator(src='validator.cpp', dependency=['testlib.h'])
#java_validator(src='Validator.java', encoding='UTF-8',
#               mainclass='tmp/validator/Validator')
#script_validator(src='validator.pl')

## Output judges.
#c_judge(src='judge.c')
#cxx_judge(src='judge.cc', dependency=['testlib.h'],
#          variant=testlib_judge_runner)
#java_judge(src='Judge.java', encoding='UTF-8', mainclass='Judge')
#script_judge(src='judge.py')

## Reactives.
#c_reactive(src='reactive.c')
#cxx_reactive(src='reactive.cc', dependency=['testlib.h', 'reactive.hpp'],
#             variant=kupc_reactive_runner)
#java_reactive(src='Reactive.java', encoding='UTF-8', mainclass='Judge')
#script_reactive(src='reactive.py')

## Extra Testsets.
# icpc type
#icpc_merger(input_terminator='0 0\n')
# icpc wf ~2011
#icpc_merger(input_terminator='0 0\n',
#            output_replace=casenum_replace('Case 1', 'Case {0}'))
#gcj_merger(output_replace=casenum_replace('Case 1', 'Case {0}'))
id='X'
#merged_testset(name=id + '_Merged', input_pattern='*.in')
#subtask_testset(name='All', score=100, input_patterns=['*'])
# precisely scored by judge program like Jiyukenkyu (KUPC 2013)
#scoring_judge()
```

## generator / validatorの作成

Rime では generator と validator を書く際に `testlib.h` というライブラリを使います。

- https://github.com/MikeMirzayanov/testlib
- [read*のまとめ](https://scrapbox.io/ecasdqina-cp/testlib_read_%E7%B3%BB%E3%81%BE%E3%81%A8%E3%82%81)
- [generator・validator・judgeの例](https://scrapbox.io/ecasdqina-cp/Rime_TESTSET)


詳しい使い方は公式のサンプル等を参照してください。

今回は以下のようになります。

20個のランダムケースを作るなら

```cpp
#include "testlib.h"
#include<bits/stdc++.h>
using namespace std;

const int MIN_A = 1;
const int MAX_A = 1000;
const int MIN_B = 1;
const int MAX_B = 1000;

int main(int argc, char* argv[]){
  registerGen(argc, argv, 1);
  for (int t = 0; t < 20; t++) {
    ofstream of(format("02_random_%02d.in", t+1).c_str());
    of << rnd.next(MIN_A, MAX_A) << endl;
    of << rnd.next(MIN_B, MAX_B) << endl;
    of.close();
  }
  return 0;
}
```

```cpp
#include "testlib.h"
#include<bits/stdc++.h>
using namespace std;

const int MIN_A = 1;
const int MAX_A = 1000;
const int MIN_B = 1;
const int MAX_B = 1000;

int main(int argc, char* argv[]){
  registerValidation(argc, argv);
  inf.readInt(MIN_A, MAX_A, "A");
  inf.readEoln();
  inf.readInt(MIN_B, MAX_B, "B");
  inf.readEoln();
  inf.readEof();
  return 0;
}
```

制約はconstで宣言しておいて generator と validator で共有するのがいいと思います。（`constrains.h`を作成してインクルードするのもありかもしれません。）

入力に余計な空白や改行が1つでもあるとエラーになるので注意してください。

空白は `readSpace`, 改行は `readEoln`, 整数は `readInt` や `readLong`, 文字列は `readToken` で読み込めます。
最後に `readEof` が必要です。

## テストの実行

ようやく準備が整ったのであとはテストです。
問題用ディレクトリに移動して

```sh
rime test -k
```

で全ての解答ディレクトリについてテストが行われます。

特定の解答ディレクトリだけテストを行いたい場合はtestの後ろにディレクトリ名をつけます

```sh
$ rime test AC-writer
```

> **Note**
> Macを使っていると g++ が clang であるせいでうまく動作しない場合があります。
>
> まず、g++ をインストールしてない場合は `brew install g++`
>
> すると、`g++-12` のように `g++-*` がインストールされるはずです。
> これを環境変数 `CXX` に設定します。
>
> ```sh
> # ~/.bashrc または ~/.zshrc に追記
> # パスは `which g++-12` で検索できます。
> export CXX=/opt/homebrew/bin/g++-12
> ```


## テストケースの書き出し
ジャッジサーバーにアップロードする際には問題ディレクトリで

```sh
$ rime pack
```

コマンドを実行します。rime-outディレクトリの下にatcoderという名前のディレクトリが作成され、その下のin/outに入力/出力ファイルが書き出されます。

