#include <stdio.h>

int main()
{
	int sum = 0;
	int num;
	int count = 0;
	do
	{
		printf("����һ����������-1������");
		scanf("%d", &num);
		if (num != -1)
		{
			count ++;
			sum += num;
		}	
	 } 
	while(num != -1);
	printf("��%d������ƽ����Ϊ%d", count, sum/count);
	
	return 0;
}
