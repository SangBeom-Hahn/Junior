package HSB;

public class main { //조건문, 반복분 return 조건, 문자열에서 문자빼는 라이브러리 사용기
	public static void main(String[] args) {
		
		ArrQueue<String> q = new ArrQueue<>();
		q.add("apple");
		q.add("orange");
		q.add("pear");
		q.add("cherry");
		q.print();
		q.delete();
		q.delete();
		System.out.println();
		q.print();
		System.out.println();
		q.add("apple");
		q.add("orange");
		q.add("pear");
		q.add("cherry");
		q.print();
	}
}