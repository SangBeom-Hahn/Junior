/*
감소하는 수 : 양의 정수 x의 자릿수가 가장 큰 자릿수부터 작은 자릿수까지 감소한다면
ex) 감소수 : 321 950
감소수 아님 : 322 958
N번째 감소하는 수를 출력하라 (0 = 0번째, 1=1 번째, N번째 감소하는 수가 없으면 -1)

감소하는수
0
1
2
3
4
5
6
7
8
9
10
20
21
9876543210
1. 모경수(prt, n=1)
1) 0 ~ 9의 수 중에서 길이가 1 ~ 10까지 조합을 구함 -> 백으로 탐색
2) 모든 조합 요소를 뒤집음
3) N번째를 구함

* N : N번째 감소하는 수를 구할거임
출 : N번째 감소하는 수

2. n 

* */

import java.util.*;
import java.io.*;
import java.util.stream.Collectors;

/*
* System.out.println()
* */


public class Main {
    
    static String[] arr = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"};
    static Set<Long> dicreases = new HashSet<>();
    
    static void back(int start, String comb) {
        for(int i=start; i<10; i++) {
            StringBuilder sb = new StringBuilder(comb+arr[i]);
            sb.reverse();

//            System.out.println(Long.parseLong(sb.toString()));
            dicreases.add(Long.parseLong(sb.toString()));
            back(i+1, comb+arr[i]);

//            System.out.println(Integer.parseInt(comb+arr[i]));
//            dicreases.add(Integer.parseInt(comb+arr[i]));
//            back(i+1, comb+arr[i]);
        }
    }
    
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

//        0 ~ 9의 수 중에서 길이가 1 ~ 10까지 조합을 구함 -> 백으로 탐색
        back(0, "");
        List<Long> result = new ArrayList<>(dicreases);
        Collections.sort(result);
        int leng = result.size();

        if(leng <= n) {
            System.out.println(-1);
            return;
        }

        System.out.println(result.get(n));
    }
}
