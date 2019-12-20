#include <stdio.h>
#include "readstudent.h"

void read(FILE *fp, int index);

int main(int argc, char *argv[]) 
{
	FILE *fp = fopen("E:/C/C/��ʮ�����ļ�λ����/student/student.data", "r");
	if ( fp )
	{
		fseek(fp, 0L, SEEK_END);//ָ���Ƶ���� 
		long size = ftell(fp);//��ȡָ�뵱ǰλ�ã����ļ���С 
		int number = size / sizeof(Student);
		int index = 0;
		printf("��%d�����ݣ���Ҫ���ڼ�����", number);
		scanf("%d", &index);
		read(fp, index-1);
		fclose(fp);
	}
	else printf("ʧ��"); 
	
	return 0;
}

void read(FILE *fp, int index)
{
	fseek(fp, index*sizeof(Student), SEEK_SET);
	Student stu;
	if ( fread(&stu, sizeof(Student), 1, fp) == 1 )
	{
		printf("��%d��ѧ����", index+1);
		printf("\n\t������%s\n", stu.name);
		printf("\t�Ա�");
		switch( stu.gender )
		{
			case 0:printf("��\n"); break;
			case 1:printf("Ů\n"); break;
			case 2:printf("����\n"); break;
		}
		printf("\t���䣺%d\n", stu.age);
	}
}


