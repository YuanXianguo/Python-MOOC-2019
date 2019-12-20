#include <stdio.h>
#include <string.h>

size_t mylen(const char *s)
{
	char *s0 = s;
	while ( *s != '\0' )
	{
		s ++;
	}
	return s - s0;
}
int main()
{
	char s[] = "hello";
	printf("strlen=%d\n", strlen(s));
	printf("mylen =%d\n", mylen(s));
	
	return 0;
}


