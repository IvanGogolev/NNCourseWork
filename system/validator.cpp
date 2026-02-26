#include <iostream>
#include "testlib.h"
 
using namespace std;
 
int main(int argc, char *argv[]) {
    registerValidation(argc, argv);
    int n = inf.readInt(1, 300, "n");
    inf.readSpace();
    int m = inf.readInt(1, 300, "m");
    inf.readSpace();
    int k = inf.readInt(1, 300, "k");
    inf.readEoln();
    
    const int MAX = 1000000000;
    inf.readInt(1, MAX);
    for(int i = 2;i <= n;i++){
    	inf.readSpace();
    	inf.readInt(1, MAX);
    }
    inf.readEoln();
    
    inf.readInt(1, MAX);
    for(int i = 2;i <= m;i++){
    	inf.readSpace();
    	inf.readInt(1, MAX);
    }
    inf.readEoln();
    
    inf.readInt(1, MAX);
    for(int i = 2;i <= k;i++){
    	inf.readSpace();
    	inf.readInt(1, MAX);
    }
    inf.readEoln();
    
    inf.readEof();
}