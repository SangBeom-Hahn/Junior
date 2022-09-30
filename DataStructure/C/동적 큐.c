#include <stdio.h>
#include <stdlib.h>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

typedef int element;
typedef struct queue{
	element *data;
	int rear, front;
	int capacity;
}Queue;

void init(Queue *s){
	
	s->rear = -1, s->front = -1;
	s->capacity = 1;
	s->data = (element*)malloc(s->capacity*sizeof(element));
}

int is_empty(Queue *s){
	return s->rear == s->front;
}
int is_full(Queue* s){
	return s->rear == s->capacity-1;
}

void push(Queue *s, int item){
	
	if(is_full(s)){
		s->capacity*=2;
		s->data = (element*)realloc(s->data, s->capacity*sizeof(element));
	}
	s->data[++(s->rear)] = item;
}

element pop(Queue *s){
	
	if(is_empty(s)){
		fprintf(stderr, "스택 공백 에러\n");
		exit(1);
	}	
	else return s->data[++(s->front)];
}

int capacity(Queue *s){
	return s->capacity;
}

int main(void){
	
	Queue q;
	init(&q);
	push(&q, 1);
	push(&q, 2);
	push(&q, 3);
	push(&q, 3);
	push(&q, 3);
	push(&q, 3);
	push(&q, 3);
	push(&q, 3);
	push(&q, 3);
	push(&q, 3);
	
	
	printf("%d\n",pop(&q));
	printf("%d\n",pop(&q));
	printf("%d\n",pop(&q));
	printf("%d",capacity(&q));
	free(&q);
}
