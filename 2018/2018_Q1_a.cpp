#include <bits/stdc++.h>
using namespace std;

// I think that this solution works but I am not entirely sure on how efficient it will be, I think I will just go with it.
// Taking a break 2 hours in, I have solutions for all the questions not sure about how right they are tho

// I think that the score for this paper would be about 35 ish overall as I got the solution for 2 perfect but screwed up 1 and 3
// I am now going to proceed to debug them

// Solution doens't seem to be working well, it gets near but not exact, the answers I get are above what I expect

void solve() {
    double debt = 100;
    double interest, repayment;
    cin >> interest >> repayment;
    interest /= 100;
    repayment /= 100;

    if (abs(1-repayment) < 1e-9) {
        cout << 100 << "\n";
    }

    double total = 100;
    // Used for part b
    int payments = 0;
    while (debt > 0) {
        total += debt * interest;
        debt *= (interest + 1);
        payments++;
        if (debt * repayment > 50) {
            debt -= debt * repayment;
        } else {
            debt -= 50;
        }
    }
    total = ceil(total*100)/100;
    cout << total << "\n";
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    solve();
}