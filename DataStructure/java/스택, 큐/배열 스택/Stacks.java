package HSB;

public class Stacks<T> {
	//필드
	int top;
	Object o[];
	
	//생성자
	Stacks(){
		top = -1;
		o = new Object[1];
	}
	
	//메소드
	public int size() {
		return top+1;
	}
	public void push(T t1) {
		if(size() == o.length) {
			resize(2*o.length);
		}
		
		o[++top] = t1;
	}
	public T pop() {
		if(size() > 0 && size() == o.length/4) {
			resize(o.length/2);
		}
		return (T)o[top--];
	}
	public void resize(int newsize) {
		Object o1[] = new Object[newsize];
		
		for(int i = 0; i<o.length; i++)
			o1[i] = o[i];
		o = o1;
	}
	public void print() {
		for(int i=0; i<=top; i++)
			System.out.print(o[i]+"  "); //object배열이므로 어떤 타입이든 출력 가능
	}
}