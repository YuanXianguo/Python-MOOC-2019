#include <stdio.h>

int main()
{
	int x;
	scanf("%d", &x);
	int ret = 1;
	int i;
	
	for ( i=2; i<x; i++ )
	{
		if (x % i == 0)
		{
			ret = 0;
			break;
		}
	}
	if ( ret )
	{
		printf("%d������", x);
	}
	else
	{
		printf("%d��������", x);
	} 
	
	return 0;
 } 
