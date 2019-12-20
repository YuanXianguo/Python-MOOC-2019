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
		//��ʼ������Ԫ��Ϊ1 
	} 
	for ( j=2; j<25; j++)
	{
		if ( isPrime(j))
		//�����е������ı�����ֵΪ0 
		{
			for ( i=2; i*j<25; i++ )
			{
				primes[i*j] = 0;
			}
		}
	}
	//��ӡ25���ڵ����� 
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
