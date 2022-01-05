#include <bits/stdc++.h>
using namespace std;

// Looked at a python solution at https://github.com/matthewelse/british-informatics-olympiad/blob/master/2021/q1.py

bool checkPat(string word) {
    // If the word length is one then it must be a pat
    if (word.length() == 1)
        return true;
    // Otherwise iterate through the string seeing if it is possible to divide it into pats
    for (int i = 1; i < word.length(); i++) {
        string l = word.substr(0,i);
        string r = word.substr(i);
        char lmin = 100, rmax = 0;
        // Makes substrings and gets the lowest and highest character values
        for (int i = 0; i < l.length(); i++) {
            if (l[i] < lmin)
                lmin = l[i];
        }
        for (int i = 0; i < r.length(); i++) {
            if (r[i] > rmax)
                rmax = r[i];
        }
        // If the left min is less than the right max we reverse both sides and if they are both pats we return true
        if (lmin > rmax) {
            string rcopy = r;
            reverse(rcopy.begin(), rcopy.end());
            string lcopy = l;
            reverse(lcopy.begin(), lcopy.end());
            if (checkPat(lcopy) && checkPat(rcopy))
                return true;
        }
    }
    // Otherwise they are not pats
    return false;
}

void solve() {
    string s1, s2;
    cin >> s1 >> s2;
    string together = s1 + s2;
    string a = checkPat(s1) ? "YES" : "NO";
    string b = checkPat(s2) ? "YES" : "NO";
    string c = checkPat(together) ? "YES" : "NO";
    cout << a << "\n" << b << "\n" << c << "\n";
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    solve();
}