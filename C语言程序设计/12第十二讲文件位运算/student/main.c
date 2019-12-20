#include <stdio.h>
#include "student.h"

void getList(Student aStu[], int number);
int save(Student aStu[], int number);

int main(int argc, char *argv[]) 
{
	int number = 0;
	printf("����ѧ��������");
	scanf("%d", &number);
	Student aStu[number];
	
	getList(aStu, number);
	if ( save(aStu, number) )
	{
		printf("����ɹ�\n");
	}
	else
	{
		printf("����ʧ��\n");
	}
	
	return 0;
}

void getList(Student aStu[], int number)
{
	char format[STR_LEN];
	sprintf(format, "%%%ds", STR_LEN-1); //"%19s"
	
	int i;
	for ( i=0; i<number; i++ )
	{
		printf("��%d��ѧ����\n", i);
		printf("\t������");
		scanf(format, aStu[i].name);
		printf("\t�Ա�0-�У�1-Ů��2-��������");
		scanf("%d", &aStu[i].gender);
		printf("\t���䣺");
		scanf("%d", &aStu[i].age);
	}
}

int save(Student aStu[], int number)
{
	int ret = -1;
	FILE *fp = fopen("student.data", "w");
	if ( fp )
	{
		ret = fwrite(aStu, sizeof(Student), number, fp);
		fclose(fp);
	}
	return ret == number;
}

