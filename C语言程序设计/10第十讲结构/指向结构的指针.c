#include <stdio.h> 

struct date
{
	int month;
	int day;
	int year;
} myday;

struct date *p = &myday;

(*p).month = 12; //����1 
p->month = 12; //����2���Ƽ� 


