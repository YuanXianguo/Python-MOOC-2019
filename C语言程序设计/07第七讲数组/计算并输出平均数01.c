#include <stdio.h>

int main()
{
	double sum = 0;
	int num;
	int count = 0;
	int number[100]; 
	
	printf("输入一个整数，以-1结束：");
	scanf("%d", &num);
	while (num != -1)
	{
		number[count] = num;
		count ++;
		sum += num;
		printf("输入一个整数，以-1结束：");
		scanf("%d", &num);
	} 
	if (count > 0)
	{
		double average = sum/count;
		printf("这%d个数的平均数为%f\n", count, average);
		int i;
		for ( i=0; i<count; i++)
		{
			if ( number[i] > average )
			{
				printf("%d\n", number[i]);
			}
		}
	}
	
	return 0;
}
