#include <stdio.h> 

struct point
{
	int x;
	int y;
};

struct point *getStruct(struct point *p)
{
	scanf("%d %d", &p->x, &p->y);//ָ�뷽ʽ�����Ա 
	return p; //����ָ�� 
}

void outPut(struct point p)
{
	printf("%d-%d\n", p.x, p.y);//�ṹ�巽ʽ��� 
}

void print(const struct point *p) 
{
	printf("%d-%d\n", p->x, p->y);//ָ�뷽ʽ��� 
}

int main(int argc, char const *argv[])
{
	struct point q = {0,0};
	getStruct(&q)->x = 1;//����ṹ��ָ��,ָ�뷽ʽ�޸ĳ�Ա 
	outPut(q);//�����޸ĺ�ṹ��,����� 
	
	*getStruct(&q) = (struct point){2,2};
	//����ṹ��ָ��,�ṹ�巽ʽ�޸ĳ�Ա 
	print(&q);//�����޸ĺ�ṹ��ָ��,����� 
	
	outPut(*getStruct(&q));//����ṹ��ָ��,����� 
	print(getStruct(&q));//����ṹ��ָ��,����� 
	
	return 0;
} 


