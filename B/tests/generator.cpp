# include "testlib.h"
# include <bits/stdc++.h>
# define rep(i, n) for (int i = 0; i < int(n); i++)
using namespace std;

// constraints
constexpr int N_MIN = 0;
constexpr int N_MAX = 18;

int main(int argc, char* argv[]) {
   registerGen(argc, argv, 1);

   // sample
   {
      ofstream ofs("01_sample_01.in");
      ofs << 2 << endl;
      ofs.close();
   }
   {
      ofstream ofs("01_sample_02.in");
      ofs << 3 << endl;
      ofs.close();
   }

   // random
   rep (ts, 5) {
      ofstream ofs(format("02_random_%02d.in", ts + 1).c_str());
      ofs << rnd.next(N_MIN, N_MAX) << endl;
      ofs.close();
   }

   // hack
   {
      ofstream ofs("03_hack_01.in");
      ofs << 0 << endl;
      ofs.close();
   }
   {
      ofstream ofs("03_hack_02.in");
      ofs << 18 << endl;
      ofs.close();
   }

   return 0;
}