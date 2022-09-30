#include<stdio.h>
#define Max(a,b) ((a)>(b) ? a:b)
#define Max_degree 101

typedef struct sik {
	int degree;
	float coef[Max_degree];
}poly;

int main(void) {

	poly a = { 5,{10,0,0,0,6,3} };
	poly b = { 4,{1,0,5,0,7} };
	poly c;
	c.degree = Max(a.degree, b.degree);

	int Apos = 0, Bpos = 0, Cpos = 0;

	for (int j = 0; j <= b.degree; j++) {

		c.coef[Cpos] = a.coef[Apos] + b.coef[Bpos];

		Apos++;
		Bpos++;
		Cpos++;
		
	}

	while (Apos <= a.degree) {
		c.coef[Cpos] = a.coef[Apos];
		Apos++;
		Cpos++;
	}

	for (int i = c.degree; i > 0; i--) {
		printf("%3.1lfx^%d +", c.coef[i], i);
	}
	printf("%3.1lf", c.coef[0]);


}