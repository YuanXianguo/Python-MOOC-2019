struct point
{
	int x;
	int y;
}; 
struct rectangle
{
	struct point pt1;
	struct point pt2;
};

如果有变量:
struct rectangle r;
就可以有:
r.pt1.x, r.pt1.y;
r.pt2.x, r.pt2.y;

如果有变量:
struct rectangle r, *rp;
rp = &r;
那么下面的四种形式是等价的:
r.pt1.x;
rp->pt1.x;
(r.pt1).x;
(rp->pt1).x; 
但是没有rp->pt1->x (因为pt1不是指针)



