package HSB;

public class Node<key extends Comparable<key>, value> {
	//ÇÊµå
	key item;
	value name;
	Node left;
	Node right;
	Node(key item, value name){
		this.item = item;
		this.name = name;
		left = right = null;
	}
	public key getItem() {
		return item;
	}
	public void setItem(key item) {
		this.item = item;
	}
	public value getName() {
		return name;
	}
	public void setName(value name) {
		this.name = name;
	}
	public Node getLeft() {
		return left;
	}
	public void setLeft(Node left) {
		this.left = left;
	}
	public Node getRight() {
		return right;
	}
	public void setRight(Node right) {
		this.right = right;
	}
	
}
