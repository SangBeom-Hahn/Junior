package HSB;

public class BST<key extends Comparable<key>, value> {
	Node root;
	BST(){
		root = null;
	}
	//¸Þ¼Òµå
	public Node getRoot() {
		return root;
	}
	public void setRoot(Node root) {
		this.root = root;
	}
	public Node map() {
		Node<Integer, String> n1 = new Node<>(50, "n1");
		Node<Integer, String> n2 = new Node<>(30, "n2");
		Node<Integer, String> n3 = new Node<>(80, "n3");
		Node<Integer, String> n4 = new Node<>(10, "n4");
		Node<Integer, String> n5 = new Node<>(40, "n5");
		Node<Integer, String> n6 = new Node<>(90, "n6");
		return n1;
	}
	public value get(Node root, key k) {
		if(root == null) {
			return null;
		}
		else if(root.getItem().compareTo(k)>0) {
			return get(root.getLeft(), k); 
		}
		else if(root.getItem().compareTo(k)<0) {
			return get(root.getRight(), k); 
		}
		else {
			return (value)root.getName();
		}
	}
	public value min(Node root) {
		if(root.getLeft() != null) {
			min(root.getLeft());
		}
		return (value) root.getName();
	}
	public Node put(Node root, key k, value v) {
		if(root == null) {
			Node<Integer, String> newNode = Node<>(k, v);
			return newNode;
		}
		else if(root.getItem().compareTo(k)>0) {
			return root.setLeft(put(root.getLeft(), k)); 
		}
		else if(root.getItem().compareTo(k)<0) {
			return root.setRight(put(root.getRight(), k)); 
		}
		else {
			root.setName(v));
		}
		return root;
	}
	public Node deleteMin(Node root) {
		if(root.getLeft() == null) {
			return root.getRight();
		}
		else {
			root.setLeft(deleteMin(root.getLeft()));
		}
		return root;
	}
	public Node delete(Node root, key k) {
		if(root.getItem() == k) {
			if(root.getLeft() == null) {
				root.setLeft(root.getRight());
			}else if(root.getRight() == null) {
				root.setRight(root.getLeft());
			}else {
				root.setItem(minValue(root.right));
			}
		}
		else if(root.getItem().compareTo(k)>0){
			root.setLeft(delete(root.getLeft(), k));
		}
		else {
			root.setRight(delete(root.getRight(), k));
		}
		return root;
	}
	public key minValue(Node n) {
		if(n.getLeft() != null) {
			minValue(n.getLeft());
		}
		return (key) n.getItem();
	}
}
