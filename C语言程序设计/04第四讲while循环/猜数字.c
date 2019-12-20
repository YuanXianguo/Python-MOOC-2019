#include <stdio.h>
#include <stdlib.h>
#include <time.h> 

int main()
{
	srand(time(0));
	int a = rand()%100+1;
	int count = 0;
	int num = 0;
	printf("我已经想好了一个1到100之间的数字。");
	do
	{
		printf("猜猜我心里的数字：");
		scanf("%d", &num);
		count ++;
		if (num < a)
		{
			printf("猜错了！你猜的数字小了！");
		}	
		else if (num > a) 
		{
			printf("猜错了！你猜的数字大了！");
		}	 
	}
	while (num != a);
	printf("猜对了！你一共猜了%d次\n", count);
	
	return 0;
}
