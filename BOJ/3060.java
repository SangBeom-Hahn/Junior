/*
원형 식탁에 돼지 6마리
기억 : 전날 양쪽, 맞은편 음식 양
추가 : 전날 자신이 먹은양에다가, 기억하는 만큼 양을 추가하여 식사하기를 원해
N : 매일 오는 사료, 남은 사료는 모두 폐기

ex)
1   2   3   4   5   6번돼지
3   2   7   1   5   4

돼지  양쪽  맞음편     전날  총합
2       10  5       2       17 -> 둘째날에는 17만큼 먹고 셋째날에는 더 늘려가는 것이다.

n = 21
1   2   3   4   5   6번돼지
1   2   3   4   5   6

돼지  양쪽  맞음편     전날  총합
1       8   4       1       13
2       4   5       2       11
3       6   6       3       15
4       8   1       4       13
5       10  2       5       17
6       6   3       6       15

1. 모경수(prt, n=1)
ok 1) 입력을 배열에 저장함 (번호대로 저장하기 위해 1번부터 저장하)
ok 2) 결과는 1부터 시작
2) 언제까지 줄 수 있나 반복
    1] 배열의 총합을 구함
    2] 총합 > n
        1] 결과 출력
    3] 총합 <= n
        1] 배열 갱신
            1] 가짜 배열을 만듦 (깊은 복사 어캐하지?)
            2] 현재 인덱스 -1 -> 0이면 6
            +1, -> 7이면 1
            +3 -> 나머지 6
            을 구해서 진짜 배열 idx 값 + 3개값을 가까 배열에 넣고 진짜 배열로 바꿈 (깊은 복사해야하나)

        2] 결과 ++


* t : 테케 수
n : 하루에 배달되는 사료의 양
1 ~ 6번 돼지가 첫날 먹었던 식사의 양
출 : 돼지 모두에게 밥을 줄 수 없게 되는 날이 몇 번째 날인가?

2. n^3


 */

import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine());

        for(int i=0; i<t; i++) {
            long n = Long.parseLong(br.readLine());
//            1) 입력을 배열에 저장함 (번호대로 저장하기 위해 1번부터 저장하)
//            2) 결과는 1부터 시작

            long[] wants = new long[7];
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            for(int j=1; j<7; j++) {
                wants[j] = Long.parseLong(st.nextToken());
            }

            // System.out.println(Arrays.toString(wants));

            long result = 1;

//            2) 언제까지 줄 수 있나 반복
//                ok 1] 배열의 총합을 구함
//                ok 2] 총합 > n
//                    1] 결과 출력
//                3] 총합 <= n
//                    1] 배열 갱신
//                        1] 가짜 배열을 만듦 (깊은 복사 어캐하지?)
//                        2] 현재 인덱스 -1 -> 0이면 6
//                        +1, -> 7이면 1
//                        +3 -> 나머지 6
//                        을 구해서 진짜 배열 idx 값 + 3개값을 가까 배열에 넣고 진짜 배열로 바꿈 (깊은 복사해야하나)
//
//                    2] 결과 ++
            int su = 1;
            while(true) {
//            while(su != 3) {
                long hab = 0;
                for(int j=1; j<7; j++) {
                    hab += wants[j];
                }

                if(hab > n) {
                    System.out.println(result);
                    break;
                }
                else {
                    result += 1;
                    // 가짜 배열
                    long[] fakes = new long[7];
                    for(int j=1; j<7; j++) {
                        fakes[j] = wants[j]; // 이전값 더함
                        // -1
                        int minusOne = j-1;
                        if(minusOne == 0) minusOne = 6;
                        fakes[j] += wants[minusOne];

                        // +1
                        int plusOne = j+1;
                        if(plusOne == 7) plusOne = 1;
                        fakes[j] += wants[plusOne];

                        // +3
                        int plusThree = (j+3) % 6;
                        if(plusThree == 0) plusThree = 6;
                        fakes[j] += wants[plusThree];
                    }

                    for(int j=1; j<7; j++) {
                        wants[j] = fakes[j];
                    }

                    // System.out.println(Arrays.toString(fakes));
                }

                su += 1;
            }
        }
    }
}