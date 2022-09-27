package Main;
import java.util.*;

public class main2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int weight[][] = { //가중치 인접행렬
				{0, 9, 10, 0, 0, 0, 0},
				{9, 0, 0, 10,5, 0, 3},
				{10, 0, 0, 9, 7, 2, 0},
				{0, 10, 9, 0, 0, 4, 8},
				{0, 5, 7, 0, 0, 0, 1},
				{0, 0, 2, 4, 0, 0, 6},
				{0, 3, 0, 8, 1, 6, 0}
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
		
		KruskalMst k = new KruskalMst(adjList, M);
		System.out.print("최소신장트리 : ");
		int sum = 0;
		Edge2 tree[] = k.mst();
		for(int i=0; i<tree.length; i++) {
			sum+=tree[i].weight;
		}
		System.out.print(sum);
	}

}
