#include <stdio.h>

int main()
{
	int min = 1;
	int *p = &min;
	printf("*p=%d\n", *p);
	printf("p[0]=%d\n", p[0]);
	return 0;
}

