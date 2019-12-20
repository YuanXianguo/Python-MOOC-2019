#include <stdio.h> 

int main(int argc, char const *argv[])
{
	printf("9位正常右对齐:%9d\n", 123);
	printf("9位加号左对齐:%-+9d\n", 123);
	printf(" 默认六位小数:%f\n", 123.0);
	printf(" 共9位2位小数:%9.2f\n", 123.0);
	printf(" 共9位空位补0:%09.2f\n", 123.0); 
	printf("%hhd\n", (char)12345); 
	
	return 0;
} 


