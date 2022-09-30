package Main;
import java.util.Arrays;
import java.util.*;

class Peaple implements Comparable{
	
	int age;
	String name;
	
	Peaple(String name, int age){
		this.name = name;
		this.age = age;
	}
	
	public void print() {
		System.out.println(name + " "+ age);
	}
@Override
	public int compareTo(Object pea) {
		// TODO Auto-generated method stub
		Peaple temp = (Peaple)pea;
		if(this.age < temp.age) 
			return -1;
		else if(this.age == temp.age)
			return 0;
		else
			return 1;
	}
}

class name implements Comparator<Peaple>{
	
	@Override
	public int compare(Peaple p1, Peaple p2) {
		// TODO Auto-generated method stub
		return p1.name.compareTo(p2.name);
	}
}

class Age implements Comparator<Peaple>{
	
	@Override
	public int compare(Peaple p1, Peaple p2) {
		// TODO Auto-generated method stub
		return p1.age- p2.age;
	}
}

public class Sort {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Peaple p[] = { 
				new Peaple("한상범", 23),
				new Peaple("김미르", 22),
				new Peaple("정한영", 21)
		};
		//이름으로 정렿하는 방법
		Arrays.sort(p, new name());
		for( Peaple pea : p) {
			pea.print();
		}
	}

}