package HSB;
import java.util.*;

public class SCC {
	int N;
	boolean sig[];
	List<Integer> graph[];
	boolean visit[];
	List<Integer> seq;
	List<Integer> revSeq;
	SCC(){
		sig =new boolean[N];
		graph = map();
		
		seq = new ArrayList<>();
		revSeq = new ArrayList<>();
		visit = new boolean[N];
		N = graph.length;
		System.out.print(N);
		for(int i=0; i<N; i++) {
			visit[i] = false;
			sig[i] = false;
		}
		revSeq = tSort();
	}
	//¸Þ¼Òµå
	public List<Integer>[] map(){
		List<Integer> adjList[] = new List[9];
		adjList[0] = new LinkedList<>();
		adjList[0].add(7);
		
		adjList[1] = new LinkedList<>();
		adjList[1].add(8);
		
		adjList[2] = new LinkedList<>();
		adjList[2].add(5);
		
		adjList[3] = new LinkedList<>();
		adjList[3].add(4); adjList[3].add(8); adjList[3].add(1);
		
		adjList[4] = new LinkedList<>();
		adjList[4].add(2); adjList[4].add(5);
		
		adjList[5] = new LinkedList<>();
		adjList[5].add(3);
		
		adjList[6] = new LinkedList<>();
		adjList[6].add(0); adjList[6].add(4);

		adjList[7] = new LinkedList<>();
		adjList[7].add(2); adjList[7].add(6);
		
		adjList[8] = new LinkedList<>();
		adjList[8].add(1); 
		return adjList;
	}
	public List<Integer>[] revMap() {
		List<Integer> SccGraph[] = new List[N];
		for(int i = 0; i<N; i++) {
			for(int v : graph[i]) {
				if(sig[v] == false) {
					SccGraph[v] = new LinkedList<>();
					sig[v] = true;
				}
				graph[v].add(i);
			}
		}
		return SccGraph;
	}
	public void dfs(int i) {
		visit[i] = true;
		for(int e : graph[i]) {
			if(!visit[e])
				dfs(e);
		}
	}
	public List<Integer> tSort(){
		for(int i = 0; i<N; i++) if(!visit[i]) dfs(i);
		Collections.reverse(seq);
		return seq;
	}
	public void scc() {
		for(int i =0; i<N; i++) visit[i]=false;
		int start = revSeq.remove(0);
	}
}
