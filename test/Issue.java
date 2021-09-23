package HSB;
import java.util.*;

public class Issue {
	String str;
	int len;
	Stack<Character> s;
	boolean err;
	Issue(String str, int len){
		this.len = len;
		this.str = str;
		err = false;
		s = new Stack<>();
	}
	
	//¸Þ¼Òµå
	public boolean process() {
		int i = 0;
		char c = 0;
		while(i<len) {
			c = str.charAt(i);
			
			if(c == '}' || c ==']' || c == ')') {
				char ch = s.pop();
				
				switch(ch) {
				case '{':
					if(c != '}')
						err = true;
					break;
				case '[':
					if(c != ']')
						err = true;
					break;
				case '(':
					if(c != ')')
						err = true;
					break;
				}
			}
			else if(c == '{' || c =='[' || c == '('){
				s.add(c);
			}
			i++;
		}
		if(!s.isEmpty()) err = true;
		return err;
	}
}
