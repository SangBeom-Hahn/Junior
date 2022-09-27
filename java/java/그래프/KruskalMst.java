package Main;
import java.util.*;

public class KruskalMst {
	int M;
	int N;
	Edge2 tree[];
	List<Edge2> graph[];
	KruskalMst(List<Edge2> adjList[], int M){
		graph = adjList;
		this.M = M;
		N = graph.length;
		tree = new Edge2[N-1];
	}
	class Com implements Comparator<Edge2>{
		@Override
		public int compare(Edge2 o1, Edge2 o2) {
			// TODO Auto-generated method stub
			if(o1.weight > o2.weight)
				return 1;
			else
				return -1;
		}
	}
	public Edge2[] mst() {
		Com c = new Com();
		UnionFind uf = new UnionFind(N);
		PriorityQueue<Edge2> pq = new PriorityQueue<Edge2>(M, c);
		for(int i=0; i<N; i++)
			for(Edge2 e : graph[i])
				pq.add(e);
		
		int count = 0;
		while(!pq.isEmpty() && count < N-1) {
			Edge2 realE = pq.poll();
			if(!uf.connect(realE.vertax, realE.adjVertax)) {
				uf.union(realE.vertax, realE.adjVertax);
				tree[count++] = realE;
				
			}
		}
		return tree;
	}
}
