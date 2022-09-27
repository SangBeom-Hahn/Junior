package main;

import java.util.*;

public class Student implements Comparable<Student>{
	
	//public static final Comparator<Student> ID = new Id();
	//public static final Comparator<Student> DEP = new Dep();
	public static final Comparator<Student> GRADE = new Grade();
	
	private int id;
	private String name;
	private String dep;
	private int grade;
	
	Student(int id, String name, String dep, int grade){
		this.id = id;
		this.name = name;
		this.dep = dep;
		this.grade = grade;
	}

	public int getId() {
		return id;
	}
	public String getName() {
		return name;
	}
	public String getDep() {
		return dep;
	}
	public int getGrade() {
		return grade;
	}
	@Override
	public int compareTo(Student o) {
		// TODO Auto-generated method stub
		return 0;
	}
}

class Name implements Comparator<Student>{
	
	@Override
	public int compare(Student s1, Student s2) {
		// TODO Auto-generated method stub
		return s1.getName().compareTo(s2.getName());
	}
}

class Dep implements Comparator<Student>{
	
	public int compare(Student o1, Student o2) {
		// TODO Auto-generated method stub
		return o1.getDep().compareTo(o2.getDep());
	}
}

class Id {
	
	public int compare(Student o1, Student o2) {
		// TODO Auto-generated method stub
		return o1.getId() - o2.getGrade();
	}
}

class Grade implements Comparator<Student>{
	
	@Override
	public int compare(Student o1, Student o2) {
		// TODO Auto-generated method stub
		return o1.getGrade() - o2.getGrade();
	}
}