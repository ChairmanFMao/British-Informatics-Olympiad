#include <bits/stdc++.h>
using namespace std;
#define ll long long

// To do this I am going to generate all of the possible groups for the combos
// For "12345", I got the longest group to be 6
// For "123456789", It was taking a long time and eventually outputted 216, I am going to improve the code and try to run it again, which it also outputted 216 in much less time

int longestVisted = 0;
set<string> visited;
set<string> perms;
map<string,bool> used;

void generatePerms(string built, string remaining) {
    if (remaining.size() == 0) {
        perms.insert(built);
        return;
    }
    for (int i = 0; i < remaining.size(); i++)
        generatePerms(built + remaining[i], remaining.substr(0,i) + remaining.substr(i+1));
}

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
    used[number] = 1;
    for (int i = 0; i < number.size()-1; i++) {
        string next = number;
        swap(next[i], next[i+1]);
        if (visited.count(next) == 0)
            if (possible(number, i, i+1))
                dfs(next, moves+1);
    }
}

void solve(string number) {

    dfs(number, 0);

    if (visited.size() > longestVisted)
        longestVisted = visited.size();
    visited.clear();
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    generatePerms("", "123456789");

    vector<string> uniquePerms(perms.begin(), perms.end());
    for (int i = 0; i < uniquePerms.size(); i++)
        used[uniquePerms[i]] = 0;
    
    for (int i = 0; i < uniquePerms.size(); i++)
        if (used[uniquePerms[i]] == 0)
            solve(uniquePerms[i]);
    
    cout << longestVisted << "\n";
}