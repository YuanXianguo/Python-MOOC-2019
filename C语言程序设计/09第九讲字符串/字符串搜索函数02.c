#include <stdio.h>
#include <string.h>
#include <stdlib.h> 

int main()
{
	char s[] = "hello";
	char *p = strchr(s, 'l'); 
	char c = *p;//将指针所指赋给c 
	printf("%c\n", c);
	*p = '\0';//将指针赋值为'0' 
	char *t = (char*)malloc(strlen(s)+1);
	strcpy(t, s);//将构造的字符串复制到t 
	printf("%s\n", t);
	*p = c; 
	printf("%s", s);
	free(t);
	
	return 0;
}

 
