/*
용량이 a, b, c 리터인 비커가 있다. 리터 d를 만들고 싶다.

조건 :
0] 1번에 1가지 행동만 가능
1] 비커 1개 변환
    1] 액체를 넘치지 않게 가득 채우기,
    2] 담긴 액체를 모두 버리기만 가능하다.
2] 비커끼리 액체를 이동시키기
    1] 넘치지 않게 완전 채우기
    2] 넘치치 않으면 지금 비커를 완전히 비우기

ex)
a   b   c / d = 1
3   5   7

a   b   c   연산
0   0   0
0   5   0   b에 가득 채우기
3   5   0   a에 가득

전체 c - 현재 c = 7 - 0 = 7
현재 a = 3

둘 중 작은 거 = 3을 c에는 더하고 a에는 빼고
0   5   3   a -> c

---

전체 c - 현재 c = 7 - 3 = 4
현재 b = 5

둘 중 작은 거 = 4를 c엔 더하고 b에는 빼고
0   1   7   b -> c


ex2)
a   b   c / d = 1
3   5   9

a   b   c
0   5   3

전체 c - 현재 c = 9 - 3 = 6
현재 b = 5

a   b   c
0   0   8

목표(전체) - 목표(현재) 와 소스(현재)의 최소값을 구함
목표엔 더하고 소스엔 뺌

1. 모경수
1) bfs로 방문 탐색
    1] a 가득 채우기
    b 가득 채우기
    c 가득 채우기
    a , b, c 비우기

    a -> b / b전체 - b현재 vs a현재의 최소값을 b에 더하고 a에 뺌
    a -> c / c전체 - c현재 vs a현재의 최소값을 c에 더하고 a에 뺌
    b -> a / a전체 - a현재 vs b현재의 최소값을 a에 더하고 b에 뺌
    b -> c / c전체 - c현재 vs b현재의 최소값을 c에 더하고 b에 뺌
    c -> a / a전체 - a현재 vs c현재의 최소값을 a에 더하고 c에 뺌
    c -> b / b전체 - b현재 vs c현재의 최소값을 b에 더하고 c에 뺌

    2] 상태는 set에 두고 상태에 없는 것만 큐에 넣는다.
    ok 3] 큐 = a, b, c상태, 횟수(0으로 시작)


* a, b, c의 용량
d : 만들어야 할 리터
출 : d리터를 만들기 위한 최소 횟수, 만들수 없다면 -1

2. n^3
 */

import java.util.*;
import java.io.*;

public class Main {
    private static int bfs(int totalA, int totalB, int totalC, int d) {
        Queue<int[]> q = new LinkedList<>();
        Set<List<Integer>> visit = new HashSet<>();
        q.offer(new int[] {0, 0, 0, 0});
        visit.add(Arrays.asList(0, 0, 0));

        int su = 1;
        while(!q.isEmpty()) {
//        while(su != 4) {
            q.stream().forEach(ele -> System.out.println(Arrays.toString(ele)));
            System.out.println();
            int[] currentL = q.poll();
            int currentA = currentL[0];
            int currentB = currentL[1];
            int currentC = currentL[2];
            int currentCount = currentL[3];

            if(currentA == d || currentB == d || currentC == d) {
                return currentCount;
            }

//            1] a 가득 채우기
//            b 가득 채우기
//            c 가득 채우기
//            a , b, c 비우기
//
//            a -> b / b전체 - b현재 vs a현재의 최소값을 b에 더하고 a에 뺌
//            a -> c / c전체 - c현재 vs a현재의 최소값을 c에 더하고 a에 뺌
//            b -> a / a전체 - a현재 vs b현재의 최소값을 a에 더하고 b에 뺌
//            b -> c / c전체 - c현재 vs b현재의 최소값을 c에 더하고 b에 뺌
//            c -> a / a전체 - a현재 vs c현재의 최소값을 a에 더하고 c에 뺌
//            c -> b / b전체 - b현재 vs c현재의 최소값을 b에 더하고 c에 뺌

            int[][] candidates = {
                    {totalA, currentB, currentC},
                    {currentA, totalB, currentC},
                    {currentA, currentB, totalC},
                    {0, currentB, currentC},
                    {currentA, 0, currentC},
                    {currentA, currentB, 0},
                    {currentA - Math.min(totalB - currentB, currentA), currentB + Math.min(totalB - currentB, currentA), currentC},
                    {currentA - Math.min(totalC - currentC, currentA), currentB, currentC + Math.min(totalC - currentC, currentA)},
                    {currentA + Math.min(totalA - currentA, currentB), currentB - Math.min(totalA - currentA, currentB), currentC},
                    {currentA, currentB - Math.min(totalC - currentC, currentB), currentC + Math.min(totalC - currentC, currentB)},
                    {currentA + Math.min(totalA - currentA, currentC), currentB, currentC - Math.min(totalA - currentA, currentC)},
                    {currentA, currentB + Math.min(totalB - currentB, currentC), currentC - Math.min(totalB - currentB, currentC)}
            };

            for(int[] candi : candidates) {
//                2] 상태는 set에 두고 상태에 없는 것만 큐에 넣는다.
                List<Integer> compare = List.of(candi[0], candi[1],candi[2]);
                if(!visit.contains(compare)) {
                    int[] newState = {candi[0], candi[1], candi[2], currentCount+1};
                    q.offer(newState);
                    visit.add(compare);
                }
            }

            su += 1;
        }

        return -1;
    }

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int a, b, c, d;

        StringTokenizer st = new StringTokenizer(br.readLine());
        a = Integer.parseInt(st.nextToken());
        b = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());
        d = Integer.parseInt(st.nextToken());

        //System.out.println(a + " " +  b + " " + c + " " + d);

        System.out.println(bfs(a, b, c, d));
    }
}
