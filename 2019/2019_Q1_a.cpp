#include <bits/stdc++.h>
using namespace std;
#define ll long long

// Initally made a very simple implementation that will not work for very long numbers
// 678999876 causes an error
// 99999999999999 causes an error
// 999999999999999 causes an error
// These errors where due to the 9 overflow and : were created when their acsii value was incremented
// Overall 22/25 marks

// Changed the code so that it deals with inputs that are all 9, gaining an extra 2 marks
// With changes and review of code, I got marks to 30/31.
// To make solution perfect I need to carry ones left and right and even extend the number of digits the number has, but it is a hastle to implement so I didn't.

// Overall for the whole question I got 24/31 first try and took about 45 ish mins.

void solve() {
    string asString, copy;
    cin >> asString;
    copy = asString;
    int length = asString.size();
    if (length == 1) {
        if (asString[0] == '9')
            cout << 11 << "\n";
        else
            cout << ++asString[0] << "\n";
        return;
    }
    bool all9 = 1;
    for (int i = 0; i < length; i++) {
        if (asString[i] != '9') {
            all9 = 0;
            break;
        }
    }
    if (all9) {
        string out = "1";
        for (int i = 0; i < length-1; i++)
            out += "0";
        out += "1";
        cout << out << "\n";
        return;
    }
    for (int i = 0; i < length/2; i++)
        asString[length-i-1] = asString[i];
    if (asString <= copy) {
        if (length & 1) {
            if (asString[(length/2)] == '9') {
                asString[(length/2)] = '0';
                asString[(length/2)+1]++;
                asString[(length/2)-1]++;
            } else
                asString[(length/2)]++;
        } else {
            asString[(length/2)-1]++;
            asString[(length/2)]++;
        }
    }
    cout << asString << "\n";
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    solve();
}