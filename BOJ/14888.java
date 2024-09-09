/*
n개의 수, 수와수 사이에 끼워넣을 n-1개의 연산자가 있다. 4종류(덧, 뺄, 곱, 나)
수식 : 수와 수 사이에 연산자를 하나씩 넣어서 수식을 만들 수 있다. 수의 순서를 바꾸면 안 됨
계산 :
1) 은 우선 순위를 무시하고 앞에서부터 진행한다.
2) 나눗셈은 정수 나눗셈으로 몫만 취함
3) 음수를 양수로 나눌 때는 양수로 바꾼 뒤 몫을 구하고 몫을 음수로 바꾼다.

ex) 수 1 2 3 4 5 6 / 연산자 +, +, -, *, % 인 경우 5 4 3 2 1 / 2 = 60가지 수

1. 모경수(prt, n=1)
1) 백으로 탐색
2) 연사자 배열을 만듬
2) 계속 값을 계산함, 길이가 n일 때 break

* N : 수의 개수
수의 개수만큼의 수
합이 N-1인 4개의 정수 : +, -, x, %의 개수

출 : 식의 결과 최대, 최소
2. n^3
* */

import java.util.*;
import java.io.*;
import java.util.stream.Collectors;

/*
* System.out.println()
* */



public class Main {
    /*
     * 1 + 2 = 3
     * 3 + 3
     *
     * 처음에 숫자 인덱스 0을 결과에 넣음
     * 계속 값 계산 = 결과 calc[i] nums[i+1]
     * 인덱스가 n-1과 같으면 결과 갱신 break
     * */

    static int max = -1000000001;
    static int min = 1000000001;

    public static void back(int idx, int leng, boolean[] used, int semi_result, List<String> cals, int[] nums) {
        if(idx == leng) {
//            System.out.println(semi_result);
            min = Math.min(min, semi_result);
            max = Math.max(max, semi_result);

            return;
        }


        for(int i=0; i<leng; i++) { // 백에서 요소 끝까지 보기 위함임
            if(used[i] == false) { // 아직 사용 안했으면
                used[i] = true;

                if(cals.get(i).equals("+")) {
                    semi_result += nums[idx+1];
                    back(idx+1, leng, used, semi_result, cals, nums);
                    semi_result -= nums[idx+1];
                } else if(cals.get(i).equals("-")) {
                    semi_result -= nums[idx+1];
                    back(idx+1, leng, used, semi_result, cals, nums);
                    semi_result += nums[idx+1];
                } else if(cals.get(i).equals("*")) {
                    semi_result *= nums[idx+1];
                    back(idx+1, leng, used, semi_result, cals, nums);
                    semi_result /= nums[idx+1];
                } else if(cals.get(i).equals("/")) {
                    if(semi_result < 0) {
                        semi_result *= -1;
                        semi_result /= nums[idx+1];
                        semi_result *= -1;
                        back(idx+1, leng, used, semi_result, cals, nums);
                        semi_result *= -1;
                        semi_result *= nums[idx+1];
                        semi_result *= -1;
                    } else {
                        semi_result /= nums[idx+1];
                        back(idx+1, leng, used, semi_result, cals, nums);
                        semi_result *= nums[idx+1];
                    }
                }

                used[i] = false;
            }
        }
    }

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        String[] input = br.readLine().split(" ");
        String[] input2 = br.readLine().split(" ");

        int[] nums = Arrays.stream(input).mapToInt(Integer::parseInt).toArray();
        int[] calCnt = Arrays.stream(input2).mapToInt(Integer::parseInt).toArray();

//        연사자 배열을 만듬
        String[] calType = {"+", "-", "*", "/"};
        List<String> cals = new ArrayList<>();

        for(int i=0; i<4; i++) {
            for(int j=0; j<calCnt[i]; j++) {
                cals.add(calType[i]);
            }
        }

//        System.out.println(cals);

        /*
        * 1 + 2 = 3
        * 3 + 3
        *
        * 처음에 숫자 인덱스 0을 결과에 넣음
        * 계속 값 계산 = 결과 calc[i] nums[i+1]
        * 인덱스가 n-1과 같으면 결과 갱신 break
        * */
        int semi_result = nums[0];
        boolean[] used = new boolean[n-1];
        back(0, n-1, used, semi_result, cals, nums);

        System.out.println(max);
        System.out.println(min);
    }
}
