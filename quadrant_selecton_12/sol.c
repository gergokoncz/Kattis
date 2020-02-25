#include<stdio.h>

int main(){
	long int a, b;
	scanf("%ld\n%ld", &a, &b);
	if (a >= 0){
		if (b >= 0){
			printf("1");
		} else {
			printf("4");
		}
	} else {
		if (b >= 0){
			printf("2");
		} else {
			printf("3");
		}
	}
	return 0;
}
