#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(){
	int n;
	scanf("%d", &n);
	char buf[10000];
	fgets(buf, 10, stdin); // get newline out of the way
	fgets(buf, 10000, stdin);
	
	int makes_sense = 1;
	char *ptr = strtok(buf, " ");
	int c_number = 0;
	
	// loops through splitted string and compare to two possible options
	while(ptr != NULL){
		int a = atoi(ptr);
		c_number++;
		if (strcmp(ptr, "mumble") != 0 && strcmp(ptr, "mumble\n") != 0){
			if (a != c_number){
				makes_sense = 0;
			}
		}
		ptr = strtok(NULL, " ");
	}
	// finish with printing decision
	if (c_number != n){
		makes_sense = 0;
	}
	if (makes_sense == 0){
		printf("something is fishy");
	} else {
		printf("makes sense");
	}
	return 0;
}
