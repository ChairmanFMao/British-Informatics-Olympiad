#include <bits/stdc++.h>
using namespace std;
#define ll long long

string toRoman(int number) {
    string out = "";
    while (number > 0) {
        if (number >= 1000) {
            out += "M";
            number -= 1000;
        } else if (number >= 900) {
            out += "CM";
            number -= 900;
        } else if (number >= 500) {
            out += "D";
            number -= 500;
        } else if (number >= 400) {
            out += "CD";
            number -= 400;
        } else if (number >= 100) {
            out += "C";
            number -= 100;
        } else if (number >= 90) {
            out += "XC";
            number -= 90;
        } else if (number >= 50) {
            out += "L";
            number -= 50;
        } else if (number >= 40) {
            out += "XL";
            number -= 40;
        } else if (number >= 10) {
            out += "X";
            number -= 10;
        } else if (number >= 9) {
            out += "IX";
            number -= 9;
        } else if (number >= 5) {
            out += "V";
            number -= 5;
        } else if (number >= 4) {
            out += "IV";
            number -= 4;
        } else {
            out += "I";
            number--;
        }
    }
    return out;
}

void solve() {
    set<string> unique;

    for (int i = 1; i < 4000; i++) {
        string current = toRoman(i);
        string out = "";
        int counter = 1;
        for (int j = 0; j < current.size()-1; j++) {
            if (current[j] == current[j+1]) {
                counter++;
            } else {
                out += toRoman(counter) + current[j];
                counter = 1;
            }
        }
        if (counter > 0)
            out += toRoman(counter) + current[current.size()-1];
        unique.insert(out);
    }
    cout << unique.size() << "\n";
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    solve();
}
