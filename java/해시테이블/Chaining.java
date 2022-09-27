package HSB;

public class Chaining<k,v> {
	int M;
	Node n[];
	Chaining(int M){
		this.M = M;
		n = new Node[M];
	}
	class Node<k,v>{
		k key;
		Object data;
		Node next;
		Node(k key, Object data, Node next) {
			this.key = key;
			this.data = data;
			this.next = next;
		}
		/*public void setNext(Node next) {
			this.next =next;
		}*/
	}
	public int hash(k key) {
		return (key.hashCode() & 0x7fffffff) & M;
	}
	public void put(k key, v data) {
		int i = hash(key);
		for(Node p = n[i]; p != null; p = p.next) {
			if(p.key.equals(key)) {
				p.data = data;
				return;
			}
		}
		n[i] = new Node(key, data, n[i]);
	}
	public v get(k key) {
		int i = hash(key);
		for(Node p = n[i]; p != null; p = p.next) {
			if(p.key.equals(key)) {
				return (v) p.data;
			}
		}
		return null;
	}	
}
