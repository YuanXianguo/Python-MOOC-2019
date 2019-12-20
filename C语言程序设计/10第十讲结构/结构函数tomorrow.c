#include <stdio.h>
#include <stdbool.h> 

struct date
{
	int month;
	int day;
	int year;
};

bool isLeap(struct date d)
{
	bool leap = false;

	if ((d.year % 4 == 0 && d.year % 100 != 0) || d.year % 400 == 0)
	{
		leap = true;
	}
	return leap;
}

int numberOfDays(struct date day)
{
	int days;

	const int daysPerMonth[12] = { 31,28,31,30,31,30,31,31,30,31,30,31 };

	if ( day.month == 2 && isLeap(day) )
	{
		days = 29;
	}
	else 
	{
		days = daysPerMonth[day.month-1];
	}
	return days;	
}

int main(int argc, char const *argv[])
{
	struct date today, tomorrow;
	
	printf("请输入今天的日期：");
	scanf("%i %i %i", &today.year, &today.month, &today.day);
	
	if ( today.day != numberOfDays(today) )
	{
		tomorrow.day = today.day + 1;
		tomorrow.month = today.month;
		tomorrow.year = today.year;
	} 
	else if ( today.month == 12 )
	{
		tomorrow.day = 1;
		tomorrow.month = 1;
		tomorrow.year = today.year + 1;
	}
	else
	{
		tomorrow.day = 1;
		tomorrow.month = today.month + 1;
		tomorrow.year = today.year;
	}
	printf("明天的日期是：%i %i %i\n", tomorrow.year, tomorrow.month, tomorrow.day);

    return 0;
}


