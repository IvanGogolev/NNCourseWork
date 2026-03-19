#include<iostream>
#include<string>
#include<vector>
#include <random>
#include <chrono>
using namespace std;
mt19937_64 rnd(chrono::steady_clock::now().time_since_epoch().count());
int next(int a, int b){
    return a + rnd()%(b - a + 1);
}
int processInt(int a, int b){
    int res = next(a, b);
    cout << res;
    return res;
}
void processSpace(){
    cout << ' ';
}
void processEoln(){
    cout << endl;
}
void processEof(){
    
}


using namespace std;
int main(int argc, char *argv[]) {
    
    int n = processInt(1, 5);
    processEoln();
    vector<int> a(n + 1);
    a[1] = processInt(1, 5);
    for(int i = 2;i <= n;i += 1){
        processSpace();
        a[i] = processInt(1, 5);
    }
    processEoln();
    int q = processInt(1, 5);
    processEoln();
    for(int i = 1;i <= q;i += 1){
        int l = processInt(1, n);
        processSpace();
        int r = processInt(l, n); 
        processEoln();    
    }
    processEof();
}
