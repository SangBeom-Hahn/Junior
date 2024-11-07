/*
과일 종류 : 딸기, 바나나, 라임, 자두
게임 룰
1) 플레이어들은 카드 뭉치를 공평하게 나눠 가짐, 자신이 가진 카드를 모두 소모하면 패배
2) 시작 : 시작 플레이어가 카드 한장을 공개
3) 이후 : 반시계 방향으로 본인의 카드를 한장씩 공개함
4) 종 누름 ; 펼쳐진 카드들 중 한종류 이사의 과일이 정확히 5개, 먼저 종 누른 사람이
모든 카드를 자신의 카드 뭉치 아래에 둠
5) 종 잘못 누름 : 다른 모든 플레이어에게 카드를 한장씩 나누어줌

1. 모경수(prt, n=1)
1) 4개 종류의 과일을 키로 개수를 벨류로 모음
2) dic을 순회해서 4개의 과일중 정확히 5개인게 하나라도 있으면 yes break
없으면 no

* n : 펼쳐진 카드의 개수
n개의 펼쳐진 카드 정보(과일 종류, 과일 개수)
출 : 종을 쳐야 하면 yes or no

2. nlogn
System.out.println
*/

import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws IOException {
//        4개 종류의 과일을 키로 개수를 벨류로 모음
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.valueOf(br.readLine());
        HashMap<String, Integer> map = new HashMap<>();

        for(int i=0; i<n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            String key = st.nextToken();
            int value = Integer.valueOf(st.nextToken());

//            System.out.println(String.format("key = %s / value = %d", key, value));
            if(map.containsKey(key)) {
                map.put(key, map.get(key) + value);
            } else {
                map.put(key, value);
            }
        }

//        System.out.println(map);
//        dic을 순회해서 4개의 과일중 정확히 5개인게 하나라도 있으면 yes break
        for(Integer value : map.values()) {
            if(value == 5) {
                System.out.println("YES");
                return;
            }
        }
        System.out.println("NO");
    }
}
