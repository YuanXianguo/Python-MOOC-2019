#include <stdio.h> 

int main(int argc, char const *argv[])
{
	int num;
	int i1 = scanf("%i", &num);
	int i2 = printf("%d\n", num);
	printf("%d:%d", i1,i2);
	
	return 0;
} 


