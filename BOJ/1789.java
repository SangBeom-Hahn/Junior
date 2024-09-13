/*
서로 다른 N개의 자연수의 합이 S이다.
S를 알 때 자연수 N의 최대값은?

ex)
s       n       자연수 조합      n의 최대값
200     19



5       1       5               2
        2       1 4

        3       1 2 ,,, = 불가

6       6       = 서로 다른 자연수라 n이 s일순 없음
        5       = 1 2 3 4


n의 개수   최소값       가능한 숫자
1            1          1이상 (1 2 3 4 5 전부 다 가능)
2            3(1, 2)    3이상 ()
3           6(1, 2, 3)  6이상 ()
4           10(1, 2, 3, 4)  10이상

s가 10일때 n의 최대값은 4이고
9일때 n의 최대값은 3이란 소리 = 9는 4개로 절대 못 만든다는 소리다.


최소값을 1 3 6 10 15 늘려가면서 그때 1 2 3 4를 더하고 최소값이 s보다 커졌을 때 더한
n-1이 답

1. 모경수(prt, n=1)
1) n의 개수는 1부터 시작
2) 최소값은 0부터 시작해서 계속 더함
3) s가 1이면 최소값이 0이다가 1일땐 패스하고 3됐을 때 n-1이 답
4) 최소값이 s보다 커졌을때 더한 n-1 출력

* S
출 : 자연수 N의 최대값

2.

* */

import java.util.*;
import java.io.*;
import java.util.stream.Collectors;

/*
* System.out.println()
* */


public class Main {
//1) n의 개수는 1부터 시작
//2) 최소값은 0부터 시작해서 계속 더함
//3) s가 1이면 최소값이 0이다가 1일땐 패스하고 3됐을 때 n-1이 답
//4) 최소값이 s보다 커졌을때 더한 n-1 출력
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long s = Long.parseLong(br.readLine());
        long n_cnt = 1;
        long min_value = 0;
        int su = 1;

        while(true) {
//        while(su != 2) {
            if(min_value > s) {
                System.out.println(n_cnt - 2);
                break;
            }
//            System.out.println(n_cnt+ " " +min_value);

            min_value += n_cnt;
            n_cnt += 1;
            su += 1;
        }
    }
}





















