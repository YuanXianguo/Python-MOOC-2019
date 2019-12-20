#include <stdio.h>
#include <stdlib.h>

int main()
{
	int number;
	int *a;
	int i;
	printf("输入数量：");
	scanf("%d", &number);
	// int a[number]; C99 
	//开辟一块大小为number*sizeof(int)的内存 
	a = (int*)malloc(number*sizeof(int)); 
	for ( i=0; i<number; i++ )
	{
		scanf("%d", &a[i]);
	}
	for ( i=0; i<number; i++ )
	{
		printf("%d", a[i]);
	}
	free(a); //释放内存 
	
	return 0;
} 

