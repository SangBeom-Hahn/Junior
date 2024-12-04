/*
집합 a, b : 자연수를 원소로 가지는 공집합이 아닌 집합
대칭 차집합 : A-b와 b-a의 합집합

1. 모경수(prt, n=1)
1) a를 순회하며 b에 속하는게 있으면 a의 개수 -1, b의 개수 -1

* A의 원소, B 원소 개수
a의 모든 원소
b의 모든 원소
출 : 대칭차집합의 원소의 개수

2. nlogn
 */

import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int a_cnt = Integer.parseInt(st.nextToken());
        int b_cnt = Integer.parseInt(st.nextToken());
        HashSet<Integer> a = new HashSet<>();
        HashSet<Integer> b = new HashSet<>();

        st = new StringTokenizer(br.readLine());
        for(int i=0; i<a_cnt; i++) {
            a.add(Integer.parseInt(st.nextToken()));
        }

        st = new StringTokenizer(br.readLine());
        for(int i=0; i<b_cnt; i++) {
            b.add(Integer.parseInt(st.nextToken()));
        }

        for(Integer ele : a) {
            if(b.contains(ele)) {
                a_cnt -= 1;
                b_cnt -= 1;
            }
        }

        System.out.println(a_cnt+b_cnt);
    }
}
