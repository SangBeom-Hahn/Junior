/*
* 자연수 n, k가 주어졌을 때 n의 약수들 중 k번째 수
*
*
*
* 1. 모경수
* 1) 1 ~ n // 2 + 1 까지 수 중에서 n과 나눠서 떨어지는 수를 List에 저장함
* 2) 맨 마지막에 n도 추가함
* 3) 인덱스 k-1 번째 수 구함
*
* * n, k
* 출 : n의 약수 중 k번째로 작은 수(n의 약수의 개수가 k개보다 적으면 0 출력)
*
* 2. nlogn
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
        String[] inputs = br.readLine().split(" ");
        int n = Integer.valueOf(inputs[0]);
        int k = Integer.valueOf(inputs[1]);

//        System.out.println(n + " " + k);
        List<Integer> list = new ArrayList<>();

//        1) 1 ~ n // 2 + 1 까지 수 중에서 n과 나눠서 떨어지는 수를 List에 저장함
        for(int i=1; i< n/2+1; i++) {
            if(n % i == 0) {
                list.add(i);
            }
        }

//        맨 마지막에 n도 추가함
        list.add(n);

//        System.out.println(list);

//        인덱스 k-1 번째 수 구함
        if(list.size() < k) {
            System.out.println(0);
        } else {
            System.out.println(list.get(k-1));
        }
    }
}
