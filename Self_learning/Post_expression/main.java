package HSB;

import java.util.*;

public class main { //조건문, 반복분 return 조건, 문자열에서 문자빼는 라이브러리 사용기
	public static void main(String[] args) {
		StringBuffer s = new StringBuffer();
		
		Issue i = new Issue("8/2-3+3*2");
		s = i.back();
		System.out.print(s);
		
	}
}