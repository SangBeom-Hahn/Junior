package HSB;

public class DList<E> {

	public class Node<E> {

		E data;
		Node previous;
		Node next;

		Node(E data, Node p, Node n) {
			this.data = data;
			this.next = n;
			this.previous = p;
		}

		public E getData() {
			return data;
		}

		public void setData(E data) {
			this.data = data;
		}

		public Node getPrevious() {
			return previous;
		}

		public void setPrevious(Node previous) {
			this.previous = previous;
		}

		public Node getNext() {
			return next;
		}

		public void setNext(Node next) {
			this.next = next;
		}

	}
	
	Node head;
	Node tail;
	int size;
	DList(){//데이터, 앞, 뒤
		head = new Node(null, null,null); //이떼 tail 못넣는 이유 알지?? 재귀순회때처럼 tail에는 아직 데이터가 없어!! 
		tail = new Node(null, head, null);
		size = 0;
		head.setNext(tail);
	}
	
	//메소드
	public void insertBefore(Node p, E data) {
		Node<E> n = new Node<>(data, p.getPrevious(), p);
		p.setPrevious(n);
		p.getPrevious().setNext(n);
		size++;
	}
	public void insertAfter(Node p, E data) {
		Node<E> n = new Node<>(data, p, p.getNext());
		p.setNext(n);
		p.getNext().setPrevious(n);
		size++;
	}
	public void delete(Node s) {
		s.getPrevious().setNext(s.getNext());
		s.getNext().setPrevious(s.getPrevious());
		size--;
	}
	public void print(){  // 연결 리스트 노드들의 item들을 차례로 출력
 		if (size > 0) 
 			for (Node p = head.getNext(); p != tail; p = p.getNext()) 
 					System.out.print(p.getData()+"\t ");
 		else
 			System.out.println("리스트 비어있음");
 		System.out.println();
 	}
	
}