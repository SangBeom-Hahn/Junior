package Main;
import java.util.*;

public class Dik {
	boolean set[];
	int dis[];
	int N;
	int start;
	List<Edge2> graph[];
	Dik(List<Edge2> adjList[], int start){
		graph = adjList;
		N = graph.length;
		set = new boolean[N];
		dis = new int[N];
		this.start = start;
	}
	public int[] algo() {
		for(int i =0; i<N; i++) {
			set[i] = false;
			dis[i] = Integer.MAX_VALUE;
		}
		for(Edge2 e : graph[start])
			dis[e.adjVertax] = e.weight;
		set[start] = true;
		int minV = found();
		for(Edge2 e : graph[minV]) {
			if(dis[e.adjVertax]>dis[e.vertax]+e.weight) {
				dis[e.adjVertax] = dis[e.vertax]+e.weight;
			}
		}
		return dis;
	}
	public int found() {
		int min = Integer.MAX_VALUE;
		int minpos = -1;
		for(int i=0; i<N; i++) {
			if(min>dis[i]) {
				min = dis[i];
				minpos = i;
			}
		}
		return minpos;
	}
}
