#include <stdio.h>

int main()
{
	double sum = 0;
	int num;
	int count = 0;
	int number[100]; 
	
	printf("����һ����������-1������");
	scanf("%d", &num);
	while (num != -1)
	{
		number[count] = num;
		count ++;
		sum += num;
		printf("����һ����������-1������");
		scanf("%d", &num);
	} 
	if (count > 0)
	{
		double average = sum/count;
		printf("��%d������ƽ����Ϊ%f\n", count, average);
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
