#include <stdio.h>

int main()
{
	int n;
	scanf("%d", &n);
	int fact = 1;
	int i=1;
	for ( ; i<=n; i++ )
	{
		fact *= i;
	}
	printf("%d!=%d", n, fact);
	
	return 0;
}
