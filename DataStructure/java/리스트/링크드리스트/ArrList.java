package HSB;

public class ArrList<E> {
	
	Node<E> head;
	int size;
	
	ArrList(){
		head = null;
		size = 0;
	}
	
	public class Node<E>{
		
		Node<E> link;
		E data;
		
		Node(Node link, E data){
			this.data = data;
			this.link = link;
		}

		public Node<E> getLink() {
			return link;
		}

		public void setLink(Node<E> link) {
			this.link = link;
		}

		public E getData() {
			return data;
		}

		public void setData(E data) {
			this.data = data;
		}
		
	}
	public int research(E data) {
		Node p = head;
		for(int k=0; k<size; k++) {
			if(data == p.getData())
				return k;
			p = p.getLink();
		}
		return -1;
	}
	public void insertFront(E data) {
		head = new Node<>(head, data);
		size++;
	}
	public void insertAfter(E data, Node p) {
		p.setLink(new Node<>(p.getLink(), data));
		size++;
	}
	public E deleteFront() {
		E src = head.getData();
		head = head.getLink();
		size--;
		return src;
	}
	public E deleteAfter(Node p) {
		E data = (E) p.getLink().data;
		Node remove = p.getLink();
		p.setLink(remove.getLink());
		remove = null;
		size--;
		return data;
	}
	
}
