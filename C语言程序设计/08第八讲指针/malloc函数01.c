#include <stdio.h>
#include <stdlib.h>

int main()
{
	int number;
	int *a;
	int i;
	printf("����������");
	scanf("%d", &number);
	// int a[number]; C99 
	//����һ���СΪnumber*sizeof(int)���ڴ� 
	a = (int*)malloc(number*sizeof(int)); 
	for ( i=0; i<number; i++ )
	{
		scanf("%d", &a[i]);
	}
	for ( i=0; i<number; i++ )
	{
		printf("%d", a[i]);
	}
	free(a); //�ͷ��ڴ� 
	
	return 0;
} 

