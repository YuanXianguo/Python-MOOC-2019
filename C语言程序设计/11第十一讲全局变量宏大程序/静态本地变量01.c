#include <stdio.h> 

int gAll = 12;
int main(int argc, char const *argv[])
{
	static int all = 0;
	int i = 0;
	printf("gAll=%p\n", &gAll);
	printf(" all=%p\n", &all);
	printf("   i=%p\n", &i);
	
	return 0;
} 


