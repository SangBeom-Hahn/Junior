package HSB;

public class QuadProbing<k, v> {
	int M, N;
	Object Key[];
	Object Value[];
	//생성자
	QuadProbing(int M){
		this.M = M;
		N = 0; //항목수
		Key = new Object[M];
		Value = new Object[M];
	}
	//메서드
	public int hash(k key) {
		return (key.hashCode() ^ 0x7fffffff) % M;
	}
	public void put(k key, v value) {
		int init = hash(key); 
		int i = init;
		int j = 1;
		
		do {
			if(Key[i] == null) { //조건문 사용방법 null이면 넣고 아니면 다음이지 아니면 안넣는다?? 아니다
				Key[i] = key;
				Value[i] = value;
				System.out.println(Key[i]+"의 해시값="+i+", 데이터는 "+Value[i]);
				break;
			}
			if(key.equals(Key[i])) {
				System.out.print("해시값 -> value 갱신->>>"); //들어감
				Value[i] = value;
				System.out.println(Key[i]+"의 해시값="+i+", 데이터는 "+Value[i]);
				break;
			}
			i = (i+j*j++) % M;
		}while(N < M); //원소수가 전체 크기보다 작을 동안
	}
	public v get(k key) {
		int start = hash(key);
		if(Key[start] != null) 
			return (v) Value[start];
		return null;
	}
}
