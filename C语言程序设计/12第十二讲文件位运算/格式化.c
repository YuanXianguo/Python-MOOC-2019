#include <stdio.h> 

int main(int argc, char const *argv[])
{
	printf("9λ�����Ҷ���:%9d\n", 123);
	printf("9λ�Ӻ������:%-+9d\n", 123);
	printf(" Ĭ����λС��:%f\n", 123.0);
	printf(" ��9λ2λС��:%9.2f\n", 123.0);
	printf(" ��9λ��λ��0:%09.2f\n", 123.0); 
	printf("%hhd\n", (char)12345); 
	
	return 0;
} 


