#include <stdio.h> 

int main(int argc, char const *argv[])
{
	FILE *fp = fopen("file", "r");
	if ( fp )
	{
		int num;
		fscanf(fp, "%d", &num);
		printf("%d\n", num);
		fclose(fp);
	}
	else 
	{
		printf("无法打开文件\n");
	}
	
	return 0;
} 


