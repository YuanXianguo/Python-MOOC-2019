#ifndef __LIST_HEAD__
#define __LIST_HEAD__

#include "node.h"

typedef struct _list {
	Node *head;
	Node *tail;
} List;

#endif


