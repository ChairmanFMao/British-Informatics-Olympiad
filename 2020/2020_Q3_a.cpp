#include <bits/stdc++.h>
using namespace std;
#define ll long long

// Thinking about what algorithm to use, currently thinking about a depth first search but idk, too many outputs created I think
// Need to use some kind of binary search I think
// Made a recursive solution that works for lower range numbers but, not higher range as it takes ages
// Looked at a version of a solution, need to implement a more efficient way of finding how many strings are possible with a specific prefix
// Slower than the python implementation because it can't use lru_cache


ll combo(int remaining, int letterChoice, int longestSubstring, char last, int lastLength) {
    if (lastLength > longestSubstring)
        return 0;
    if (remaining == 0)
        return 1;

    ll total = 0;
    for (int i = 0; i < letterChoice; i++)
        total += (char) i+65 == last ? combo(remaining-1, letterChoice, longestSubstring, last, lastLength+1) : combo(remaining-1, letterChoice, longestSubstring, (char) i+65, 1);
    return total;
}

void solve() {
    int p, q, r;
    ll n;
    cin >> p >> q >> r >> n;

    stack<char> prefix;
    int lastCount = 0, current = 0;
    char last = ' ';
    while (prefix.size() < r) {
        for (int i = 0; i < p; i++) {
            char c = i+65;
            current = c == last ? lastCount+1 : 1;
            prefix.push(c);
            ll combinations = combo(r - prefix.size(), p, q, c, current);

            if (combinations >= n) {
                last = c;
                lastCount = current;
                break;
            }

            n -= combinations;
            prefix.pop();
        }
    }

    string out = "";
    int prefixSize = prefix.size();
    for (int i = 0; i < prefixSize; i++) {
        out = prefix.top() + out;
        prefix.pop();
    }
    cout << out << "\n";
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    solve();
}