#include <stdlib.h>
#include <stdio.h>

int main(void){
	unsigned long n;
	unsigned long m;
	scanf("%ld %ld\n",&n,&m);
	long w[n];
	for (int i = 0; i < n; i++){
		long cw; 
		scanf("%ld", &cw);
		w[i] = cw;
	}
	for (int i = 0; i < n; i++){
		printf("%ld", w[i]);
	}
	return EXIT_SUCCESS;
}
