#include <stdio.h>
#include <string.h>

size_t mylen(const char *s)
{
	int idx = 0;
	while ( s[idx] != '\0' )
	{
		idx ++;
	}
	return idx;
}
int main()
{
	char s[] = "hello";
	printf("strlen=%d\n", strlen(s));
	printf("mylen =%d\n", mylen(s));
	
	return 0;
}


