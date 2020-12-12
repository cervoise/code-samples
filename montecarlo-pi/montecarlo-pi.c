#include <stdio.h>
#include <stdlib.h>

int main() {
	int i, N, z;
	double x, y, pi;
	
	N = 10000000;
	z = 0;

	for (i = 0; i < N; i++) {
		x = (double)rand() / (double)RAND_MAX;
		y = (double)rand() / (double)RAND_MAX;
		if( (x*x+y*y)< 1) z++; 
	}

	pi = 4*(double)z/(double)N ;

	printf("Estimation de pi: %f\n", pi);
	return 0;
}