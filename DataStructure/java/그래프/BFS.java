package Main;
import java.util.*;

public class BFS {
	int M;
	boolean visited[];
	List<Edge> graph[];
	BFS(int M, List<Edge> adjList[]){
		this.M = M;
		visited=new boolean[M];
		graph = adjList;
		for(int i = 0; i<M; i++) visited[i] = false;
		for(int i = 0; i<M; i++)
			if(!visited[i])
				bfs(i);
	}
	//¸Þ¼Òµå
	public void bfs(int i) {
		Queue<Integer> q = new LinkedList<>();
		visited[i] = true;
		q.add(i);
		while(!q.isEmpty()) {
			int j = q.remove();;
			System.out.print(j+"->");
			for(Edge e : graph[j]) {
				if(!visited[e.adjvertex])
					visited[e.adjvertex] = true;
					q.add(e.adjvertex);
			}
		}
	}
}
