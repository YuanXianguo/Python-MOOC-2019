#include <stdio.h>

void f(int *p)
{
	printf("p=%p\n", p);
	printf("*p=%d\n", *p); 
	*p = 26;
}
int main()
{
	int i = 6;
	printf("i=%p\n", &i);
	f(&i);
	printf("ÏÖÔÚi=%d\n", i);
	
	return 0;
} 
 
 
