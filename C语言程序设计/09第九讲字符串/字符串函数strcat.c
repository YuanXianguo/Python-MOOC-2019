#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void mycat(char *dst, const char *src)
{
	dst += strlen(dst);
	while ( *dst ++ = *src ++ );
}
int main()
{
	char src[] = "World";
	char dst[] = "Hello";
	char dst2[] = "Hello";
	strcat(dst, src);
	mycat(dst2, src);
	printf("strcat=%s\n", dst);
	printf("mycat =%s\n", dst2);
	
	return 0;
}



