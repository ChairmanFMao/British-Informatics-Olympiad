#include <bits/stdc++.h>
using namespace std;
#define ll long long

// Finding the further node from the number and then finding the furthest node from the furthest node for the width of the graph
// For "326451", I got the longest distance to be 14
// For "183654792", I got the longest distance to be 56

int longestPath = 0;
string longestNode = "";
set<string> visited;

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
    visited.insert(number);
    if (moves > longestPath) {
        longestPath = moves;
        longestNode = number;
    }

    for (int i = 0; i < number.size()-1; i++) {
        string next = number;
        swap(next[i], next[i+1]);
        if (visited.count(next) == 0)
            if (possible(number, i, i+1))
                dfs(next, moves+1);
    }
}

void solve() {
    string number = "183654792";

    dfs(number, 0);

    visited.clear();
    // Don't actually need to reset the longestPath as it should only update if a longer path is found
    dfs(longestNode, 0);

    cout << longestPath << "\n";
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    solve();
}