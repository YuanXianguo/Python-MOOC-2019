#include <stdio.h>

int main()
{
	int i;
	int* p = &i;
	int *q = &i; 
	
	printf("%p\n", &i);
	printf("%p\n", p);
	printf("%p\n", q);

	return 0;
} 
