package HSB;

public class LinearProbing<k,v> { //선형 조사 해시테이블
	int M;
	Object Key[];
	Object Value[];
	//생성자
	LinearProbing(int M){
		this.M = M;
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
				break;
			}
			if(key.equals(Key[i])) {
				Value[i] = value;
				break;
			}
			i = (i+j++) % M;
		}while(i != init);
	}
	public v get(k key) {
		int start = hash(key);
		if(Key[start] != null) 
			return (v) Value[start];
		return null;
	}
}
