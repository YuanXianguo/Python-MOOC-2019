#include <stdio.h>

int main()
{
	int i = 0;
	
	printf("0x%X\n", &i);
	printf("%p\n", &i);
	printf("%lu\n", sizeof(int));
	printf("%lu\n", sizeof(&i));
	 
	return 0;
 } 
