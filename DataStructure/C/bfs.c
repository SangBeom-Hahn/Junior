#include<stdio.h>
#include<stdlib.h>
#define MAX_V 50

typedef struct graphNode {
	
	int vertax;
	struct GraphNode* link;
}GraphNode;

typedef struct graphType {

	int n;
	GraphNode* mat[MAX_V];
}GraghType;

void init(GraghType* g) {

	g->n = 0;
	for (int j = 0; j < MAX_V; j++)
		g->mat[j] = NULL;
}

void insert_v(GraghType* g) {

	g->n++;
}

void insert_e(GraghType* g, int v, int u) {

	GraphNode *node = (GraphNode*)malloc(sizeof(GraphNode));

	node->vertax = u;
	node->link = g->mat[v];
	g->mat[v] = node;
}

void print(GraghType* g) {

	for (int i = 0; i < g->n; i++) {
		GraphNode* p = g->mat[i];
		printf("정점 %d의 인접 리스트", i);
		while (p != NULL) {
			printf("->%d", p->vertax);
			p = p->link;
		}
		printf("\n");
	}
}

int visited[MAX_V];
void bfs(GraghType* g, int v) {
	
	Queue q;
	GraphNode* w;
	visited[v] = 1;
	//enque(*q, v);
	while (!is_empty) {
		v = deque();
		for (w = g->mat[v]; w ; w = w->link) {
			if (!visited[w->vertax]) {
				visited[w->vertax] = 1;
	//			enque(*q, w->vertax);
			}
		}
	}
}