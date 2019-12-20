#include <stdio.h> 

int main(int argc, char const *argv[])
{
	int a = 0x80000000;
	unsigned int b = 0x80000000;
	printf("a=%d\n", a);
	printf("b=%u\n", b);
	printf("a>>1=%d\n", a>>1);
	printf("b>>1=%d\n", b>>1);
	
	return 0;
} 


