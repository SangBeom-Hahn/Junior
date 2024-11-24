/*
구분자 : 문자열을 나누는 기준
병합자 : 구분자에서 제외하는 조건
규칙 :
1) 문자열을 공백과 구분자들로 나눔
2) 문자 구분자 = 영어 대소문자 중 하나
3) 숫자 구분자 0~9

ex) abcdefg 1234
구분자 b -> a / cdefg 1234
구분자 공백 -> a / cdefg / 1234
구분자 3 -> a / cdefg / 12 / 4

flag        기준 문자열      sb
f           a               a
t           b               a\
f           c               a\c
t           d               a\cd
            e
            f
            g               a\cdefg
            ' '             a\cdefg\
f           1               a\cdefg\1

abbbefg 1234

flag        기준 문자열      sb
f           a               a
t           b               a\
f           b

ex) a372bcdefg 1234
구분자 b -> a372 / cdefg 1234
구분자 3 -> a / 72 / cdefg12 / 4

1. 모경수(prt, n=1)
0) 문자 구분자와 숫자 구분자를 하나로 모으고 병합자 순회해서 구분자 셋에서 제거
1) 기준 문자열 순회
    1] 구분자가 아니면 추가
        1] 구분자가 아닌 문자열이 들어와서 1번이라도 출력이 되면 flag t로 해서 내려도 됨을 명시
    2] 구분자이면
        1) 역슬레시가 들어갈거냐 말거냐의 flag
        2) 구분자라서 \n을 넣었다면 무조건 false로 만들어서 다음에 구분자가 들어와도 \n 안하게 만듬

* n : 문자 구분자의 개수
n개의 문자 구분자
m : 숫자 구분자 개수
m개 숫자 구분자
k : 병합자의 개수
k개의 병합자
s : 기준 문자열 길이
기준 문자열

출 : 적용 결과 (문자, 숫자, 공백으로 나눈 거 각 단어 출력)

2. nlogn
*/

import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        HashSet<Character> set = new HashSet<>();

//        0) 문자 구분자와 숫자 구분자를 하나로 모으고 병합자 순회해서 구분자 셋에서 제거
        int n = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        for(int i=0; i<n; i++) {
            set.add(st.nextToken().charAt(0));
        }

        int m = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        for(int i=0; i<m; i++) {
            set.add(st.nextToken().charAt(0));
        }

        int k = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        for(int i=0; i<k; i++) {
            Character ele = st.nextToken().charAt(0);
            if(set.contains(ele)) {
                set.remove(ele);
            }
        }

//        System.out.println(set);

//        1) 기준 문자열 순회
//        1] 구분자가 아니면 추가
//          1 ] 구분자가 아닌 문자열이 들어와서 1번이라도 출력이 되면 flag t로 해서 내려도 됨을 명시
//        2] 구분자이면
    //        1) 역슬레시가 들어갈거냐 말거냐의 flag
    //        2) 구분자라서 \n을 넣었다면 무조건 false로 만들어서 다음에 구분자가 들어와도 \n 안하게 만듬

        int s = Integer.parseInt(br.readLine());
        String str = br.readLine();
        StringBuilder sb = new StringBuilder();
        boolean flag = false;
        for(Character ele : str.toCharArray()) {
            if(!set.contains(ele) && !ele.equals(' ')) {
                sb.append(ele);
                flag = true;
            } else {
                if(flag == true) {
                    sb.append("\n");
                    flag = false;
                }
            }
        }

        System.out.println(sb);
    }
}
