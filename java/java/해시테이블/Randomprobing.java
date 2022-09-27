package HSB;
import java.util.Random;

public class Randomprobing<k, v> {
	int M, N;
	Object Key[];
	Object Value[];
	//생성자
	Randomprobing(int M){
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
		Random rand = new Random();
		do {
			if(Key[i] == null) { //조건문 사용방법 null이면 넣고 아니면 다음이지 아니면 안넣는다?? 아니다
				Key[i] = key;
				Value[i] = value;
				System.out.println(Key[i]+"의 해시값="+i+", 데이터는 "+Value[i]);
				N++;
				break;
			}
			if(key.equals(Key[i])) {
				Value[i] = value;
				break;
			}
			i = (i+rand.nextInt(1000)) % M;
		}while(N < M); //원소수가 전체 크기보다 작을 동안
	}
	public v get(k key) {
		int start = hash(key);
		if(Key[start] != null) 
			return (v) Value[start];
		return null;
	}
}
