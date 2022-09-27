package HSB;

public class Main {
	public static void main(String[] args) {
		
		DList<String> d = new DList<>();
		
		d.insertAfter(d.head, "apple");
		d.insertBefore(d.tail, "orange");
		d.insertBefore(d.tail, "cherry");
		d.insertAfter(d.head.getNext(), "pear");
		d.print();
	}
}