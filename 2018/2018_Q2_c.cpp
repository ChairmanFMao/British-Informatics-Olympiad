#include <bits/stdc++.h>
using namespace std;
#define ll long long

// I am going to attempt to brute force it and see if it works, the brute force is taking a long time but, I think that it won't take too long
// Turns out it was simply too slow and I had to stop it as I needed to test by code for question 3
// I used the faster generation of the wheel from part b however, I got no answer for brute forcing all the possible values of n from 1 to 1000000, therefore I don't think that there is a second dial

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

void solve(int n) {
    string word = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    string wheel = generateWheel(n);
    string encrypted = "";

    // We use i as the offset here for the incrementation after every character
    for (int i = 0; i < word.size(); i++)
        encrypted += wheel[(word[i] - 65 + i) % 26];
    
    sort(encrypted.begin(),encrypted.end());
    if (encrypted == word)
        cout << n << "\n";
}

int main(void) {
    ios::sync_with_stdio(0);
    //cin.tie(0);

    for (int i = 1; i <= 1000000; i++)
        solve(i);
}