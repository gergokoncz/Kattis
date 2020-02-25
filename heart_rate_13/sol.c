#include<stdio.h>

int main(){
	long int a;
	int b;
	float p;
	scanf("%ld", &a);
	for (int i = 0; i < a; i++){
		scanf("%d %f", &b, &p);
		float min = (b - 1) * 60 / p;
		float correct = b * 60 / p;
		float max = (b + 1) * 60 / p;
		printf("%.4f %.4f %.4f\n", min, correct, max);
	}
}
