#include <stdio.h>

int main()
{
	int a,b;
	scanf("%d %d", &a, &b);
	int x=a, y=b;
	int t;
	while (b!=0)
	{
		t = a % b;
		a = b;
		b = t;
	} 
	printf("%d��%d�����Լ����%d", x, y, a);
	
	return 0;
 } 
