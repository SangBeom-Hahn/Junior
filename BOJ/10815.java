/*
숫자 카드 : 정수 하나
상근이 : 숫자카드 n개 가짐

1. 모경수(prt, nn=1
1) n개의 수를 set으로 관리
2) m개의 수를 순회
3) 속하면 1, 아니면 0

* n : 상근이가 가지고 있는 숫자 카드 개수
숫자 카드 번호 n개
m :
m개의 정수
출 : m개의 수에 대해서 각 수가 상근이가 가지고 있으면 1, 아니면 0

2. n
 */

import java.util.*;
import java.io.*;
//1) n개의 수를 set으로 관리
//        2) m개의 수를 순회
//        3) 속하면 1, 아니면 0
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        HashSet<Integer> set = new HashSet<>();
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i=0; i<n; i++) {
            set.add(Integer.valueOf(st.nextToken()));
        }

        int m = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());

        for(int i=0; i<m; i++) {
            int ele = Integer.valueOf(st.nextToken());
            if(set.contains(ele)) {
                System.out.print(1 + " ");
            } else {
                System.out.print(0 + " ");
            }
        }
    }
}
