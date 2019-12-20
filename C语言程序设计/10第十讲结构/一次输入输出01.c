#include <stdio.h> 

struct point
{
	int x;
	int y;
};
struct point getStruct(struct point p)
{
	scanf("%i %i", &p.x, &p.y);
	return p;
}
void outPut(struct point p)
{
	printf("%i-%i", p.x, p.y);
}
int main(int argc, char const *argv[])
{
	struct point q = {0,0};
	q = getStruct(q);
	outPut(q);
	
	return 0;
} 


