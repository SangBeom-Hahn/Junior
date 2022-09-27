package main;

import java.util.*;
import java.lang.Math;

public class Main {
	
	public static void main(String[] args) {
		
		int arr[] = {4, 23, 33, 15, 17, 19};
		
		Arrays.sort(arr);
		
		for(int ar : arr) {
			System.out.println(ar);
		}
	}
	
	/*public static void print(Student[] st, String key) {
		System.out.println();
		System.out.println("     "+key+"로 정렬");
		System.out.println("---------------");
		for(Student temp : st) {
			System.out.print(temp.getId()+" "+temp.getName()+" "+temp.getDep()+" "+temp.getGrade()+" ");
		}
	}
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		
		Student stu[] = {
				new Student(111, "한**", "컴퓨터", 2),
				new Student(222, "김**", "사회", 2),
				new Student(333, "정**", "러시아", 2)
		};
		
		Arrays.sort(stu);
		print(stu, "ID");
		Arrays.sort(stu, new Dep());
		print(stu, "DEP");
		
		
	}*/
}








