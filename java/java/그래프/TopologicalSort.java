package HSB;
import java.util.*;

public class TopologicalSort {
	int N;
	boolean visit[];
	List<Integer> graph[];
	List<Integer> seq;
	TopologicalSort(List<Integer> adjList[]){
		N = graph.length;
		graph = adjList;
		visit = new boolean[N];
		for(int i =0; i<N; i++) visit[i] = false;
		seq = new ArrayList<>();
	}
	public List<Integer> tSort(){
		for(int i = 0; i<N; i++) if(!visit[i]) dfs(i);
		Collections.reverse(seq);
		return seq;
	}
	public void dfs(int i) {
		visit[i] = true;
		for(int v : graph[i]) {
			if(!visit[v])
				dfs(v);
		}
		seq.add(i);
	}
}
