/*
게임 : 전주듣고 제목을 맞히면 점수를 얻음, 최종적으로 점수 높으면 이김
윤수 : 노래 첫 4음만 들어도 맞출수 있음
정환 : 3음만 들어도 노래 맞추는 프로그램을 만들고 싶음

1. 모경수(prt, n=1)
1) N개의 노래를 (3개음, 노래 제목) 으로 사전 만듬
2) M개 노래 순회하면서 검색
    1) 검색 전에 없으면 !
    2) 있으면
        1] 제거 후 한번더 있는지 체크 -> 있으면 ? 출력 -> 처음 제거한거 다시 넣음
        2] -> 없으면 !출력 -> 다시 넣을 필요 없음

* N : 정환이 음을 아는 노래의 개수
M : 게임 시작하고 들어올 노래 개수

T : N개의 노래 제목의 길이, S : 대소문자 구분하는 노래 제목, 해당 노래에 첫 7개의 음
M개의 정환이 맞출 3개의 음
출 : 맞출 노래에 대해서 3음이 동일한 노래 (1개 있다면 노래 제목, 두개 이상이면 ?, 없으면 !)

2. nlogn
*/

import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        HashMap<String, List<String>> map = new HashMap<>();
        StringBuilder sb = new StringBuilder();

        for(int i=0; i<n; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            sb = new StringBuilder();
            int leng = Integer.parseInt(st.nextToken());
            String title = st.nextToken();

            for(int j=0; j<3; j++) {
                sb.append(st.nextToken());
            }
            String key = sb.toString();
            if(map.containsKey(key)) {
                map.get(key).add(title);
            } else {
                map.put(key, new ArrayList<>(List.of(title)));
            }
        }
//        System.out.println(map);


//        2) M개 노래 순회하면서 검색
//            1) 검색 전에 없으면 !
//            2) 있으면
//                1] 제거 후 한번더 있는지 체크 -> 있으면 ? 출력 -> 처음 제거한거 다시 넣음
//                2] -> 없으면 !출력 -> 다시 넣을 필요 없음

        for(int i=0; i<m; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            sb = new StringBuilder();
            for(int j=0; j<3; j++) {
                sb.append(st.nextToken());
            }
            String key = sb.toString();

            if(!map.containsKey(key)) {
                System.out.println("!");
            } else {
                List<String> value = map.get(key);
                if(value.size() >= 2) {
                    System.out.println("?");
                } else {
                    System.out.println(value.get(0));
                }
            }
        }
    }
}
