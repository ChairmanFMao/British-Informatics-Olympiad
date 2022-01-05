#include <bits/stdc++.h>
using namespace std;
#define ll long long

// This works on test case and an extra case that I did manually, I think it works perfectly!
// This works fast enough for n = 1000000 but, times out when n = 1000000000 for part b

// Function now works as intended, generates the alphabet in a messed up order
string generateWheel(int n) {
    bool used[26];
    memset(used, 0, 26);
    string out = "";
    int start = -1;
    int placed = 0;
    while (out.size() < 26) {
        int a = n;
        while (a > 26)
            a = (a/26)*placed+a%26;
        for (int i = 0; i < a; i++) {
            start++;
            if (start > 25)
                start -= 26;
            if (used[start] == 1)
                i--;
        }
        out += (char) (start + 65);
        used[start] = 1;
        placed++;
    }
    return out;
}

void solve() {
    int n;
    string word;
    cin >> n >> word;

    string wheel = generateWheel(n);
    string encrypted = "";
    cout << wheel.substr(0,6) << "\n";

    // We use i as the offset here for the incrementation after every character
    for (int i = 0; i < word.size(); i++)
        encrypted += wheel[(word[i] - 65 + i) % 26];
    
    cout << encrypted << "\n";
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    solve();
}