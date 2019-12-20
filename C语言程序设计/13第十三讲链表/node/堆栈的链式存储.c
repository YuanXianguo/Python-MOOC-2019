typedef struct SNode_ {
	ElementType Data;
	struct SNode *Next; 
} SNode;

SNode *Stack;
Stack S;

//��ջ��ʼ��
Stack CreateStack()
{	//����һ����ջ��ͷ��㣬����ָ�� 
	Stack S;
	S = (Stack)malloc(sizeof(SNode));
	S->Next = NULL;
	return S; 
} 

//�ж϶�ջS�Ƿ�Ϊ��
int IsEmpty(Stack S)
{	//��Ϊ�շ���1������0 
	return ( S->Next == NULL );
} 

//��ջ
void Push(Stack S, ElementType item)
{
	struct SNode *TmpCell;
	TmpCell = (Stack)malloc(sizeof(SNode));
	TmpCell->Data = item;
	TmpCell->Next = S->Next;
	S->Next = TmpCell;
} 

//��ջ
ElementType Pop(Stack S)
{
	struct SNode *FirstCell;
	ElementType TopItem;
	if ( IsEmpty(S) )
	{
		printf("��ջ��");
		return NULL;
	}
	else
	{
		FirstCell = S->Next;
		S->Next = FirstCell->Next;
		TopItem = FirstCell->Data;
		free(FirstCell); 
		return TopItem;
	} 	
} 
