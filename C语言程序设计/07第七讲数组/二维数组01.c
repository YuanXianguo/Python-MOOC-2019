#include <stdio.h>


int main()
{
	const int size = 3;
	int board[size][size];
	int i,j;
	int numofX;
	int numofO;
	int result = -1;
	
	//输入1代表X，0代表O； 
	//result==-1:没人赢，1：X赢，0：O赢；
	
	//读入矩阵
	for ( i=0; i<size; i++ )
	{
		for ( j=0; j<size; j++)
		{
			scanf("%d", &board[i][j]);
		}
	} 
	
	//检查行 
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

	//检查列 
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

	//检查正对角
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
	
	//检查副对角
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
		printf("X赢\n");
	}
	else if ( result == 0 )
	{
		printf("O赢\n");
	}
	else 
	{
		printf("没人赢\n"); 
	}
	
	return 0;
 } 
