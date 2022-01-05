#include <bits/stdc++.h>
using namespace std;
#define ll long long

// Think I got it working after about an hour of coding. However, just finished and it works on the test case so, I'm not sure how through it is.

// 24/24 for this question. Very cool!

// Overall 25/34, this is quite annoying as I made a perfect algorithm but, just didn't manage to correctly complete the follow up questions
// I should do more of them later before the actual test

// Is a structure to store the data about each square
struct square {
    int x;
    int y;
    int wait;
};

// Stores all the squares that are currently on cooldown
queue<square> visited;

// Checks if a specific square is still on cooldown
bool unOccupied(int x, int y) {
    int length = visited.size();
    for (int i = 0; i < length; i++) {
        square current = visited.front();
        if (current.x == x && current.y == y)
            return false;
        visited.pop();
        visited.push(current);
    }
    return true;
}

// Reduces all of the cooldowns by one
void emptyOut() {
    int length = visited.size();
    for (int i = 0; i < length; i++) {
        square current = visited.front();
        visited.pop();
        current.wait--;
        if (current.wait == 0)
            continue;
        visited.push(current);
    }
}

// Turns around until a valid direction is found, otherwise it returns -1 to show that there was no valid direction
int findValidDirection(int x, int y, int d) {
    for (int i = 0; i < 4; i++) {
        if ((d == 0 && unOccupied(x, y+1)) || (d == 1 && unOccupied(x+1, y)) || (d == 2 && unOccupied(x,y-1)) || (d == 3 && unOccupied(x-1, y)))
            return d;
        d++;
        d %= 4;
    }
    return -1;
}

void solve() {
    int t, m;
    string directions;
    cin >> t >> directions >> m;

    // Using 0 as up, 1 as right, 2 as down and 3 as left
    int x = 0, y = 0, direction = 0;
    for (int i = 0; i < m; i++) {
        // Parses the current direction command
        char turn = directions[i%directions.size()];
        direction += turn == 'F' ? 0 : turn == 'R' ? 1 : -1;
        direction += direction >= 4 ? -4 : direction < 0 ? 4 : 0;

        // Adding the visited position to the queue
        square position;
        position.x = x;
        position.y = y;
        position.wait = t+1;
        visited.push(position);

        // Turning until valid direction
        direction = findValidDirection(x, y, direction);
        if (direction == 0)
            y++;
        else if (direction == 1)
            x++;
        else if (direction == 2)
            y--;
        else if (direction == 3)
            x--;
        else
            break;
        
        // Turns the explorer after they have moved
        emptyOut();
    }
    cout << "(" << x << "," << y << ")" << "\n";
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    solve();
}