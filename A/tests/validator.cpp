# include "testlib.h"
# include <bits/stdc++.h>
using namespace std;

// constraints
constexpr int A_MIN = -1'000'000'000;
constexpr int A_MAX = 1'000'000'000;
constexpr int B_MIN = -1'000'000'000;
constexpr int B_MAX = 1'000'000'000;

int main(int argc, char* argv[]) {
   registerValidation(argc, argv);

   int a = inf.readInt(A_MIN, A_MAX, "A");
   inf.readSpace();
   int b = inf.readInt(A_MIN, A_MAX, "B");
   inf.readEoln();
   inf.readEof();

   return 0;
}