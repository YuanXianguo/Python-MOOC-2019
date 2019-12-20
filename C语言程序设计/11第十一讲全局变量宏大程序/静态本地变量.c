#include <stdio.h> 

int f(void)
{
	static int all = 0;
	printf("in %s all=%d\n", __func__, all);
	all += 2;
	printf("agn in %s all=%d\n", __func__, all);
	return all;
} 
int main(int argc, char const *argv[])
{
	f();
	f();
	
	return 0;
} 


