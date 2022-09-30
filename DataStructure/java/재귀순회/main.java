package Main;

import java.util.*;
import java.lang.Math;

class Travel{
	
	Node start;
	Travel(){
		start = null;
	}
	public class Node {

		char data;
		Node left;
		Node right;
		
		public Node(char data, Node left, Node right) {
			this.data = data;
			this.left = left;
			this.right = right;
		}
	}
	public Node map() {
		
		Node n1 = new Node('H', null, null);
		Node n2 = new Node('F', null, null);
		Node n3 = new Node('S', null, null);
		Node n4 = new Node('U', null, null);
		Node n5 = new Node('E', null, null);
		Node n6 = new Node('Z', null, null);
		Node n7 = new Node('K', null, null);
		Node n8 = new Node('N', null, null);
		Node n9 = new Node('A', null, null);
		Node n10 = new Node('Y', null, null);
		Node n11 = new Node('T', null, null);
		
		n1.left = n2;
		n1.right = n3;
		n2.left = n4;
		n2.right = n5;
		n3.left = n6;
		n3.right = n7;
		n4.left = n8;
		n5.left = n9;
		n7.right = n10;
		n9.right = n11;
		
		return n1;
	}
	
	public void front(Node root) {
		if(root != null) {
			System.out.print(root.data+" -> ");
			front(root.left);
			front(root.right);
		}
	}
}
public class main {
	
	public static void main(String[] args) {

		Travel t = new Travel();
		t.start = t.map();
		t.front(t.start);
	}
}



