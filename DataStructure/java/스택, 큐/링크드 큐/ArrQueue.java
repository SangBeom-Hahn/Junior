package HSB;

public class ArrQueue<E> {

	int size;
	Node front, rear;
	
	public class Node<E>{
		E data;
		Node next;
		
		Node(E data, Node next){
			this.data = data;
			this.next = next;
		}

		public E getData() {
			return data;
		}

		public void setData(E data) {
			this.data = data;
		}

		public Node getNext() {
			return next;
		}

		public void setNext(Node next) {
			this.next = next;
		}
		
	}
	
	//생성자
	ArrQueue(){
		size=0;
		front=rear= null;
	}
	
	public int size() {
		return size;
	}
	public boolean isEmpty() {
		return(size == 0);
	}
	public void add(E data) {
		Node<E> p = new Node<>(data, null);
		if(isEmpty()) front = p;
		else rear.setNext(p);
		rear = p;
		size++;
	}
	public E delete() {
		Node rem = front;
		front = rem.getNext();
		size--;
		if(isEmpty()) rear = null;
		return (E) rem;
	}
	public void print() {
		Node p = front;
		for(;p != null; p = p.getNext()) { //null과 같지 않으면 조건문이네,,
			System.out.print("     "+p.getData());
		}
	}
}