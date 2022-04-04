#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>
# define SIZE 4

int* matrix(int A[][4], int B[][4], int n, int m);
int main(void){
    int A[4][4] = {
        {2,5,2,5},
        {0,-1,0,-1},
        {2,5,2,5},
        {0,-1,0,-1}
    } ;

    int B[4][4] = {
        {1,2,1,2},
        {3,0,3,0},
        {1,2,1,2},
        {3,0,3,0}
    } ;

    int C[4][4];
}    

int* matrix(int A[][4], int B[][4], int n, int m){

    if(sizeof(A)/sizeof(A[0]) <= 2){
        return; 
    }
    int A11[n/2][m/2];
    int A12[n/2][m/2];
    int A21[n/2][m/2];
    int A22[n/2][m/2];

    int B11[n/2][m/2];
    int B12[n/2][m/2];
    int B21[n/2][m/2];
    int B22[n/2][m/2];

    int C11[n/2][m/2];
    int C12[n/2][m/2];
    int C21[n/2][m/2];
    int C22[n/2][m/2];

    //A
    for (int i = 0; i < SIZE/2; i++){
        for (int j = 0; j < SIZE/2; j++){
            A11[i][j] = A[i][j];
        }     
    }
    for (int i = 0; i < SIZE/2; i++){
        for (int j = SIZE/2; j < SIZE; j++){
            A12[i][j-SIZE/2] = A[i][j];
        }     
    }

    for (int i = SIZE/2; i < SIZE; i++){
        for (int j = 0; j < SIZE/2; j++){
            A21[i-SIZE/2][j] = A[i][j];
        }     
    }
    for (int i = SIZE/2; i < SIZE; i++){
        for (int j = SIZE/2; j < SIZE; j++){
            A22[i-SIZE/2][j-SIZE/2] = A[i][j];
        }     
    }

    //B
    for (int i = 0; i < SIZE/2; i++){
        for (int j = 0; j < SIZE/2; j++){
            B11[i][j] = B[i][j];
        }     
    }
    for (int i = 0; i < SIZE/2; i++){
        for (int j = SIZE/2; j < SIZE; j++){
            B12[i][j-SIZE/2] = B[i][j];
        }     
    }

    for (int i = SIZE/2; i < SIZE; i++){
        for (int j = 0; j < SIZE/2; j++){
            B21[i-SIZE/2][j] = B[i][j];
        }     
    }
    for (int i = SIZE/2; i < SIZE; i++){
        for (int j = SIZE/2; j < SIZE; j++){
            B22[i-SIZE/2][j-SIZE/2] = B[i][j];
        }     
    }   



    //C
    for(int i = 0; i < n/2; i++){
        for(int j = 0; j < n/2; j++){
            C11[i][j] = A11[i][0]*B11[0][j] + A11[i][1]*B11[1][j];
        }
    }

    for(int i = 0; i < n/2; i++){
        for(int j = 0; j < n/2; j++){
            C12[i][j] = A12[i][0]*B12[0][j] + A12[i][1]*B12[1][j];
        }
    }

    for(int i = 0; i < n/2; i++){
        for(int j = 0; j < n/2; j++){
            C21[i][j] = A21[i][0]*B21[0][j] + A21[i][1]*B21[1][j];
        }
    }

    for(int i = 0; i < n/2; i++){
        for(int j = 0; j < n/2; j++){
            C22[i][j] = A22[i][0]*B22[0][j] + A22[i][1]*B22[1][j];
        }
    }    

    matrix(A11, B11, sizeof(A11)/sizeof(A11[0]), sizeof(B11)/sizeof(B11[0]));
    matrix(A12, B12, sizeof(A12)/sizeof(A12[0]), sizeof(B12)/sizeof(B12[0]));
    matrix(A21, B21, sizeof(A21)/sizeof(A21[0]), sizeof(B21)/sizeof(B21[0]));
    matrix(A22, B22, sizeof(A22)/sizeof(A22[0]), sizeof(B22)/sizeof(B22[0]));
 
}


