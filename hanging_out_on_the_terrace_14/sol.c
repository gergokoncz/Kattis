#include <stdio.h>
#include <string.h>

int main(){
	
	int l, n; // l for limit, n for number of instructions
	int a = scanf("%d %d", &l, &n); 
	int c = 0; // for current number of people on terrace
	int returned = 0; // number of returns
	
	// variables for comparison
	char ent[] = "enter";

	// looping thorugh statements
	for (int i = 0; i < n; i++){
		char step[100];
		int p;
		int a = scanf("%s %d", step, &p);

		// compare
		if (!strcmp(step, ent)){
			if ((p + c) > l){
				returned++;
			} else {
				c += p;
			}
		} else {
			c -= p;
		}
	}
	printf("%d", returned);
	return 0;
}
