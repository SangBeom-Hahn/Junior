package HSB;

public class main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Chaining<Integer, String> l = new Chaining<>(13);
		l.put(50, "orange");
		l.put(60, "apple");
		l.put(60, "melon");
		System.out.println(l.get(50));
		System.out.print(l.get(60));
	}
}