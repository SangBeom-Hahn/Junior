package HSB;

public class ArrQueue<E> {

	Object o[];
	int front, rear, size;
	
	//생성자
	ArrQueue(){
		size=front=rear= 0;
		o = new Object[2];
	}
	
	public int size() {
		return size;
	}
	public boolean isEmpty() {
		return(size == 0);
	}
	public void add(E data) {
		if((rear+1) % o.length == front)
			resize(2*o.length);
		rear = (rear+1) % o.length;
		o[rear] = data;
		size++;
	}
	public Object resize(int newsize) {
		Object oo[] = new Object[newsize];
		for(int i = 0; i<o.length; i++) {
			oo[i] = o[i];
		}
		o = oo;
		return o; 	
	}
	public E delete() {
		if(size > 0 && size == o.length)
			resize(o.length/2); 
		o[front] = null;
		front = (front+1) % o.length;
		E data = (E) o[front];
		return data;
	}
	public void print() {
		for(int i=0; i<o.length; i++)
			System.out.print(o[i]+"  "); //object배열이므로 어떤 타입이든 출력 가능
	}
	
}