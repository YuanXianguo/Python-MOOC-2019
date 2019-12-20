#include <stdio.h>

int isPrime(int i, int knownPrimes[], int numberPrimes)
{
	int j;
	int ret = 1;
	for ( j=0; j<numberPrimes; j++)
		{
			if ( i % knownPrimes[j] == 0 )
			{
				ret = 0;
				break;
			}
		}
	return ret;
 } 
 
int main()
{
	const int NUM = 100; 
	//int prime[NUM] = {2};
	int prime[100] = {2};
	int cnt = 1;
	int i = 3;
	while ( cnt < NUM )
	{
		if (isPrime(i, prime, cnt))
		{
			prime[cnt++] = i;
		}
		i ++;
	}
	for ( i=0; i<NUM; i++ )
	{
		printf("%d", prime[i]);
		if ( (i+1)%5 )
		{
			printf("\t");
		}
		else
		{
			printf("\n");
		}
	}
	
	return 0;
 } 
