#include <iostream>
#include "testlib.h"
using namespace std;
int main(int argc, char *argv[]) {
    registerValidation(argc, argv);
    int n = inf.readInt(1, 5);
    inf.readEoln();
    vector<int> a(n + 1);
    a[1] = inf.readInt(1, 5);
    for(int i = 2;i <= n;i += 1){
        inf.readSpace();
        a[i] = inf.readInt(1, 5);
    }
    inf.readEoln();
    int q = inf.readInt(1, 5);
    inf.readEoln();
    for(int i = 1;i <= q;i += 1){
        int l = inf.readInt(1, n);
        inf.readSpace();
        int r = inf.readInt(l, n); 
        inf.readEoln();    
    }
    inf.readEof();
}