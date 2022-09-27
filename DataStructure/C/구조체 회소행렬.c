#include<stdio.h>

typedef struct {
    int M2[7][3];
    int rows;
    int cols;
    int terms;
}entire;

int main(void) {

    entire result;
    entire first = {
        {{0,3,7},
        {1,0,9},
        {1,5,8},
        {3,0,6},
        {3,1,5},
        {4,5,1},
        {5,2,2}},
        6,
        6,
        7
    };

    int bindex;
    result.rows = first.rows;
    result.cols = first.cols;
    result.terms = first.terms;
    
    if (first.terms > 0) {
        bindex = 0;
        for (int c = 0; c < first.cols; c++) {
            for (int i = 0; i < first.terms; i++) {
                if (first.M2[i][1] == c) {
                    result.M2[bindex][0] = first.M2[i][1];
                    result.M2[bindex][1] = first.M2[i][0];
                    result.M2[bindex][2] = first.M2[i][2];
                    bindex++;
                }
            }
        }
    }

    for (int i = 0; i < first.terms; i++) {
        printf("%d %d %d\n", result.M2[i][0], result.M2[i][1], result.M2[i][2]);
    }
}






