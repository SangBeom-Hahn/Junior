/*
팰린드롬 : 뒤에서부터 읽어도 똑같아.

ex) radar
12421

1. 모경수
1) 길이가 1이면 yes
2) 아니면 앞 idx, 뒤 idx로 쪼여옴
    1] 같으면 계속 반복
    2] 다르면 no
3) 앞 idx가 뒤 보다 커지면 yes

* 정수
마지막 0

출 : yes or no

2. n^3
 */

import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while(true) {
            String su = br.readLine();

            if(su.equals("0")) {
                break;
            }

            int leng = su.length();

            if(leng == 1) {
                System.out.println("yes");
            } else {
//                2) 아니면 앞 idx, 뒤 idx로 쪼여옴
    //                1] 같으면 계속 반복
    //                2] 다르면 no
//                3) 앞 idx가 뒤 보다 커지면 yes

                int frontIdx = 0;
                int backIdx = leng-1;

                while(true) {
                    if(frontIdx > backIdx) {
                        System.out.println("yes");
                        break;
                    }

                    if(su.charAt(frontIdx) == su.charAt(backIdx)) {
                        frontIdx += 1;
                        backIdx -= 1;
                    } else {
                        System.out.println("no");
                        break;
                    }
                }
            }

        }

    }
}
