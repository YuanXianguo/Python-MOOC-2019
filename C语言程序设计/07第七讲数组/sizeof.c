#include <stdio.h>

int main()
{
	int a[10];
	int len;
	len = sizeof(a)/sizeof(a[0]);
	printf("%d\n", len);
	
	return 0;
}


