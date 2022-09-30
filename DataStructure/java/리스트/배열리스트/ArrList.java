package Main;
import java.util.*; //빈배열인데 peek할때 언더플로우 에러

public class ArrList<E> {
	
	//필드
	Object o[];
	int size;
	boolean b;
	
	ArrList(){
		size = 0;
		o = new Object[1];
	}
	
	//메서드
	public E peek(int a) {
		try{
			return (E)o[a];
		}
		catch(NoSuchElementException e){
			System.out.println("언더플로우 발생");
		}
		return null;
	}
	public void insertLast(E item) {
		if(size == o.length) {
			resize(2*o.length);
		}
		o[size++] = item;
	}
	public void resize(int newsize) {
		Object o1[] = new Object[newsize];
		for(int i=0; i<size; i++)
			o1[i] = o[i];
		o = o1;
	}
}
