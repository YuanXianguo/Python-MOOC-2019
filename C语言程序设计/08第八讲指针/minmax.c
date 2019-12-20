#include <stdio.h>

void minmax(int a[], int len, int *min, int *max)
{
	*min = *max = a[0];
	int i;
	for ( i=0; i<len; i++ )
	{
		if ( a[i] < *min )
		{
			*min = a[i];
		} 
		if ( a[i] > *max )
		{
			*max = a[i];
		}
	}
}	
int main()
{
	int a[] = {1,2,3,5,7,9,11,14,15,25};
	int min,max;
	minmax(a, sizeof(a)/sizeof(a[0]), &min, &max);
	printf("min=%d\tmax=%d\n", min, max);
	
	return 0;
}


