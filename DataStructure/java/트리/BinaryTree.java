package Main;
import java.util.*;

public class BinaryTree<Key extends Comparable<Key>> {
	//필드
	Node root;
	BinaryTree(){
		root = null;
	}
	public Node getRoot() {
		return root;
	}
	public void setRoot(Node root) {
		this.root = root;
	}
	public boolean isEmpty() {
		return root == null;
	}
	//메소드
	public void preorder(Node node) {
		if(node != null) {
			System.out.print(node.getItem()+"->");
			preorder(node.getLeft());
			preorder(node.getRight());
		}
	}
	public void inorder(Node node) {
		if(node != null) {
			inorder(node.getLeft());
			System.out.print(node.getItem()+"->");
			inorder(node.getRight());
		}
	}
	public void postorder(Node node) {
		if(node != null) {
			postorder(node.getLeft());
			postorder(node.getRight());
			System.out.print(node.getItem()+"->");
		}
	}
	public void levelorder() {
		Queue<Node> q = new  LinkedList<>();
		q.add(root);
		while(!q.isEmpty()) {
			root = q.remove();
			if(root != null) {
				System.out.print(root.getItem()+"->"); //null을 넣지도 않겠다 vs 넣기는 한다 차이
				q.add(root.getLeft());
				q.add(root.getRight());
			}
		}
	}
	public boolean isEqual(Node n, Node m) {
		if(n.getItem().compareTo(m.getItem()) != 0)
			return false;
		return(isEqual(n.getLeft(), m.getLeft()) && 
				isEqual(n.getRight(), m.getRight()));
	}
	public Node map() {
		Node<String> a = new Node<>("A", null, null);
		Node<String> b = new Node<>("B", null, null);
		Node<String> c = new Node<>("C", null, null);
		Node<String> d = new Node<>("D", null, null);
		Node<String> e = new Node<>("E", null, null);
		Node<String> f = new Node<>("F", null, null);
		Node<String> g = new Node<>("G", null, null);
		Node<String> h = new Node<>("H", null, null);
		
		a.setLeft(b); a.setRight(c);
		b.setLeft(d); b.setRight(e);
		c.setRight(f);
		d.setRight(g);
		e.setLeft(h);
		return a;
	}
}
