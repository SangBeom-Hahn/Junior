package Main;

public class UnionFind {
	int parents[];
	
	UnionFind(int N){
		parents = new int[N];
		for(int i=0; i<N; i++) {
			parents[i] = i; //초기엔 자기자신이 부모
		}
	}
	public int find(int node) {
		if(parents[node] != node) {
			parents[node] = find(parents[node]);
		}
		return parents[node];
	}
	public boolean connect(int i, int j) {
		return find(i) == find(j);
	}
	public void union(int i, int j) {
		int iroot = find(i);
		int jroot = find(j);
		parents[jroot] = iroot;
	}	
}
