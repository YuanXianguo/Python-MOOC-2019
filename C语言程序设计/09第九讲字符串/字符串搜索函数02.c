#include <stdio.h>
#include <string.h>
#include <stdlib.h> 

int main()
{
	char s[] = "hello";
	char *p = strchr(s, 'l'); 
	char c = *p;//��ָ����ָ����c 
	printf("%c\n", c);
	*p = '\0';//��ָ�븳ֵΪ'0' 
	char *t = (char*)malloc(strlen(s)+1);
	strcpy(t, s);//��������ַ������Ƶ�t 
	printf("%s\n", t);
	*p = c; 
	printf("%s", s);
	free(t);
	
	return 0;
}

 
