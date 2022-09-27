package Main;

public class Node<Key extends Comparable<Key>> { 
	//필드
	Key item;
	Node<Key> left;
	Node<Key> right;
	//생성자
	Node(Key item, Node<Key> left, Node<Key> right){
		this.item = item;
		this.left = left;
		this.right = right;
	}
	//메소드
	public Key getItem() {
		return item;
	}
	public void setItem(Key item) {
		this.item = item;
	}
	public Node<Key> getLeft() {
		return left;
	}
	public void setLeft(Node<Key> left) {
		this.left = left;
	}
	public Node<Key> getRight() {
		return right;
	}
	public void setRight(Node<Key> right) {
		this.right = right;
	}
}
