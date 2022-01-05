#include <iostream>
#include <queue>
#include <cmath>
using namespace std;
#define ll long long

bool checkPrime(ll n) {
    if (n == 2)
        return 1;
    if (!(n & 1))
        return 0;
    for (int i = 3; i <= ceil(sqrt(n)); i+=2)
        if (!(n % i))
            return 0;
    return 1;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    ll l, p, q;
    cin >> l >> p >> q;

    vector<ll> shortest(l+1);
    for (int i = 0; i <= l; i++)
        shortest[i] = 1e9;
    shortest[p] = 1;
    vector<ll> powers;
    for (int i = 1; i <= l; i <<= 1)
        powers.push_back(i);
    queue<pair<ll,ll>> processing;
    processing.push({p,1});
    while (!processing.empty()) {
        pair<ll,ll> current = processing.front();
        processing.pop();
        if (current.first == q) {
            cout << current.second << "\n";
            return 0;
        }
        for (int i = 0; i < powers.size(); i++) {
            if (current.first - powers[i] > 0) {
                if (current.second + 1 < shortest[current.first-powers[i]]) {
                    if (checkPrime(current.first - powers[i])) {
                        processing.push({current.first-powers[i], current.second+1});
                        shortest[current.first-powers[i]] = current.second+1;
                    }
                }
            } if (current.first + powers[i] <= l) {
                if (current.second + 1 < shortest[current.first+powers[i]]) {
                    if (checkPrime(current.first + powers[i])) {
                        processing.push({current.first + powers[i], current.second + 1});
                        shortest[current.first+powers[i]] = current.second + 1;
                    }
                }
            }
        }
    }
}