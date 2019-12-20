#include <stdio.h> 
#include <stdlib.h> 
#include "node.h" 

typedef struct _list {
	Node *head;
} List;

void add(List *plist, int number);
void print(List *pList);
void find(List *pList, int number);
void del(List *pList, int number);
void clear(List *pList);

int main(int argc, char const *argv[])
{
	List list;
	list.head = NULL;
	int number;
	do
	{
		scanf("%d", &number);
		if ( number != -1 )
		{
			add(&list, number);
		}
	}
	while ( number != -1 );
	print(&list);
	scanf("%d", &number);
	find(&list, number);
	del(&list, number);
	print(&list);
	
	return 0;
} 

void add(List *pList, int number)
{
	// 将新数据设置成新的终止结点 
	Node *p = (Node*)malloc(sizeof(Node));
	p->value = number;
	p->next = NULL;
	//找原来的终止结点 
	Node *last = pList->head;//初始化终止结点为head 
	if ( last )
	{
		while ( last->next )
		{
			last = last->next;
		}
		last->next = p; //找到终止结点 
	}
	else //last为空，即head为空，一个结点也没有 
	{
		pList->head = p;
	} 
}

void print(List *pList)
{
	Node *p;
	for ( p=pList->head; p; p=p->next)
	{
		printf("%d\t", p->value);
	}
	printf("\n");
} 

void find(List *pList, int number)
{
	Node *p;
	int isFound = 0;
	for ( p=pList->head; p; p=p->next)
	{
		if ( p->value == number)
		{
			printf("找到了\n");
			isFound = 1;
			break;
		}
	}
	if ( !isFound )
	{
		printf("没找到\n");
	}
}

void del(List *pList, int number)
{
	Node *p, *q;
	for ( q=NULL,p=pList->head; p; q=p,p=p->next)
	{
		if ( p->value == number)
		{
			if ( q )
			{
				q->next = p->next;
			}
			else
			{
				pList->head = p->next;
			}
			free(p);
			break;
		}
	}
}

void clear(List *pList)
{
	Node *p, *q;
	for ( p=pList->head; p; p=q)
	{
		q = p->next;
		free(p);
	}
}
