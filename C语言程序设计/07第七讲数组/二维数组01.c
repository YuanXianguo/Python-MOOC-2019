#include <stdio.h>


int main()
{
	const int size = 3;
	int board[size][size];
	int i,j;
	int numofX;
	int numofO;
	int result = -1;
	
	//����1����X��0����O�� 
	//result==-1:û��Ӯ��1��XӮ��0��OӮ��
	
	//�������
	for ( i=0; i<size; i++ )
	{
		for ( j=0; j<size; j++)
		{
			scanf("%d", &board[i][j]);
		}
	} 
	
	//����� 
	for ( i=0; i<size && result == -1; i++ )
	{
		numofX = numofO = 0;
		for ( j=0; j<size; j++ )
		{
			if ( board[i][j] == 1 )
			{
				numofX ++;
			}
			else
			{
				numofO ++;
			}
		}
		if ( numofX == size )
		{
			result = 1;
		}
		else if ( numofO == size )
		{
			result = 0;
		}
	} 

	//����� 
	if ( result == -1 )
	{
		for ( j=0; j<size && result == -1; j++ )
		{
			numofX = numofO = 0;
			for ( i=0; i<size; i++ )
			{
				if ( board[i][j] == 1 )
				{
					numofX ++;
				}
				else
				{
					numofO ++;
				}
			}
			if ( numofX ==size )
			{
				result = 1;
			}
			else if ( numofO == size )
			{
				result = 0;
			}
		} 
	}

	//������Խ�
	if ( result == -1 )
	{
		numofX = numofO = 0;
		for ( i=0; i<size; i++ )
		{
			if ( board[i][i] == 1 )
			{
				numofX ++;
			}
			else
			{
				numofO ++;
			}
		}
		if ( numofX == size )
		{
			result = 1;
		}
		else if ( numofO == size )
		{
			result = 0;
		}
	}
	
	//��鸱�Խ�
	if ( result == -1 )
	{
		numofX = numofO = 0;
		for ( i=0; i<size; i++ )
		{
			if ( board[i][size-1-i] == 1 )
			{
				numofX ++;
			}
			else
			{
				numofO ++;
			}
		}
		if ( numofX ==size )
		{
			result = 1;
		}
		else if ( numofO == size )
		{
			result = 0;
		}
	}
	 
	if ( result == 1 )
	{
		printf("XӮ\n");
	}
	else if ( result == 0 )
	{
		printf("OӮ\n");
	}
	else 
	{
		printf("û��Ӯ\n"); 
	}
	
	return 0;
 } 
