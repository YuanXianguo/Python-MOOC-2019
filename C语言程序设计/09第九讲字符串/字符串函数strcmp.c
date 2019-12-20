#include <stdio.h>
#include <string.h>

int mycmp(const char *s1, const char *s2)
{
	while ( *s1 == *s2 && *s1 != '\0')
	{
		s1 ++;
		s2 ++;
	}
	return *s1 - *s2;
}
int main()
{
	char s1[] = "abca";
	char s2[] = "abc";
	printf("strcmp=%d\n", strcmp(s1,s2));
	printf("mycmp =%d\n", mycmp(s1,s2));
	
	return 0;
}


