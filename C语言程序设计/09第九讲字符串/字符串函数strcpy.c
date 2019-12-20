#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void mycpy(char *dst, const char *src)
{
	while ( *dst ++ = *src ++ );
}
int main()
{
	char src[] = "abc";
	char *dst = (char*)malloc(strlen(src)+1);
	char *dst2 = (char*)malloc(strlen(src)+1);
	strcpy(dst, src);
	mycpy(dst2, src);
	printf("strcpy=%s\n", dst);
	printf("mycpy =%s\n", dst2);
	free(dst);
	free(dst2);
	
	return 0;
}


