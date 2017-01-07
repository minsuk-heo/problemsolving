package Graphs;

import com.sun.javafx.geom.Edge;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Collections;

/**
 * Created by Minsuk_Heo on 1/6/2017.
 */
public class Dijkstra {
    public static void main(String[] args) {
        Graph g = new Graph();

        //add vertices
        g.addVertex(1);
        g.addVertex(2);
        g.addVertex(3);
        g.addVertex(4);
        g.addVertex(5);
        g.addVertex(6);

        //add edges with weight
        g.addEdge(1, 2, 7);
        g.addEdge(2, 1, 7);
        g.addEdge(1, 3, 9);
        g.addEdge(3, 1, 9);
        g.addEdge(1, 6, 14);
        g.addEdge(6, 1, 14);
        g.addEdge(2, 3, 10);
        g.addEdge(3, 2, 10);
        g.addEdge(2, 4, 15);
        g.addEdge(4, 2, 15);
        g.addEdge(3, 4, 11);
        g.addEdge(4, 3, 11);
        g.addEdge(3, 6, 2);
        g.addEdge(6, 3, 2);
        g.addEdge(4, 5, 6);
        g.addEdge(5, 4, 6);
        g.addEdge(5, 6, 9);
        g.addEdge(6, 5, 9);

        Dijkstra dijkstra = new Dijkstra();
        dijkstra.shortestPath(g,1,4);


    }

    private void shortestPath(Graph g, int from, int to) {
        Map<Integer, Integer> path = new HashMap<Integer, Integer>();
        // use first vertex as start point of dijkstra algorithm
        path = dijkstra(g, g.vertexList.get(0));

        List<Integer> route = new ArrayList<Integer>();
        route.add(to);

        while(to != from) {
            route.add(path.get(to));
            to = path.get(to);
        }

        //reverse
        Collections.reverse(route);
        System.out.println(route);
    }

    private Map<Integer,Integer> dijkstra(Graph g, Integer start) {
        Map<Integer, Integer> visitedVertex = new HashMap<Integer, Integer>();
        visitedVertex.put(start, 0);
        Map<Integer, Integer> path = new HashMap<Integer, Integer>();

        while(g.vertexList.size() > 0){
            //suppose vertex should be > -1
            int minVertex = -1;
            for(int vertex : g.vertexList){
                if(visitedVertex.containsKey(vertex)){
                    if(minVertex == -1){
                        minVertex = vertex;
                    }
                    else if(visitedVertex.get(vertex) < visitedVertex.get(minVertex)){
                        minVertex = vertex;
                    }
                }
            }
            if(minVertex == -1){
                break;
            }

            for(int i=0;i<g.vertexList.size();i++){
                if(minVertex == g.vertexList.get(i)) {
                    g.vertexList.remove(i);
                    break;
                }
            }
            int curWeight = visitedVertex.get(minVertex);
            List<Integer> adjacencyVertice = g.adjacencyList.get(minVertex);

            for(int vertex : adjacencyVertice){
                int weight = curWeight + g.weightOnEdge.get(Integer.toString(minVertex)+","+Integer.toString(vertex));
                if(!visitedVertex.containsKey(vertex) || weight < visitedVertex.get(vertex)){
                    visitedVertex.put(vertex, weight);
                    path.put(vertex, minVertex);
                }
            }
        }

        return path;
    }
}

class Graph{
    public List<Integer> vertexList = new ArrayList<Integer>();
    public Map<Integer, List> adjacencyList = new HashMap<Integer, List>();
    public Map<String, Integer> weightOnEdge = new HashMap<String, Integer>();

    public void addVertex(int i) {
        vertexList.add(i);
    }

    public void addEdge(int from, int to, int weight) {
        if(adjacencyList.containsKey(from)){
            // update adjacencyList
            adjacencyList.get(from).add(to);
            weightOnEdge.put(Integer.toString(from)+","+Integer.toString(to), weight);
        }
        else {
            List<Integer> vertexList = new ArrayList<Integer>();
            vertexList.add(to);
            // add vertex in adjacencyList
            adjacencyList.put(from, vertexList);
            // store weight on edge
            weightOnEdge.put(Integer.toString(from)+","+Integer.toString(to), weight);
        }

    }
}

