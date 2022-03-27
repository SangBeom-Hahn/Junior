package HSB;
import java.util.*;
import java.lang.*;

public class Issue {
	String str;
	int len;
	Issue(String str){
		this.str = str;
		this.len = str.length();
	}
	
	//¸Þ¼Òµå
	public StringBuffer back() {
		Stack<String> s = new Stack<>();
		StringBuffer sb = new StringBuffer();
		int i = 0;
		while(i<len) {
			char c = str.charAt(i);
			if(c!='+' && c!='-' && c!='*' && c!='/') {
				sb.append(c);
				i++;
			}
			else {
				while(true) {
					if(!s.isEmpty()) {
						String stack = s.peek();
						boolean inject = rank(c, stack);
						if(inject) {
							String out = s.pop();
							sb.append(out);
						}
						else {
							s.push(Character.toString(c));
							i++;
							break;
						}
					}
					else {
						s.push(Character.toString(c));
						i++;
						break;
					}
				}
			}
		}
		while(!s.isEmpty()) {
			sb.append(s.pop());
		}
		return sb;
	}
	public boolean rank(char in, String stack) {
		switch (in) {
		case '*':
			if(stack == "*" || stack == "/")
				return true;
			else 
				return false;
			
		case '/':
			if(stack == "*" || stack == "/")
				return true;
			else 
				return false;
				
		
		case '+':
			return true;
			
		case '-':
			return true;	
		}
		return false;
	}
}