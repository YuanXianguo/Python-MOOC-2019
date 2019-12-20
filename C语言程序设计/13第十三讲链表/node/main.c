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
	// �����������ó��µ���ֹ��� 
	Node *p = (Node*)malloc(sizeof(Node));
	p->value = number;
	p->next = NULL;
	//��ԭ������ֹ��� 
	Node *last = pList->head;//��ʼ����ֹ���Ϊhead 
	if ( last )
	{
		while ( last->next )
		{
			last = last->next;
		}
		last->next = p; //�ҵ���ֹ��� 
	}
	else //lastΪ�գ���headΪ�գ�һ�����Ҳû�� 
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
			printf("�ҵ���\n");
			isFound = 1;
			break;
		}
	}
	if ( !isFound )
	{
		printf("û�ҵ�\n");
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
