#include <stdio.h>
#include <stdlib.h>
#include <time.h> 

int main()
{
	srand(time(0));
	int a = rand()%100+1;
	int count = 0;
	int num = 0;
	printf("���Ѿ������һ��1��100֮������֡�");
	do
	{
		printf("�²�����������֣�");
		scanf("%d", &num);
		count ++;
		if (num < a)
		{
			printf("�´��ˣ���µ�����С�ˣ�");
		}	
		else if (num > a) 
		{
			printf("�´��ˣ���µ����ִ��ˣ�");
		}	 
	}
	while (num != a);
	printf("�¶��ˣ���һ������%d��\n", count);
	
	return 0;
}
