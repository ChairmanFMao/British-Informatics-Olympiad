#include <bits/stdc++.h>
using namespace std;
#define ll long long

// Testing with n = 1,000,000,000 turns out brute force is way too slow
// I know that the first letter is "K", might come back to this later, can't think of an easy way to do it rn
// Thinking of trying to make a way that would involve dividing the number by 26 but not quite sure on the algorithm yet
// I made an algorithm that reduces n fast and I got as an output "LKBXIY" which I think is right but, I don't have a way to verify

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
    int n = 1000000000;

    string wheel = generateWheel(n);
    string encrypted = "";
    cout << wheel.substr(0,6) << "\n";
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    solve();
}