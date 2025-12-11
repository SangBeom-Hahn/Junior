/*
a b c의 곱에 0 ~ 9 숫자가 몇 번 쓰였나?

ex) 17037300에서 0은 3번

100 100 100

1. 모경수
1) 정수를 곱해서 문자열로 바꾼다
2) 문자열을 순회해서 dic에 개수를 저장한다.
3) dic를 순회해서 결과를 출력한다.

* a, b, c
출 : 세 숫자의ㅡ 곱에 0~9가 몇 번 쓰였는지 구하라

2. n

 */

import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int a = Integer.parseInt(br.readLine());
        int b = Integer.parseInt(br.readLine());
        long c = Long.parseLong(br.readLine());

        String string = String.valueOf(a * b * c);
        Map<String, Integer> dic = new HashMap<>();

        for(String alpha : string.split("")) {
            if(dic.containsKey(alpha)) {
                dic.put(alpha, dic.get(alpha) + 1);
            } else {
                dic.put(alpha, 1);
            }
        }

        for(int i=0; i<10; i++) {
            if(dic.containsKey(String.valueOf(i))) {
                System.out.println(dic.get(String.valueOf(i)));
            } else {
                System.out.println(0);
            }
        }
    }
}
