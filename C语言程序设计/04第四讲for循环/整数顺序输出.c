#include <stdio.h>

int main()
{
	int num;
	scanf("%d", &num);
	int t = num;
	int mask = 1;
	//����λ����mask; 
	while ( num>9 )
	{
		num /= 10;
		mask *= 10;
	}
	//�����λ��ʼ����� 
	do
	{
		int s = t / mask;
		printf("%d", s);
		if (mask > 9)
		{
			printf(" ");
		}
		t %= mask; //��tȥ�����λ�󸳸�t�� 
		mask /= 10;
	 } 
	 while ( mask > 0);
	 printf("\n");

	return 0;
 } 
