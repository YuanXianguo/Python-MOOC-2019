#include <stdio.h>

int main()
{
	int num;
	scanf("%d", &num);
	int t = num;
	int mask = 1;
	//计算位数及mask; 
	while ( num>9 )
	{
		num /= 10;
		mask *= 10;
	}
	//从最高位开始输出； 
	do
	{
		int s = t / mask;
		printf("%d", s);
		if (mask > 9)
		{
			printf(" ");
		}
		t %= mask; //将t去掉最高位后赋给t； 
		mask /= 10;
	 } 
	 while ( mask > 0);
	 printf("\n");

	return 0;
 } 
