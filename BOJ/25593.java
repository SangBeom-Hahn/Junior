/*
4교대 근무를 선다.
각 인원의 시간 = 12시간 이하 차이남
최대 50주치 근무표를 짤거임

1. 모경수(prt, n=1)
1) n주를 입력 받음 -> 1주를 4줄씩 입력 받음
2) 첫번째 줄 순회하면서 map에 사람 넣고, 시간 더함
2) 두번째, 세, 네도 동일함

3) 이것 n 주동안 함
4) 모든 사람의 시간이 12시간 이하로 차이나는 지 구함
    1] 완전 탐색
    2] 최대와 최소의 차이가 12시간 이하면 되지 않을까?

* n : 주의 개수
근무표 (하루에 4명 4교대, 1주에 7일 = 1주체 28개) (각 주는 4개의 줄 = 1열 = 하루 4명)
1열 (위에서부터 순서대로 근무시간), - : 근무자가 없음

출 : 근무표가 공평하면 yes, 아니면 no (아무도 근무안해도 공평한거임 = 12시간 이하 차이니깐)

2. n^3
*/

import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws IOException {
//        1) n주를 입력 받음 -> 1주를 4줄씩 입력 받음
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int n = Integer.parseInt(br.readLine());
        HashMap<String, Integer> map = new HashMap<>();
        for(int i=0; i<n; i++) {
            for(int j=0; j<4; j++) {
                st = new StringTokenizer(br.readLine(), " ");
//                2) 첫번째 줄 순회하면서 map에 사람 넣고, 시간 더함
                for(int k=0; k<7; k++) {
                    String name = st.nextToken();


                    if(j == 0) {
                        if(map.containsKey(name)) {
                            map.put(name, map.get(name) + 4);
                        } else {
                            map.put(name, 4);
                        }
                    }
                    if(j == 1) {
                        if(map.containsKey(name)) {
                            map.put(name, map.get(name) + 6);
                        } else {
                            map.put(name, 6);
                        }
                    }
                    if(j == 2) {
                        if(map.containsKey(name)) {
                            map.put(name, map.get(name) + 4);
                        } else {
                            map.put(name, 4);
                        }
                    }
                    if(j == 3) {
                        if(map.containsKey(name)) {
                            map.put(name, map.get(name) + 10);
                        } else {
                            map.put(name, 10);
                        }
                    }
                }
            }
        }
//        4) 모든 사람의 시간이 12시간 이하로 차이나는 지 구함
//        1] 완전 탐색
//        2] 최대와 최소의 차이가 12시간 이하면 되지 않을까?
        map.remove("-");
//        System.out.println(map);
        int max = 0;
        int min = 999999999;
        for(Integer time : map.values()) {
            if(max < time) {
                max = time;
            }
            if(min > time) {
                min = time;
            }
        }
        if(max - min <= 12) {
            System.out.print("Yes");
        } else {
            System.out.print("No");
        }
    }
}
