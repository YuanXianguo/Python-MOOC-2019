#include <stdio.h>
#include <stdlib.h>
#include <time.h> 

int main()
{
	srand(time(0));
	int a = rand()%100+1;
	printf("%d", a); 
	
	return 0;
}
