#동적스택, 큐 개념 -> 1. 구조체에 선언할때 포인터변수 배열을 만든다, 2. init함수에서 1칸짜리 배열로 malloc한다, 3. push했는데 is_full이 1이면 realloc으로 확장한다, 4. capacity가 꼭 필요하다 '현재 칸개수'
#include <stdio.h>
#include <stdlib.h>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

typedef int element;
typedef struct stack{
	element *data;
	int top;
	int capacity;
}Stack;

void init(Stack *s){
	
	s->top = -1;
	s->capacity = 1;
	s->data = (element*)malloc(s->capacity*sizeof(element));
}

int is_empty(Stack *s){
	return s->top == -1;
}
int is_full(Stack* s){
	return s->capacity == s->top-1;
}

void push(Stack *s, int item){
	
	if(is_full(s)){
		s->capacity*=2;
		s->data = (element*)realloc(s->data, s->capacity*sizeof(element));
	}
	s->data[++(s->top)] = item;
}

element pop(Stack *s){
	
	if(is_empty(s)){
		fprintf(stderr, "스택 공백 에러\n");
		exit(1);
	}	
	else return s->data[(s->top)--];
}

int main(void){
	
	Stack s;
	init(&s);
	push(&s, 1);
	push(&s, 2);
	push(&s, 3);
	
	printf("%d\n",pop(&s));
	printf("%d\n",pop(&s));
	printf("%d\n",pop(&s));
	
	free(&s);
}
