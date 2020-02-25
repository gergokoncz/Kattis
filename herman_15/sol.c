#include<stdio.h>
#include<math.h>
#define PI acos(-1.0)

int main(){
	long int r;
	int a = scanf("%ld", &r);
	printf("%.7f\n", (double)(r * r * PI));
	printf("%ld\n", r * r * 2);
	return 0;
}
