#include <stdio.h>

int main()
{
	char a[][10] = {"Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"};
	int i;
	scanf("%d", &i);
	printf("%s", a[i]);
	
	return 0;
}


