#include <stdio.h> 

enum color { red, yellow, green }; 

void f(enum color c)
{
	printf("%d\n", c);
}

int main()
{
	enum color t = red;
	enum color s;
	scanf("%d", &s);
	f(t);
	f(s);
	
	return 0;
} 

