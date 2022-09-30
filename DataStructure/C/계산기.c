#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char translate(char *sik);

int main(void) {

	translate("8/2-3");
	return 0;
}
int prec(char c){
	if(c == '+'|| c == '-')return 1;
	if(c == '*'|| c == '/')return 2;
}

char translate(char *sik){ //char *sik = "s/2-3"
	
	char *result;
	int pos=0;
	
	for(int i =0; i<strlen(sik); i++){
		if(sik[i]== '+' || sik[i]== '-' || sik[i]== '*' || sik[i]== '/'){//연산자 
			while(!empty(&stack) && prec(sik[i]) <= prec( peek(&s)) ){
				result[pos] = pop(&s);
				pos++;
			}
			push(&s, sik[i]);	 
		}
		else{//피연산자 
			result[pos] = sik[i];
			pos++;
		}
	}
	while(!empty(&s)){
		result[pos]= pop(&s);
		p++;
	}
}

int cal(char *sik){
	
	for(int i =0; i<strlen(sik); i++){
		int value=0;
		
		if(sik[i]== '+' || sik[i]== '-' || sik[i]== '*' || sik[i]== '/'){
			op1 = pop(&s);
			op2 = pop(&s);
			
			switch(sik[i]){
				case '+': push(&s, op1+op2); break;
				case '-': push(&s, op1-op2); break;
				case '*': push(&s, op1*op2); break;
				case '/': push(&s, op1/op2); break;
				
			}
		}
		else{ //피연산자 
			value = sik[i]-'0';	
			push(&s, value); 
		}
	}
	ruturn pop(&s);	
}


















