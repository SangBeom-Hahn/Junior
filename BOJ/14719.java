/*
비가 고이는 총량을 얼마일까?

ex)

ㅡㅡㅡㅡ
ㅁ  ㅁㅁ 0
ㅁ    ㅁ 1
ㅁ    ㅁ 2
      ㅁ 3

ㅡㅡㅡㅡㅡㅡㅡㅡ
ㅁㅁㅁㅁㅁㅁㅁㅁ 0
ㅁ  ㅁㅁㅁ   ㅁ 1
ㅁ    ㅁㅁ     2
       ㅁ      3


1. 모경수(prt, n=1)
-> 머리가 풀리면 이렇게
1) 0행 ~ w-1행까지 봄   의 양쪽이 막혀있나 봄 0열, w-1열
2) 0행 : 첫 블록과 다음 블록을 flag를 둬서 첫 블록이 나왔을 때 다음 블록 나올때까지 블록이
아닌 부분의 개수를 셈
3) 첫블록만 나오거나 블록이 하나도 안 나오면 개수를 세지 않음
4) 첫블럭과 닫블럭이 나오면 닫블럭을 첫블록으로 보고 닫블럭을 다시 찾을 때까지 블록이 아닌
곳의 개수를 셈

현재행     블록
0           2 -1 0 3 -> 첫, 블록 아님, 끝(이젠 얘가 첫), 끝 = 블록 아닌거의 개수 1개
1           2 -1 0 3 -> 첫, 블록 아님, 블록 아님, 끝 = 블록 아닌 거의 개수 2개
2           첫, 아님, 아님, 끝 = 2개
3           아님, 아님, 아님, 첫 = 0개

0행          2 0 1 2 3 0 0 1 -> 첫, 끝, 첫, 끝 ,,,, = 블록 아닌거 개수 0개
1행          첫, 아님, 끝(이제 얘가 첫) 끝(첫) 끝(첫), 아님, 아님, 끝 = 3개
2행          첫, 아님, 아님, 끝(첫), 끝(첫), 아님 아님 아님 = 2개

5) 블록인지 아닌지 보는 법
    1] 입력 블록을 다 -1씩 함
    2]  0행 ~ w-1까지 함
    3] 현재 행보다 크거나 같으면 블록임, 작으면 블록이 없는 거임

-> 머리가 나쁜 버전
1)

->
1) 0행 ~ w-1행까지 봄
2) 0행 : 첫 블록과 다음 블록을 flag를 둬서 첫 블록이 나왔을 때 다음 블록 나올때까지 블록이
아닌 부분의 개수를 셈
    1] 입력 블록을 다 -1씩 함
    2]  0행 ~ w-1까지 함
    3] 현재 행보다 크거나 같으면 블록임, 작으면 블록이 없는 거임
3) 첫블록만 나오거나 블록이 하나도 안 나오면 개수를 세지 않음
4) 첫블럭과 닫블럭이 나오면 닫블럭을 첫블록으로 보고 닫블럭을 다시 찾을 때까지 블록이 아닌
곳의 개수를 셈

* 세로, 가로 길이 H, W
블록 높이가 왼쪽부터 0이상 H이하 (바닥은 항상 막혀있음)

출 : 한칸 용량이 1일때 고이는 빗물의 총량을 구하라(고이지 않으면 0)
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


        String[] input1 = br.readLine().split(" ");
        String[] input2 = br.readLine().split(" ");

        int h = Integer.parseInt(input1[0]);
        int w = Integer.parseInt(input1[1]);
        int[] heightss = Arrays.stream(input2).mapToInt(Integer::parseInt).toArray();
        int[] heights = Arrays.stream(heightss).map(x -> x - 1).toArray();

        int result = 0;
        //1) 0행 ~ w-1행까지 봄
//        2) 0행 : 첫 블록과 다음 블록을 flag를 둬서 첫 블록이 나왔을 때 다음 블록 나올때까지 블록이
//        아닌 부분의 개수를 셈
        //        1] 입력 블록을 다 -1씩 함
        //        2]  0행 ~ w-1까지 함
        //        3] 현재 행보다 크거나 같으면 블록임, 작으면 블록이 없는 거임
//        3) 첫블록만 나오거나 블록이 하나도 안 나오면 개수를 세지 않음
//        4) 첫블럭과 닫블럭이 나오면 닫블럭을 첫블록으로 보고 닫블럭을 다시 찾을 때까지 블록이 아닌
//        곳의 개수를 셈

        for(int i=0; i<h; i++) {
            boolean firstFlag = false; // 아직 블록이 없었다는 의미
            int cnt = 0;
            for(int j=0; j<w; j++) {
                if(firstFlag == false) { // 첫 블록을 안 봣으면 cnt를 셀 이유도 없음
                    if(heights[j] >= i) {
                        firstFlag = true;
                        continue;
                    }
                }

                if(firstFlag == true) { // 블록을 본 상태
                    if(heights[j] >= i) { // 블록을 봤는데 또 블록이 나오면
                        firstFlag = true; // 얘가 이제 첫 블록이고
                        result += cnt; // 결과에 반영
                        cnt = 0;
                        continue;
                    } else { // 블록을 봤는데 현재가 블록이 아니면 빈 공간
                        cnt += 1;
                    }
                }
//                System.out.println("행 : " + i + " 열 : " + j + " " + cnt + " " +result);
            }
//            System.out.println("행 : " + i + " " + cnt + " " +result);
        }

        System.out.println(result);
    }
}
