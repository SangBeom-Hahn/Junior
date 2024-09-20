/*
nxm 직사각형 연구소, (빈칸, 벽)으로 이루어짐,
일부칸에 바이러스가 상하좌우로 인접한 빈칸으로 모두 퍼져나갈수있다.
벽을 새로 반드시 3개를 세워야한다.
벽을 3개 세운뒤, 바이러스가 퍼질 수 없는 곳을 안전영역이라고 한다.

1. 모경수(prt, n=1)
1) 지도의 모든 좌표를 하나의 배열에 저장
2) 모든 좌표를 크기 3짜리 조합 구함
3) 모든 조합을 순회
4) 하나의 조합으로 벽 세우고 바이러스가 퍼지도록 bfs
5) bfs 끝나고 0의 개수를 세고 최대값 갱신하고 지도 원상 복구

* n, m
지도의 상태(0, 1, 2 = 빈칸, 벽, 바이러스)
출 : 안전 영역 크기의 최대값

2. n^3

Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray()
Arrays.stream(graph).map(row -> Arrays.toString(row)).forEach(System.out::println);
System.out.println();
* */

import java.util.*;
import java.io.*;
import java.util.stream.Collectors;

public class Test {
    static List<int[]> coordi;
    static List<List<int[]>> combs = new ArrayList<>();
    static boolean[][] visit;
    static int[][] graph;
    static Queue<int[]> q;
    static int n;
    static int m;



    static void comb(int start, Stack<int[]> stack) {
        if(stack.size() == 3) {
            combs.add(new ArrayList<>(stack));
            return;
        }

        for(int i=start; i<coordi.size(); i++) {
            stack.add(coordi.get(i));
            comb(i+1, stack);
            stack.pop();
        }
    }

    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static int max = 0;

    static void bfs() {
        q = new LinkedList<>();
        for(int i=0; i<n; i++) {
            for(int j=0; j<m; j++) {
                if(graph[i][j] == 2) {
                    q.add(new int[] {i, j});
                }
            }
        }

        System.out.println(q);
        while(!q.isEmpty()) {
            int[] ele = q.remove();
            int x = ele[0];
            int y = ele[1];

            for(int i=0; i<4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if(nx < 0 || ny < 0 || nx >= n || ny >= m) {
                    continue;
                }

                if(!visit[nx][ny] && graph[nx][ny] == 0) {
                    visit[nx][ny] = true;
                    graph[nx][ny] = 2;
                    q.add(new int[] {nx, ny});
                }
            }
        }

        int cnt = 0;
        for(int i=0; i<n; i++) {
            for(int j=0; j<m; j++) {
                if(graph[i][j] == 0) {
                    cnt += 1;
                }
            }
        }

        max = Math.max(max, cnt);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        1) 지도의 모든 좌표를 하나의 배열에 저장
//        2) 모든 좌표를 크기 3짜리 조합 구함
        String[] input = br.readLine().split(" ");
        n = Integer.parseInt(input[0]);
        m = Integer.parseInt(input[1]);

        graph = new int[n][m];
        int[][] tmp = new int[n][m];


        for(int i=0; i<n; i++) {
            graph[i] = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        }
        for(int i=0; i<n; i++) {
            for(int j=0; j<m; j++) {
                tmp[i][j]=graph[i][j];
            }
        }
        // 바이러스 위치
        visit = new boolean[n][m];
        for(int i=0; i<n; i++) {
            for(int j=0; j<m; j++) {
                if(graph[i][j] == 2) {
                    visit[i][j] = true;
                }
            }
        }

        boolean[][] tmpVisit = new boolean[n][m];
        for(int i=0; i<n; i++) {
            for(int j=0; j<m; j++) {
                tmpVisit[i][j]=visit[i][j];
            }
        }

//        Arrays.stream(graph).map(row -> Arrays.toString(row)).forEach(System.out::println);

        coordi = new ArrayList<>();
        for(int i=0; i<n; i++) {
            for(int j=0; j<m; j++) {
                coordi.add(new int[] {i, j});
            }
        }

//        coordi.stream().map(row -> Arrays.toString(row)).forEach(System.out::println);
        Stack<int[]> stack = new Stack<>();
        comb(0, stack);
//        System.out.println(combs);
//        combs.stream().forEach(ele -> {
//            ele.stream().map(row -> Arrays.toString(row)).forEach(System.out::print);
//            System.out.println();
//        });

//        3) 모든 조합을 순회
//        4) 하나의 조합으로 벽 세우고 바이러스가 퍼지도록 bfs
//        5) bfs 끝나고 0의 개수를 세고 최대값 갱신하고 지도 원상 복구

        for(List<int[]> comb : combs) {
            for(int i=0; i<n; i++) {
                for(int j=0; j<m; j++) {
                    visit[i][j]=tmpVisit[i][j];
                }
            }

            for(int i=0; i<n; i++) {
                for (int j = 0; j < m; j++) {
                    graph[i][j] = tmp[i][j];
                }
            }

            // 벽 세움
            boolean notBlankFlag = false;
            for(int i=0; i<3; i++) {
                int[] cooldinate = comb.get(i);;
                int x = cooldinate[0];
                int y = cooldinate[1];

                // 벽이 아닌 곳에만 벽 세울 수 있음, 아니면 다음 조합 봄
                if(graph[x][y] != 0) {
                    notBlankFlag = true;
                    break;
                }

                graph[x][y] = 1;

//                System.out.print(x + " : " + y);
            }

            if(notBlankFlag == true) {
                continue;
            }

//            바이러스가 퍼지도록 bfs
            Arrays.stream(graph).map(row -> Arrays.toString(row)).forEach(System.out::println);
            bfs();

            int[] cooldinate1 = comb.get(0);;
            int x1 = cooldinate1[0];
            int y1 = cooldinate1[1];

            int[] cooldinate2 = comb.get(1);;
            int x2 = cooldinate2[0];
            int y2 = cooldinate2[1];

            int[] cooldinate3 = comb.get(2);;
            int x3 = cooldinate3[0];
            int y3 = cooldinate3[1];

//            if(x1 == 0 && y1 == 1 && x2 == 1 && y2 == 0 && x3 == 3 && y3 == 5) {
//                System.out.println();
//                Arrays.stream(graph).map(row -> Arrays.toString(row)).forEach(System.out::println);
//                break;
//            }

//            Arrays.stream(graph).map(row -> Arrays.toString(row)).forEach(System.out::println);
            System.out.println();


//                comb.stream().map(row -> Arrays.toString(row)).forEach(System.out::println);
//                break;

        }

        System.out.println(max);
    }




    static class Number implements Comparable<Number> {
        public int first;
        public int second;

        public Number(int first, int second) {
            this.first = first;
            this.second = second;
        }

        public int compareTo(Number n) {
            int b = Integer.compare(this.first, n.first);
            if (b != 0) {
                return b;
            } else {
                return Integer.compare(this.second, n.second);
            }
        }

        @Override
        public String toString() {
            return "Number{" +
                    "first=" + first +
                    ", second=" + second +
                    '}';
        }
    }

}
