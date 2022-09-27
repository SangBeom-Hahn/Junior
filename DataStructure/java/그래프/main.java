package HSB;

import java.util.*;

public class main {
	public static void main(String[] args) {
		/*public void connect(in)
		List<Edge> adjList[] = new List[10];
		for(int i = 0; i < 10; i++) {
			adjList[i] = new LinkedList<>();
			for(int j = 0; j<10; j++) {
				if(i와 j 사이에 간선이 존재하면) {
					Edge e = new Edge(j);
					adjList[i].add(e);
				}
			}
		}*/
		
		int N = 10;
		List<Edge>[] adjList = new List[N];
		adjList[0] = new LinkedList<>(); 
			Edge e2 = new Edge(2); adjList[0].add(e2);
			Edge e1 = new Edge(1); adjList[0].add(e1);
			
		adjList[1] = new LinkedList<>(); 
			Edge e4 = new Edge(3); adjList[1].add(e4);
			Edge e3 = new Edge(0); adjList[1].add(e3);
			
		adjList[2] = new LinkedList<>(); 
			Edge e6 = new Edge(3); adjList[2].add(e6);
			Edge e5 = new Edge(0); adjList[2].add(e5);
			
		adjList[3] = new LinkedList<>(); 
			Edge e8 = new Edge(9); adjList[3].add(e8);
			Edge e9 = new Edge(8); adjList[3].add(e9);
			Edge e10 = new Edge(2); adjList[3].add(e10);
			Edge e7 = new Edge(1); adjList[3].add(e7);
			
		adjList[4] = new LinkedList<>(); Edge e11 = new Edge(5); adjList[4].add(e11);
			
		adjList[5] = new LinkedList<>(); Edge e12 = new Edge(7); adjList[5].add(e12);
			Edge e13 = new Edge(6); adjList[5].add(e13);
			Edge e14 = new Edge(4); adjList[5].add(e14);
			
		adjList[6] = new LinkedList<>(); Edge e15 = new Edge(7); adjList[6].add(e15);
			Edge e16 = new Edge(5); adjList[6].add(e16);
			
		adjList[7] = new LinkedList<>(); Edge e17 = new Edge(6); adjList[7].add(e17);
			Edge e18 = new Edge(5); adjList[7].add(e18);
			
		adjList[8] = new LinkedList<>(); Edge e19 = new Edge(3); adjList[8].add(e19);

		adjList[9] = new LinkedList<>(); Edge e20 = new Edge(3); adjList[9].add(e20);
		
		DFS d = new DFS(adjList);
	}
}