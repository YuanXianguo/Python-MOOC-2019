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
	int i,j;
	int primes[25];
	for ( i=0; i<25; i++)
	{
		primes[i] = 1;
		//初始化所有元素为1 
	} 
	for ( j=2; j<25; j++)
	{
		if ( isPrime(j))
		//把所有的素数的倍数赋值为0 
		{
			for ( i=2; i*j<25; i++ )
			{
				primes[i*j] = 0;
			}
		}
	}
	//打印25以内的素数 
	for ( i=2; i<25; i++)
	{
		if ( isPrime(i) )
		{
			printf("%d\t", i);
		}
	}
	printf("\n");
	
	return 0;
 } 
