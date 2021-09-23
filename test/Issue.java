package HSB;
import java.util.*;
import java.lang.*;

public class Issue {
	String str;
	int len;
	Issue(String str){
		this.str = str;
		len = str.length();
	}
	//¸Þ¼Òµå
	public int cal() {
		Stack<Character> s = new Stack<>();
		int N = 0;
		while(N<len) {
			char c = str.charAt(N);
			int result = 0;
			if(c == '+' || c == '-' || c == '*' || c == '/') {
				char out2 = s.pop();
				char out1 = s.pop();
				
				
				switch (c) {
				case '+': result = (int)out1 + (int)out2; break;
				case '-': result = (int)out1 - (int)out2; break;
				case '*': result = (int)out1 * (int)out2; break;
				case '/': result = (int)out1 / (int)out2; break;
				}
				String res = Integer.toString(result);
				char c2 = res.charAt(0);
				s.push(c2);
			}
			else {
				s.push(c);
			}
			N++;
		}
		return s.pop();
	}
	
}