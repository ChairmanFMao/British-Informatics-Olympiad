#include <bits/stdc++.h>
using namespace std;
#define ll long long

// Program outputed: 99198
// 0/4 marks

// Manged to tweak my code, turns out it was doing completely the wrong thing, it now outputs the correct answer: 9030

bool check(int b) {
    string a = to_string(b);
    for (int i = 0; i < a.size()/2; i++) {
        if (a[i] != a[a.size()-i-1])
            return false;
    }
    return true;
}

void solve() {
    bool palidrome[100000];
    memset(palidrome, 0, 100000);
    for (int i = 0; i < 100000; i++)
        palidrome[i] = check(i);
    int count = 0;
    // Loops over all the numbers
    for (int i = 1; i < 100000; i++) {
        bool good = 1;
        for (int j = 1; j <= i; j++) {
            if (palidrome[j] && palidrome[i-j]) {
                good = 0;
                break;
            }
        }
        if (good)
            count++;
    }
    cout << count << "\n";
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    solve();
}