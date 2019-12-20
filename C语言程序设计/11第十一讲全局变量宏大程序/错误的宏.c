#include <stdio.h> 

#define RADTIDEF(x) ((x)*57.29578)
#define RADTIDEF1(x) (x*57.29578) 
#define RADTIDEF2(x) (x)*57.29578
 
int main(int argc, char const *argv[])
{
	printf("RADTIDEF(5+2) =%f\n", RADTIDEF(5+2));
	printf("RADTIDEF1(5+2)=%f\n", RADTIDEF1(5+2));
	printf("180/RADTIDEF(1) =%f\n", 180/RADTIDEF(1));
	printf("180/RADTIDEF2(1)=%f\n", 180/RADTIDEF2(1));
	
	return 0;
} 


