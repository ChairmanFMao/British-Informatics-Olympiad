#include <bits/stdc++.h>
#include <chrono>
using namespace std;
using namespace std::chrono;

// Used a permute function that I copied off geeks for geeks as well as dijkstra's algorithm to make my code run fast
// With a bit of variation I managed to get the longest test(27 depth) to execute in just under a second
// Would get full marks in this second for the thing!
// We LOVE cpp and its INSANE efficiency, python will never be able to get on it's level

map<string, int> depths;

// All copied off geeks for geeks
void permute(string s, string answer) {
    if (s.length() == 0) {
        depths[answer] = 2147483647;
        return;
    }
    for (int i = 0; i < s.length(); i++) {
        char ch = s[i];
        string left = s.substr(0,i);
        string right = s.substr(i+1);
        string rest = left + right;
        permute(rest, answer+ch);
    }
}

void solve() {
    string b;
    cin >> b;
    if (b == "A") {
        cout << 1 << "\n";
        return;
    }
    int required = b.size();
    queue<pair<string, int>> potential;
    depths["AB"] = 2;
    string thing = "";
    for (int i = 65; i < 74; i++) {
        thing += (char) i;
        permute(thing, "");
    }
    potential.push({"AB", 2});

    while (!potential.empty()) {
        string current = potential.front().first;
        int moves = potential.front().second;
        potential.pop();
        if (current == b) {
            cout << depths[current] << "\n";
            return;
        }

        if (current.size() < required) {
            char biggest = 0;
            for (int i = 0; i < current.size(); i++) {
                if (current[i] > biggest)
                    biggest = current[i];
            }
            string added = current + ((char) (biggest+1));
            potential.push({added, moves+1});
        }

        swap(current[0], current[1]);
        if (moves+1 < depths[current]) {
            potential.push({current, moves+1});
            depths[current] = min(moves+1, depths[current]);
        }
        swap(current[0], current[1]);

        string move = current.substr(1) + current[0];
        if (moves+1 < depths[move]) {
            potential.push({move, moves+1});
            depths[move] = min(moves+1, depths[move]);
        }
    }
    
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    auto start = high_resolution_clock::now();
    solve();
    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<milliseconds>(stop-start);
    cout << duration.count() << "\n";
}