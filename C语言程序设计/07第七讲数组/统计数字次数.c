#include<stdio.h>

int main()
{
	const int NUMBER = 10;
	//int count[NUMBER] = {0};
	int count[10] = {0};
	int num;
	int i;
	
	scanf("%d", &num);
	while ( num != -1 )
	{	
		if ( num >= 0 && num < NUMBER )
		{
			count[num] ++;
		}
		scanf("%d", &num);
	}
	
	for ( i=0; i<NUMBER; i++ )
	{
		if ( count[i] )
		{
			printf("%d出现了%d次\n", i, count[i]);
		}
	}

    return 0;
}

