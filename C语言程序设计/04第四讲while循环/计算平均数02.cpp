#include <stdio.h>

int main()
{
	int sum = 0;
	int num;
	int count = 0;
	
	printf("输入一个整数，以-1结束：");
	scanf("%d", &num);
	while (num != -1)
	{
		count ++;
		sum += num;
		printf("输入一个整数，以-1结束：");
		scanf("%d", &num);
	} 
	
	printf("这%d个数的平均数为%d", count, sum/count);
	
	return 0;
}
