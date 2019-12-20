#include <stdio.h> 

struct point
{
	int x;
	int y;
};

struct point *getStruct(struct point *p)
{
	scanf("%d %d", &p->x, &p->y);//指针方式输入成员 
	return p; //返回指针 
}

void outPut(struct point p)
{
	printf("%d-%d\n", p.x, p.y);//结构体方式输出 
}

void print(const struct point *p) 
{
	printf("%d-%d\n", p->x, p->y);//指针方式输出 
}

int main(int argc, char const *argv[])
{
	struct point q = {0,0};
	getStruct(&q)->x = 1;//传入结构体指针,指针方式修改成员 
	outPut(q);//调用修改后结构体,并输出 
	
	*getStruct(&q) = (struct point){2,2};
	//传入结构体指针,结构体方式修改成员 
	print(&q);//调用修改后结构体指针,并输出 
	
	outPut(*getStruct(&q));//传入结构体指针,并输出 
	print(getStruct(&q));//传入结构体指针,并输出 
	
	return 0;
} 


