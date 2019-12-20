#include <stdio.h> 

int main(int argc, char const *argv[])
{
	int number;
	scanf("%x", &number);
	unsigned mask = 1u<<31;
	printf("%d", mask& mask?1:0);
	printf("\n");
	for ( ; mask; mask >>= 1 )
	{
		printf("%d", number & mask?1:0);
	}
	printf("\n");
	
	return 0;
} 


