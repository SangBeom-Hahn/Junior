/*
크기가 N인 수열에 a1 ~ an이 있다. 수열의 각 원소에 대해서 오큰수 NGE를 구할거다.
Ai의 오큰수 NGE(i) Ai보다 오른쪽에 있으면서 첫번째로 Ai보다 큰 수
없으면 -1

ex) 3 5 2 7
i번째(Ai)     오큰수 NGE  
1번째         5
2           7
3           7
4           -1

선택      스택
3       3 -> 스택이 비면 넣음
5       팝 -> 선택 > 스택 탑 = 팝
5       5 -> 스택이 비면 넣음
2       5 2 -> 선택 <= 스택탑 = 넣음

1. 모경수(prt, n=1)
1) 스택이 비면 넣음
2) 선택 > 스택 탑 = 팝
3) 선택 <= 스택탑 = 넣음

* N  : 수열의 크기
수열의 원소
출 : N개의 수의 오큰수

2. nlogn

* */

import java.util.*;
import java.io.*;
import java.util.stream.Collectors;

/*
* System.out.println()
* */


public class Main {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

//        1) 스택이 비면 넣음
//        2) 선택 > 스택 탑 = 팝
//        3) 선택 <= 스택탑 = 넣음
        int n = Integer.parseInt(br.readLine());
//        StringTokenizer ste = new StringTokenizer(br.readLine(), " ");
        int[][] nums = new int[n][n];

        for (int i = 0; i < n; i++) {
            StringTokenizer ste = new StringTokenizer(br.readLine(), " ");
            for (int j = 0; j < n; j++) {
                nums[i][j] = Integer.parseInt(ste.nextToken());
            }
        }
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                sb.append(nums[i][j]).append(" ");
            }
            sb.append("\n");
        }
        System.out.print(sb);
    }
}








