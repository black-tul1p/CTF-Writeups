#include <stdio.h>
#include <stdlib.h>

void revvy();
void tryToRev(uint);

void main() {
	uint entry;
	printf("Enter value: ");
	scanf("%ld", &entry);
	tryToRev(entry);
	return;
}

void revvy(void) {
	srand(0x11c4);
	return;
}

void tryToRev(uint input) {
	uint var1, var2;

	revvy();
	var1 = rand();
	var2 = rand();

	if ((input ^ var1 ^ 0x3597b741) == var2) {
		printf("Password Accepted! flag: btcf{%d}\n", input); // modified this line from original decompiled code for readability
	} else {
		puts("That\'s incorrect. Try again.\n"); // modified this line from original decompiled code for readability
	}
}
