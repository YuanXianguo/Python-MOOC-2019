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

����б���:
struct rectangle r;
�Ϳ�����:
r.pt1.x, r.pt1.y;
r.pt2.x, r.pt2.y;

����б���:
struct rectangle r, *rp;
rp = &r;
��ô�����������ʽ�ǵȼ۵�:
r.pt1.x;
rp->pt1.x;
(r.pt1).x;
(rp->pt1).x; 
����û��rp->pt1->x (��Ϊpt1����ָ��)



