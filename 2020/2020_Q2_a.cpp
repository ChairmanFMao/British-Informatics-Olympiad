#include <bits/stdc++.h>
using namespace std;
#define ll long long

// Perfectly working solution, took a very long time and did look at a solution for some help but, mainly did on my own
// Took ages debugging this error where I was incrementing the visted value of a room too early

bool chosen[10];

struct Node {
    char value;
    // The two values are for where it goes and how many times used
    vector<pair<char,int>> edges;
    int visited;
};

char firstNotIn(queue<char> plan) {
    set<char> in;
    // Need to remember that the size of the queue is variable
    int length = plan.size();
    for (int i = 0; i < length; i++) {
        in.insert(plan.front());
        plan.pop();
    }
    for (int i = 0; i < 10; i++) {
        if (in.count((char)i+65) == 0 && !chosen[i]) {
            chosen[i] = 1;
            return (char) i + 65;
        }
    }
    return ' ';
}

void solve() {
    string s;
    cin >> s;
    int p, q;
    cin >> p >> q;
    
    memset(chosen, 0, 10);
    queue<char> plan;
    for (int i = 0; i < s.size(); i++)
        plan.push(s[i]);
    vector<Node> rooms;
    for (int i = 0; i < s.size()+2; i++) {
        Node node;
        node.value = (char)i+65;
        node.visited = 0;
        rooms.push_back(node);
    }
    rooms[0].visited++;
    
    while (plan.size() > 0) {
        char c = firstNotIn(plan);
        rooms[c-65].edges.push_back({plan.front(), 0});
        rooms[plan.front()-65].edges.push_back({c, 0});
        plan.pop();
    }
    vector<char> notChosen;
    for (int i = 0; i < s.size()+2; i++) {
        if (chosen[i] == 0)
            notChosen.push_back((char)i+65);
    }
    rooms[notChosen[0]-65].edges.push_back({notChosen[1], 0});
    rooms[notChosen[1]-65].edges.push_back({notChosen[0], 0});

    for (int i = 0; i < s.size()+2; i++)
        sort(rooms[i].edges.begin(), rooms[i].edges.end());

    for (int i = 0; i < s.size()+2; i++) {
        string out = "";
        for (int j = 0; j < rooms[i].edges.size(); j++)
            out += rooms[i].edges[j].first;
        cout << out << "\n";
    }

    // Starting the traversal of the graph part
    int location = 0;
    // We will start by just traversing p steps and then doing the bit with q
    for (int i = 0; i < q; i++) {
        if (i == p)
            cout << rooms[location].value;
        if (rooms[location].visited & 1) {
            rooms[location].edges[0].second++;
            location = rooms[location].edges[0].first-65;
            rooms[location].visited++;
            continue;
        }
        int noEdges = rooms[location].edges.size();
        for (int j = 0; j < noEdges; j++) {
            if (rooms[location].edges[j].second & 1) {
                if (j == noEdges-1) {
                    rooms[location].edges[j].second++;
                    location = rooms[location].edges[j].first-65;
                } else {
                    rooms[location].edges[j+1].second++;
                    location = rooms[location].edges[j+1].first-65;
                }
                rooms[location].visited++;
                break;
            }
        }
        
    }
    cout << rooms[location].value << "\n";
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    solve();
}