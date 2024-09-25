/*
nxn에 학생이 있다.
선생님 : 상하좌우 감시한다. 장애물 뒷편에 학생은 못봄, 장애물에 막히기 전까지는 다 
볼 수 있음
정확히 3개의 장애물을 설치한다. 모든 학생이 감시를 피할수있는지 출력하라

1. 모경수(prt, n=1)
1) x인 좌표를 배열에 모음
2) 길이 3인 조합을 구함
3) 조합을 순회
4) 하나의 조합으로 장애물을 설치하고 선생님 상하좌우 감시 -> 감시 구역은 visit true
5) 학생의 좌표가 전부 다 visit false이면 yes 하고 끝
6) 아니면 다음 조합 봄
7) 모든 조합 봤는데 yes 안됐으면 no

* n : nxn
복도정보 (s, t, x) = 학생, 선생님, 아무것도 없음
출 : 모든 학생이 감시로부터 피하도록 할 수 있는지 여부를 출력 yes no

2. n^3

System.out.println();
Arrays.stream(graph).map(row -> Arrays.toString(row)).forEach(System.out::println);
* */

import java.util.*;
import java.io.*;
import java.util.stream.Collectors;

public class Main {
    static List<Ele> cooldis;
    static List<List<Ele>> combs = new ArrayList<>();
    static boolean[][] visit;
    static char[][] graph;
    static int n;

    static void dfsUp(int x, int y) {
        visit[x][y] = true;

        int nx = x-1;
        if(nx < 0 || graph[nx][y] == 'O') {
            return;
        } else {
            dfsUp(nx, y);
        }
    }

    static void dfsDown(int x, int y) {
        visit[x][y] = true;

        int nx = x+1;
        if(nx >= n || graph[nx][y] == 'O') {
            return;
        } else {
            dfsDown(nx, y);
        }
    }

    static void dfsL(int x, int y) {
        visit[x][y] = true;

        int ny = y-1;
        if(ny < 0 || graph[x][ny] == 'O') {
            return;
        } else {
            dfsL(x, ny);
        }
    }

    static void dfsR(int x, int y) {
        visit[x][y] = true;

        int ny = y+1;
        if(ny >= n || graph[x][ny] == 'O') {
            return;
        } else {
            dfsR(x, ny);
        }
    }

//    장애물 설치 위치를 배열을 조합을 길이 3으로 구함
    static void comb(Stack<Ele> st, int start) {
        if(st.size() == 3) {
            combs.add(new ArrayList<>(st));
        }


        for(int i=start; i<cooldis.size(); i++){
//            System.out.println(st);
            Ele cooldi = cooldis.get(i);
            st.add(new Ele(cooldi.x, cooldi.y));
            comb(st, i+1);
            st.pop();
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());

        graph = new char[n][n];
        char[][] tempGraph = new char[n][n];
        visit = new boolean[n][n];
        boolean[][] tempVisit = new boolean[n][n];

        for(int i=0; i<n ; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            for(int j=0; j<n; j++) {
                graph[i][j] = st.nextToken().charAt(0);
            }
        }
        List<Ele> teachers = new ArrayList<>();
        List<Ele> stus = new ArrayList<>();
        for(int i=0; i<n ; i++) {
            for(int j=0; j<n; j++) {
                if(graph[i][j] == 'T') {
                    teachers.add(new Ele(i, j));
                }
                if(graph[i][j] == 'S') {
                    stus.add(new Ele(i, j));
                }
            }
        }
        for(int i=0; i<n ; i++) {
            for(int j=0; j<n; j++) {
                tempGraph[i][j] = graph[i][j];
            }
        }

//        Arrays.stream(graph).map(row -> Arrays.toString(row)).forEach(System.out::println);
//        그래프가 장애물일 경우에만 좌표를 구해서 배열에 넣음

        cooldis = new ArrayList<>();
        for(int i = 0; i<n; i++) {
            for(int j=0; j<n; j++) {
                if(graph[i][j] == 'X') {
                    cooldis.add(new Ele(i, j));
                }
            }
        }

//        System.out.println(cooldis);
        comb(new Stack<>(), 0);
//        List<List<Ele>> combs;
//        System.out.println(combs.get(0));

//        4) 모든 조합을 순회함
//        7) 그런 경우가 있다면 yes하고 끝냄(main에서 return), 없으면 no

//        List<List<Ele>> combs = List.of(
//                List.of(new Ele(0, 0), new Ele(0, 2), new Ele(0, 3)),
//                List.of(new Ele(0, 3), new Ele(1, 1), new Ele(2, 2))
//        );
        for(List<Ele> comb : combs) {
            boolean allFalseFalge = true;
            // 5) 각 조합에서 설치를 하고 선생님들 모두를 각각 상하좌우로 dfs를 돌림
            for(Ele ele : comb) {
                graph[ele.x][ele.y] = 'O';
            }

            for(Ele ele : teachers) {
                dfsUp(ele.x, ele.y);
                dfsDown(ele.x, ele.y);
                dfsL(ele.x, ele.y);
                dfsR(ele.x, ele.y);
            }

//        6) 모든 선생님이 다 보고 나서 학생들의 위치가 visit이 전부 다 false인 경우가
//        모두 감시를 피한 경우임
//            System.out.println(stus);
//            Arrays.stream(visit).map(row -> Arrays.toString(row)).forEach(System.out::println);
            for(Ele ele : stus) {
                if(visit[ele.x][ele.y] == true) {
                    allFalseFalge = false;
                    break;
                }
            }

            if(allFalseFalge == true) {
//                그런 경우가 있다면 yes하고 끝냄(main에서 return), 없으면 no
                System.out.println("YES");
                return;
            }


//            Arrays.stream(graph).map(row -> Arrays.toString(row)).forEach(System.out::println);
//            Arrays.stream(visit).map(row -> Arrays.toString(row)).forEach(System.out::println);
//            System.out.println();

            for(int i=0; i<n ; i++) {
                for(int j=0; j<n; j++) {
                    graph[i][j] = tempGraph[i][j];
                    visit[i][j] = tempVisit[i][j];
                }
            }
        }
        System.out.println("NO");
    }
}

class Ele {
    int x;
    int y;

    public Ele(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public String toString() {
        return String.format("[%d, %d]", x, y);
    }
}