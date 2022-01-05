#include <bits/stdc++.h>
using namespace std;
#define ll long long

// Implemented a dfs and it seems to work fine and produce the desired output for the test case, not sure about the efficiency tho
// Actually seems to be working fine for bigger inputs which is great, but I can't verify that the answers are actually correct

// Code doesn't work as intended
// Solution that I looked at used a bfs instead of a dfs idk which is better tho
// I think that there is an error with the checking if the string is possible, because it generates 10 outputs where there should only be 9
// Not sure how to stop the code looping over itself, cba to do bfs, I will do codewars now

set<string> seen;
int longestPath = 0;

bool possible(string number, int first, int second) {
    if (number.size() < 3)
        return false;
    int big = max(number[first]-48,number[second]-48), small = min(number[first]-48,number[second]-48);
    if (first == 0)
        return big > number[second+1] - 48 && small < number[second+1] - 48;
    else if (second == number.size()-1)
        return big > number[first-1] - 48 && small < number[first-1] - 48;
    else
        return (big > number[second+1] - 48 && small < number[second+1] - 48) || (big > number[first-1] - 48 && small < number[first-1] - 48);
}

void dfs(string number, int moves) {
    seen.insert(number);
    if (moves > longestPath)
        longestPath = moves;
    
    for (int i = 0; i < number.size()-1; i++) {
        string next = number;
        swap(next[i], next[i+1]);
        if (seen.count(next) == 0)
            if (possible(number, i, i+1))
                dfs(next, moves+1);
    }
}

void solve() {
    int d;
    string number;
    cin >> d >> number;

    seen.insert(number);
    dfs(number, 0);
    vector<string> seenVector(seen.begin(), seen.end());
    for (int i = 0; i < seenVector.size(); i++)
        cout << seenVector[i] << " ";

    cout << longestPath << "\n";
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    solve();
}