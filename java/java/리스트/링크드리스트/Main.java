package HSB;

public class Main {
	public static void main(String[] args) {
		
		ArrList<Integer> a = new ArrList<>();
		
		a.insertFront(1);
		a.insertFront(2);
		a.insertFront(3);
		a.insertAfter(4, a.head.getLink());
		
		System.out.println(a.deleteAfter(a.head.getLink()));
		System.out.println(a.research(4));
	}
}