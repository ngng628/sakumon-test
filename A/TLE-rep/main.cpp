# include <bits/stdc++.h>

int main() {
   int a, b;
   std::cin >> a >> b;

   int ans = a;
   for (long long i = 0; i < 100LL * std::abs(b); i++) {
      if (i < std::abs(b)) {
         ans += b < 0 ? -1 : 1;
      }
   }

   std::cout << ans << std::endl;
}