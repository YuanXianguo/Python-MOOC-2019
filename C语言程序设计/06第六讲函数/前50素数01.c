#include <stdio.h>

int isPrime(int i)
{
	int j;
	int ret = 1;
	for ( j=2; j<i; j++)
		{
			if (i%j == 0)
			{
				ret = 0;
				break;
			}
		}
	return ret;
 } 
 
int main()
{
	int i;
	int cnt = 0;
	for ( i=2; cnt<50; i++)
	{
		if (isPrime(i))
		{
			cnt ++;
			printf("%d\t", i);
			if (cnt % 5 == 0)
			{
				printf("\n"); 
			} 
		}
	}
	
	return 0;
 } 
