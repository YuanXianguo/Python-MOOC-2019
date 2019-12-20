#include <stdio.h>

int divide(int a, int b, int *result)
{
	int ret = 1;
	if ( b==0 ) ret = 0;
	else
	{
		*result = a / b;
	}
	return ret;
}	
int main()
{
	int a = 15;
	int b = 4;
	int c;
	if ( divide(a, b, &c) )
	{
		printf("%d/%d=%d\n", a, b, c); 
	}	
	
	return 0;
}


