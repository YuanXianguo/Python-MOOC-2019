#include <stdio.h>
#include <string.h>

int mycmp(const char *s1, const char *s2)
{
	int idx = 0;
	while ( s1[idx] == s2[idx] && s1[idx] != '\0')
	{
		idx ++;
	}
	return s1[idx] - s2[idx];
}
int main()
{
	char s1[] = "abca";
	char s2[] = "abc";
	printf("strcmp=%d\n", strcmp(s1,s2));
	printf("mycmp =%d\n", mycmp(s1,s2));
	
	return 0;
}




