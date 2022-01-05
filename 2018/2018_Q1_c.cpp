#include <bits/stdc++.h>
using namespace std;

// To do this I am just going to brute force all the combinations of interest and repayment
// I think the brute force determined that having the interest as 85 and the repayment as 46 led to the largest amount of repaid debt
// I think this must be true as I even increased the maximum amount of payments to 10000 and it still came out as the answer
// 85 and 46 obtained when adding tweaks to the program, sound more promising

// 0/3 marks, Should get the output 96 and 49

double largest = 0, largestI = 0, largestR = 0;

void solve(double interest, double repayment) {
    double debt = 100;
    interest /= 100;
    repayment /= 100;

    if (abs(1-repayment) < 1e-9) {
        debt = 0;
    }

    double total = 100;
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
        if (payments > 10000) {
            return;
        }
    }
    total = round(total*100)/100;
    if (total > largest) {
        largest = total;
        largestI = interest * 100;
        largestR = repayment * 100;
    }
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    for (int i = 0; i <= 100; i++)
        for (int j = 0; j <= 100; j++)
            solve((double) i, (double) j);
    
    cout << largestI << " " << largestR << "\n";
}