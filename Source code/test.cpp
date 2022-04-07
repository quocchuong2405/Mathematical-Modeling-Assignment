#include <bits/stdc++.h>
using namespace std;

int main() {
    int a,t, u, v, x,n;
    
    n = 24;
    x = ((n+1)/2);
    
    while (n < x*x) {
    	x = x -1;
	}
	cout << "x: " << x;
    return 0;
}
