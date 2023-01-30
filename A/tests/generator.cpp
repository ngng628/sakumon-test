# include "testlib.h"
# include <bits/stdc++.h>
# define rep(i, n) for (int i = 0; i < int(n); i++)
using namespace std;

// constraints
constexpr int A_MIN = -1'000'000'000;
constexpr int A_MAX = 1'000'000'000;
constexpr int B_MIN = -1'000'000'000;
constexpr int B_MAX = 1'000'000'000;

int main(int argc, char* argv[]) {
   registerGen(argc, argv, 1);

   // sample
   {
      ofstream ofs("01_sample_01.in");
      ofs << 1 << ' ' << 2 << endl;
      ofs.close();
   }
   {
      ofstream ofs("01_sample_02.in");
      ofs << -2 << ' ' << -1 << endl;
      ofs.close();
   }

   // random
   rep (ts, 5) {
      ofstream ofs(format("02_random_%02d.in", ts + 1).c_str());
      ofs << rnd.next(A_MIN, A_MAX) << ' ' << rnd.next(B_MIN, B_MAX) << endl;
      ofs.close();
   }

   // hack
   {
      ofstream ofs("03_hack_01.in");
      ofs << A_MIN << ' ' << B_MIN << endl;
      ofs.close();
   }
   {
      ofstream ofs("03_hack_02.in");
      ofs << A_MAX << ' ' << B_MAX << endl;
      ofs.close();
   }

   return 0;
}