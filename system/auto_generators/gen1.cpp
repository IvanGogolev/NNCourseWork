#include "testlib.h"
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;






int test_id = 0;

void print_test(int a, int b) {
	startTest(++test_id);
	printf("%d %d\n", a, b);
	
	

}


void samples(){
	print_test(0, 1);
	print_test(10, 15);
	print_test(14, 17);

}



int main(int argc, char* argv[]) {
	registerGen(argc, argv, 1);

	samples();
	

	return 0;

}