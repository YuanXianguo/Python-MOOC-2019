{
	int *const q = &i; //q «const;
	*q = 26; //OK; 
	q++; //ERROR!
} 
	
{
	const int *p = &i; <==> int const *p = &i;
	*p = 26; //ERROR! (*p) «const;
	i = 26; //OK;
	p = &j; //OK;
}

{	
	void f(const int *x);
	int a = 15; 
	f(&a); //OK;
	const int b = a; 
	f(&b); //OK;
	b = a + 1; //ERROR!
}


{
	char ac[] = {0,1,2,3,4,5,6,7,8,9,-1,};
	char *p = ac;
	for ( p=ac; *p!=-1; p++ )
	{
		printf("%d\n", *p);
	}
}

{
	char ac[] = {0,1,2,3,4,5,6,7,8,9,-1,};
	char *p = ac;
	while ( *p != -1 )
	{
		printf("%d\n", *p++);
	}
}




