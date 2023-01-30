# include <bits/stdc++.h>
using namespace std;

int main () {
   int n;
   cin >> n;

   int a = min(n, 9);
   int b = n - a;
   printf("%d %d\n", a, b);

   return 0;
}
