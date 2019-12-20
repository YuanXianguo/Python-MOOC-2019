#include <stdio.h> 

#define PI 3.14159
#define FORMAT "%f\n"
#define PI2 2*PI // pi*2 
#define PRT printf("%f ", PI);\
			printf("%f\n", PI2) 
			
int main(int argc, char const *argv[])
{
	PRT;
	printf(FORMAT, PI2*3.0);
	
	return 0;
} 


