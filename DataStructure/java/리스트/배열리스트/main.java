package Main;

public class main {
	
	public static void main(String[] args) {

		ArrList<Integer> a = new ArrList<>();
		a.insertLast(2);
		a.insertLast(3);
		
		System.out.println(a.peek(0));
		System.out.println(a.peek(1));
		
	}
}



