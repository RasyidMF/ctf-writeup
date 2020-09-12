#include <stdio.h>
#include <stdbool.h>
#include <string.h>

char * license = "REDACTED";

bool check_license(char * licenses) {
	if (strcmp(licenses, license) == 0) {
		return true;
	} else {
		return false;
	}
}

int main(void) {
	char * input;
	
	printf("Input Your License: ");

	scanf("%s", input);
	
	if (check_license(input)) {
		printf("Success Activated License: %s \n", license);
	} else {
		puts("Wrong License!");
	}
}
