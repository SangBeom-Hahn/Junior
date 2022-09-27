package HSB;

public class main {
	public static void main(String[] args) {
		
		Stacks<String> s = new Stacks<>();
		
		s.push("apple");
		s.push("orange");
		s.push("cherry");
		System.out.println(s.pop());
		s.push("pear");
		s.print();
	}
}