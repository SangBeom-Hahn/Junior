/*
N개의 높이가 다른 탑을 왼쪽부터 오른쪽으로 차례로 세우고
레이저 송신기는 레이저 신호를 왼쪽으로 발사한다.
기둥에는 레이저 신호 수신장치가 있다.
레이저 신호는 가장 먼저 만나는 단 하나의 탑에서만 수신이 가능하다.

ex) 6 9 5 7 4
수신      송신
7           4
9           7
9           5
0           9
0           6

탑       스택
4       4 -> 스택이 비어있으면 넣음(높이, 인덱스)
7       팝 -> 현재 탑 > 스택 헤드 팝, 스택에서 팝한 것의 인덱스에 현재 탑 인덱스 저장
7       7 -> 스택이 비면 넣음
5       75 -> 현재 탑 < 스택 헤드, 넣음
9       팝 = 7 -> 현재 탑 > 스택 헤드 팝,
9       팝 = [] -> 현재 탑 > 스택 헤드 팝,
9       9 -> 스택이 비면 넣음
6       96 -> while 조건 : 스택이 빌때까지?? ㄴㄴ 현재 탑을 바라보는 인덱스가 -1이 아닐동안

1. 모경수(prt, n=1)
1) while 조건 : 현재 탑을 바라보는 인덱스가 -1이 아닐동안
2) 현재 탑 > 스택 헤드 팝, 스택에서 팝한 것의 인덱스에 현재 탑 인덱스 저장
3) 스택이 비어있으면 넣음(높이, 인덱스)
4) 현재 탑 < 스택 헤드, 넣음


* n : 탑의 개수
탑들의 높이
출 : 각 탑에서 발사한 레이저 신호를 어떤 탑에서 수신하는지 구하라

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
        int n = Integer.parseInt(br.readLine());
        String[] input = br.readLine().split(" ");
        int[] tops = Arrays.stream(input).mapToInt(Integer::parseInt).toArray();

//        1) while 조건 : 현재 탑을 바라보는 인덱스가 -1이 아닐동안
//        2) 현재 탑 > 스택 헤드 팝, 스택에서 팝한 것의 인덱스에 현재 탑 인덱스 저장
//        3) 스택이 비어있으면 넣음(높이, 인덱스)
//        4) 현재 탑 < 스택 헤드, 넣음
        int[] result = new int[n];

        Stack<Ele> stack = new Stack<>();
        for(int i=n-1; i>-1; i--) {
            while(!stack.isEmpty() && tops[i] > stack.peek().value) {
                Ele ele = stack.pop();
                result[ele.idx] = i+1;
            }

            stack.push(new Ele(tops[i], i));
        }

        for(Integer ele : result) {
            System.out.print(ele + " ");
        }
    }
}

class Ele {
    public int value;
    public int idx;

    public Ele(int value, int idx) {
        this.value = value;
        this.idx = idx;
    }
}






