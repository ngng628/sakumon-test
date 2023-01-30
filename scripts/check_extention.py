# 入力ファイルの拡張子が *.in であるかを確認したかったやつ

from pathlib import Path
import os
import sys

tests = []
def rec(cur, par):
   global tests

   if os.path.isfile(str(cur)):
      return

   for name in os.listdir(cur):
      if name == 'TESTSET':
         tests.append(cur)
      elif name not in ['rime-out']:
         rec(cur / name, cur)

rec(Path(os.getcwd()), -1)

for path in tests:
   with open(path / 'TESTSET') as f:
      print(f.read())
   print('====')