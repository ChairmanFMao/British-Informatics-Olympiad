#include <bits/stdc++.h>
using namespace std;
#define ll long long

// This implementation of creating all of the possible permutations and checking them works well up until about l = 11 ish, then it becomes too inefficient
// Thinking of passing in the last 3 letters to the generatePermutations function so that it can check it faster and on the way rather than calling another function
// Need to try to think of a way to do it in better time complexity
// With some testing turns out my implementation just doesn't work properly, misinterpreted the problem, only fully realized what it means after a long time spent attempting to debug ;-;
// Still don't really get the question after about an hour and a half.
// I get the problem now, its just that I don't get one part of matthewelse's solution that prunes additional choices, the code is functional but slow
// Current implementation borrows a lot from others code, I think it gets about 20 ish marks in testing, I relied very heavily on help for this problem, currently passes all tests but last 2

queue<pair<string,string>> processing;

bool checkValid(string built, char toAdd, string remaining) {
    char smallest = built[0];
    for (int i = 0; i < built.size(); i++) {
        if (built[i] < smallest)
            smallest = built[i];
        else if (built[i] > smallest && built[i] < toAdd)
            return false;
    }
    // This returns false to prevent all the future problems that this would create in later strings
    if (smallest < toAdd)
        for (int i = 0; i < remaining.size(); i++)
            if (toAdd < remaining[i])
                return false;
    return true;
}

void solve() {
    int l;
    cin >> l;
    string p;
    cin >> p;

    string left = "";
    set<char> charsInP;
    for (int i = 0; i < p.size(); i++)
        charsInP.insert(p[i]);
    for (int i = 0; i < l; i++)
        if (!(charsInP.count((char) i + 65)))
            left += (char) (i + 65);
    
    ll permutations = 0;
    processing.push({p, left});
    while (!processing.empty()) {
        string current = processing.front().first, remaining = processing.front().second;
        processing.pop();
        if (remaining.size() == 0) {
            permutations++;
            continue;
        }
        for (int i = 0; i < remaining.size(); i++)
            if (checkValid(current, remaining[i], remaining))
                processing.push({current+remaining[i], remaining.substr(0,i)+remaining.substr(i+1)});
    }
    
    cout << permutations << "\n";
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    solve();
}