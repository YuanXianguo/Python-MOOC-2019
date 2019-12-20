#include <stdio.h>

int main()
{
	int a,b;
	scanf("%d %d", &a, &b);
	int ret = 0;
	int i;
	for ( i=1; i<=a && i<=b; i++ )
	{
		if ( a%i == 0 )
		{
			if ( b%i == 0 )
			{
				ret = i;
			}
		}
	}
	printf("%d和%d的最大公约数是%d", a, b, ret); 
	
	return 0;
 } 
