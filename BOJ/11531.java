/*
각 팀별로 제출 로그를 분석하겨 채점한다.
로그 : 제출시각, 문제이름, 제출결과

1팀 로그
3 e right
10 a wrong

점수 :
1) 푼문제수를 우선으로, 푼 문제수가 같다면 패널티를 기준으로 매겨짐
2) 패널티 :
    1] 맞춘 문제만 패널티를 부여
    2] 문제를 맞힌 시각 + 틀린 횟수 * 20

ex) 3분 E 해결 첫 제출
200분 A 해결 세번 제출
300분 D 해결 첫 제출
패널 티 : e = 3
a = 200 + 2(두번틀림) * 20
d = 300

1. 모경수(prt, n=1)
1) dic - 문제 이름 : [제출횟수, 시각, 결과]
2) 제출횟수 = 증가
3) 시각 = 갱신
4) 결과 = 갱신
5) dic을 순회해서 맞춘 문제에 대해서만 패널티를 구함 (시각 + 틀린 횟수 * 20)
6) 틀린 횟수 = 제출횟수 -1

* n 줄의 로그
시각, 문제이름, 결과
(마지막 = -1)

출 : 푼 문제수, 패널티

2. n^3

*/

import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {


        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        HashMap<String, int[]> map = new HashMap<>();

        while(true) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            int time = Integer.parseInt(st.nextToken());
            if(time == -1) {
                System.out.println();
                break;
            } else {
                String name = st.nextToken();
                String result = st.nextToken();
                int result_num; // 0 = 틀, 1 = 맞

                if(!map.containsKey(name)) {
                    if(result.equals("right")) {
                        result_num = 1;
                    } else {
                        result_num = 0;
                    }
//        1) dic - 문제 이름 : [제출횟수, 시각, 결과]
//        2) 제출횟수 = 증가
//        3) 시각 = 갱신
//        4) 결과 = 갱신
//        시각, 문제이름, 결과
                    map.put(name, new int[]{1, time, result_num});
                } else {
                    if(result.equals("right")) {
                        result_num = 1;
                    } else {
                        result_num = 0;
                    }
                    int cnt = map.get(name)[0];
                    map.put(name, new int[]{cnt+1, time, result_num});
                }
            }
        }
//        문제 이름 : [제출횟수, 시각, 결과]
//        5) dic을 순회해서 맞춘 문제에 대해서만 패널티를 구함 (시각 + 틀린 횟수 * 20)
//        6) 틀린 횟수 = 제출횟수 -1

        int result = 0;
        int match_cnt = 0;
        for(Map.Entry<String, int[]> entry : map.entrySet()) {
            int[] v = entry.getValue();
            int cnt = v[0];
            int time = v[1];
            int each_result = v[2];

            if(each_result == 1) {
                match_cnt += 1;
                result += (time + (cnt-1) * 20);
            }
        }

        System.out.println(match_cnt + " " + result);
    }
}
