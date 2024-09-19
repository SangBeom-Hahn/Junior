/*
1. 레이저 : 여 괄호 + 닫 괄호 인접 쌍, 모든 ()는 레이저다.
2. 막대 : ( + )

막대는 레이저에 의해 조각으로 잘린다.

ex) ()
선택      스택              총 조각
(       (
)       팝                   0

()()
선택      스택              총 조각
(       (
)       팝 -> 레이저의 팝은 결과에 영향 없음
(       (
)       팝                   0

(())
선택      스택                                      총 조각
(       (
(       ( ( -> 열 괄호면 푸시
)       팝 ( -> 레이저의 팝은 결과에 영향 없음(선택의 하나 앞이 열괄호면 레이저)
)       팝 -> 레이저가 아니면 결과에 반영            2 (레이저 팝은 헤더(0)에 + 1, 레이저 아닌 팝은 결과에 현재팝값(1) + 1을 더하나?)

(레이저 팝은 헤더(0)에 + 1, 레이저 아닌 팝은 결과에 현재팝값(1) + 1을 더하나?)
레이저 팝으로 현재 헤더가 1이되고, 레이저 아닌 팝에 현재 팝값이 1이니 1 더해서 최종 결과 2??

(()()) = 결과 3
선택      스택                                      총 조각
(       0
(       0 0
)       팝 1 -> 레이저=헤더에만 + 1
(       1 0
)       팝 2 -> 레이저=헤더에만 + 1
)       팝 -> 레이저x = 2+1 = 3



((())) = 결과 4
선택      스택                                      총 조각
(       0
(       0 0
(       0 0 0
)       팝 0 1 -> 레이저=헤더에만 + 1
)       팝 0 -> 레이저x = 결과에 + (1+1)           2
)       팝 -> 레이저x = 결과에 + (0+1)             3
         ↓
((()())(())) = 5 + 4 = 9
선택      스택                                      총 조각
(       0
(       0 0
(       0 0 0
)       팝 0 1 -> 레이저=헤더에만 + 1
(       0 1 0
)       팝 0 2 -> 레이저=헤더에만 + 1
)       팝 2 -> 레이저x=헤드에 팝값(2) / 결과에 팝값+1(3)     3
(       2 0
(       2 0 0
)       팝 2 1 -> 레이저=헤더에만 + 1
)       팝 3 -> 레이저x=헤드에 팝값(1) / 결과에 팝값+1(2)     3+2
)       팝 -> 결과에 팝값+1(4)                            3+2+4 = 9

1. 모경수 (prt, n=1)
1) 레이저 팝은 헤더에 + 1, 레이저 아닌 팝은 결과에 현재팝 + 1을 더하고, 헤더에 팝값 더함
2) 헤더에 더할 때 스택이 비었으면 안 더함

* 괄호 표현 : 
출 : 잘려진 조각의 총 개수

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
        String galho = br.readLine();

// 1) 레이저 팝은 헤더에 + 1, 레이저 아닌 팝은 결과에 현재팝 + 1을 더하고, 헤더에 팝값 더함
// 2) 헤더에 더할 때 스택이 비었으면 안 더함
        Stack<Integer> st = new Stack<>();
        int result = 0;
        for(int i=0; i<galho.length(); i++) {
            if(galho.charAt(i) == '(') {
                st.push(0);
            }
            // 닫 갈호이면
            else {
                // 레이저면
                if(galho.charAt(i-1) == '(') {
                    st.pop();
                    if(!st.isEmpty()) {
                        int head = st.pop();
                        st.push(head + 1);
                    }
                }
                else {
                    int ele = st.pop();
                    result += (ele+1);
                    if(!st.isEmpty()) {
                        int head = st.pop();
                        st.push(head + ele);
                    }
                }
            }
        }
        System.out.println(result);
    }
}








