#include <stdio.h>

int main()
{
	int sum = 0;
	int num;
	int count = 0;
	
	printf("����һ����������-1������");
	scanf("%d", &num);
	while (num != -1)
	{
		count ++;
		sum += num;
		printf("����һ����������-1������");
		scanf("%d", &num);
	} 
	
	printf("��%d������ƽ����Ϊ%d", count, sum/count);
	
	return 0;
}
