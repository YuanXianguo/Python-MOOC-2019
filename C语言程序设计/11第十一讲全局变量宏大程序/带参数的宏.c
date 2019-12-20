#include <stdio.h> 

#define cube(x) ((x)*(x)*(x)) 
int main(int argc, char const *argv[])
{
	int i = 0; 
	printf("%d\n", cube(5));
	printf("%d\n", cube(i+2));
	
	return 0;
} 


