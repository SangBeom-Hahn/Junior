package Main;
import java.util.*;

public class main2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int weight[][] = { //가중치 인접행렬
				{0, 1, 0, 2, 0, 0, 0, 0},
				{1, 0, 4, 3, 1, 6, 0, 0},
				{0, 4, 0, 0, 0, 1, 1, 2},
				{2, 3, 0, 0, 5, 0, 0, 0},
				{0, 1, 0, 5, 0, 0, 2, 0},
				{0, 6, 1, 0, 0, 0, 0, 9},
				{0, 0, 1, 0, 2, 0, 0, 1},
				{0, 0, 2, 0, 0, 9, 1, 0}
		};
		int N = weight.length;
		int M = 0;
		List<Edge2> adjList[] = new List[N];
		for(int i = 0; i<N; i++) {
			adjList[i] = new LinkedList<>();
			for(int j=0; j<N; j++) {
				if(weight[i][j] != 0) {
					Edge2 e = new Edge2(i, j, weight[i][j]);
					adjList[i].add(e);
					M++;
				}
			}
		}
		Dik d = new Dik(adjList, 0);
		int dis[] = d.algo();
		for(int i = 0; i<dis.length; i++) {
			System.out.println(dis[i]);
		}
		
	}

}
