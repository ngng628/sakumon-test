#include "testlib.h"
#include <bits/stdc++.h>
using namespace std;

// constraints
constexpr int N_MIN = 0;
constexpr int N_MAX = 18;

constexpr int A_MIN = 0;
constexpr int A_MAX = 9;
constexpr int B_MIN = 0;
constexpr int B_MAX = 9;

void ac(){
   quitf(_ok, "ok");
}

void wa(const char* msg = "wrong answer"){
   quitf(_wa, msg);
}

void t_assert(bool b, const char* msg = "wrong answer"){
   if (b) return;
   quitf(_wa, msg);
}

int main(int argc, char** argv) {
   registerTestlibCmd(argc, argv);

   int n = inf.readInt(N_MIN, N_MAX, "N");
   int a = ouf.readInt(A_MIN, A_MAX, "A");
   ouf.readSpace();
   int b = ouf.readInt(B_MIN, B_MAX, "B");
   ouf.readEoln();
   ouf.readEof();


   t_assert(to_string(a).size() == 1);
   t_assert(to_string(b).size() == 1);
   t_assert(a + b == n);

   ac();

   return 0;
}
