#include <stdio.h>

int main()
{
	int a[10] = {
		[0] = 2, [2] = 3, 6,
	};
	int i;
	for ( i=0; i<10; i++ )
	{
		printf("%d ", a[i]);
	}
	
	return 0;
}


