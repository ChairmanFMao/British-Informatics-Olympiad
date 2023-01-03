#include <bits/stdc++.h>
using namespace std;
#define ll long long

// Mark scheme says that the answer should be 96 but, I can only get 54 out of this code

bool chosen[10];
int working = 0;

char firstNotIn(queue<char> plan) {
    set<char> in;
    // Need to remember that the size of the queue is variable
    int length = plan.size();
    for (int i = 0; i < length; i++) {
        in.insert(plan.front());
        plan.pop();
    }
    for (int i = 0; i < 8; i++) {
        if (in.count((char)i+65) == 0 && !chosen[i]) {
            chosen[i] = 1;
            return (char) i + 65;
        }
    }
    return ' ';
}

void solve(string s) {
    memset(chosen, 0, 10);
    queue<char> plan;
    for (int i = 0; i < s.size(); i++)
        plan.push(s[i]);
    
    bool good[4];
    memset(good, 0, 4);
    
    for (int i = 0; i < 4; i++) {
        char c = firstNotIn(plan);
        char small = min(c,plan.front()), big = max(c,plan.front());
        if (small == 'A' && big == 'E')
            good[0] = 1;
        if (small == 'B' && big == 'F')
            good[1] = 1;
        if (small == 'C' && big == 'G')
            good[2] = 1;
        if (small == 'D' && big == 'H')
            good[3] = 1;
        plan.pop();
    }
    if (good[0] && good[1] && good[2] && good[3]) {
        working++;
        cout << s << " " << working << "\n";
    }
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    for (int a = 0; a < 8; a++) {
        for (int b = 0; b < 8; b++) {
            for (int c = 0; c < 8; c++) {
                for (int d = 0; d < 8; d++) {
                    for (int e = 0; e < 8; e++) {
                        for (int f = 0; f < 8; f++) {
                            string test = "";
                            test += (char) a+65;
                            test += (char) b+65;
                            test += (char) c+65;
                            test += (char) d+65;
                            test += (char) e+65;
                            test += (char) f+65;
                            solve(test);
                        }
                    }
                }
            }
        }
    }
}
