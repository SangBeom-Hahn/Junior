package HSB;

public class CList<E> {

	public class Node<E> {

		E data;
		Node next;
		
		Node(E data, Node n){
			this.data =data;
			this.next = n;
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
	
	Node last;
	int size;
	
	CList(){
		last = null;
		size = 0;
	}
	
	//메소드
	public void insertfirst(E data) {
		Node<E> n = new Node<>(data, null);
		if(last == null) {
			n.setNext(n);
			last = n;
		}
		else {
			n.setNext(last.getNext());
			last.setNext(n);
		}
		size++;
	}
	public Node deleteFirst() {
		Node rem = last.getNext(); //last의 getnext가 맨앞이겠지?
		if ( rem == null)
			return rem;
		else {
			last.setNext(rem.getNext());//맨앞이 사라지는거니 맨 마지막게 맨앞이었던것의 하나 앞을 봐야지
		}
		size--;
		return rem;
	}
	public void print(){  // 연결 리스트 노드들의 항목들을 차례로 출력
		if (size > 0){
			int i = 0;
			for (Node p = last.getNext(); i<size ; p = p.getNext(), i++) 
					System.out.print(p.getData()+"\t ");
		}
		else
			System.out.println("리스트 비어있음.");
	}
}