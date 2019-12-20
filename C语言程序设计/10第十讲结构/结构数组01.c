#include <stdio.h> 

struct date 
{
	int month;
	int day;
	int year;
};

int main(int argc, char const *argv[])
{
	struct date dates[2] = {
		{9,20,2018},
		{9,21,2018}
	};
	int i;
	for ( i=0; i<2; i++ )
	{
		printf("Date is %i-%i-%i.\n",
			dates[i].year, dates[i].month, dates[i].day);
	}
	
	return 0;
} 


