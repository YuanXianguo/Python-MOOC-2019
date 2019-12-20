#include <stdio.h>

int main()
{
	int i,j;
	int ret = 1;
	int cnt = 0;
	for ( i=2; i<=100; i++)
	{
		for ( j=2; j<i; j++)
		{
			if (i%j == 0)
			{
				ret = 0;
				break;
			}
		}
	    if (ret)
		{
			cnt ++;
			printf("%d\t", i);
			if ( cnt%5 == 0)
			{
				printf("\n");
			}
		}
		ret = 1;
	}
	
	return 0;
 } 
