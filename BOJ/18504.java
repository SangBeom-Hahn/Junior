/*
nxn 크기의 시험관이있다. 바이러스는 1~K번까지의 종류 중 하나이다.
1) 존재하는 모든 바이러스는 1초마다 증식함, 단 매초마다 번호가 낮은 종류부터 먼저 증식함
2) 이미 바이러스가 존재하는 칸은 다른 바이러스가 갈 수 없음

1. 모경수(prt, n=1)
1) 바이러스를 미리 큐에 넣어놓음
2) bfs로 s번 돌림
3) s초 일때 x-1, y-1자리를 구함

* n, k : nxn, 1 ~ k번까지의 바이러스 종류
시험관 정보
s, x, y

출: s초가 지난 후 x-1, y-1에 있는 바이러스의 종류를 구하라(없다면 0)
2. nlogn


System.out.println();
Arrays.stream(graph).map(row -> Arrays.toString(row)).forEach(System.out::println);
* */

import java.util.*;
import java.io.*;
import java.util.stream.Collectors;

public class Main {
    static Queue<int[]> q;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static int[][] graph;
    static boolean[][] visit;
    static int s;
    static int n;

    //    bfs로 s번 돌림
    static int bfs(int rx, int ry) {
        while(!q.isEmpty()) {
//            Arrays.stream(graph).map(row -> Arrays.toString(row)).forEach(System.out::println);

            int[] ele = q.remove();
            int x = ele[0];
            int y = ele[1];
            int time = ele[2];
//            System.out.println(time);

            if(time == s) {
                return graph[rx-1][ry-1];
            }

            for(int i=0; i<4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if(nx < 0 || ny < 0 || nx >= n || ny >= n) {
                    continue;
                }

                if(!visit[nx][ny] && graph[nx][ny] == 0) {
                    visit[nx][ny] = true;
                    graph[nx][ny] = graph[x][y];
                    q.add(new int[] {nx, ny, time+1});
                }
            }
        }
        return graph[rx-1][ry-1];
    }

    public static void main(String[] args) throws IOException {
//        바이러스를 미리 큐에 넣어놓음
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        graph = new int[n][n];
        visit = new boolean[n][n];
        for(int i=0; i<n; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            for(int j=0; j<n; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        st = new StringTokenizer(br.readLine(), " ");
        s = Integer.parseInt(st.nextToken());
        int x = Integer.parseInt(st.nextToken());
        int y = Integer.parseInt(st.nextToken());
        q = new LinkedList<>();
        for(int p=1; p<=k; p++) {
            for(int i=0; i<n; i++) {

                for(int j=0; j<n; j++) {
                    if(graph[i][j] == p) {
                        q.add(new int[] {i, j, 0}); // 좌표, 시간
                        visit[i][j] = true;
                    }
                }
            }
        }
        System.out.println(bfs(x, y));
//        q.stream().map(row -> Arrays.toString(row)).forEach(System.out::println);
    }
}