#include <stdio.h>

int main(){
	// start by reading amount of following numbers
	int n;
	scanf("%d", &n);
	// init sum of minutes and seconds
	int m_sum = 0;
	int s_sum = 0;
	for (int i = 0; i < n; i++){
		long int cm, cs;
		scanf("%ld %ld", &cm, &cs);
		m_sum += cm;
		s_sum += cs;
	}
	//print results
	double avg_min =  s_sum / (double)(60 * m_sum);
	if (avg_min > 1.0){
		printf("%.8f", avg_min);
	} else {
		printf("measurement error");
	}
}
