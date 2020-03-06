#include <stdio.h>
#include <string.h>

int main(){
	int n;
	char str1[1000];
	char str2[1000];
	scanf("%d\n", &n);
	fgets(str1, 1000, stdin);
	fgets(str2, 1000, stdin);
	int length = strlen(str1);
	int success = 0;
	if (n % 2 == 1){
		for(int i = 0; i < length; i++){
			char a = str1[i];
			char b = str2[i];
			if (b == a && (a == '0' || a == '1')){
				success = 1;
			}
		}
	} else {
		for(int i = 0; i < length; i++){
			char a = str1[i];
			char b = str2[i];
			if (b != a && (a == '0' || a == '1')){
				success = 1;
			}
		}
	}
	if (success == 1){
		printf("Deletion failed");
	} else {
		printf("Deletion succeeded");
	}
	return 0;
}
