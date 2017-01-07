package Graphs;

import java.util.ArrayList;
import java.util.Queue;

/**
 * Created by Minsuk_Heo on 1/3/2017.
 */
public class MyBFS {

    public static void main(String[] args) {
        ArrayList<Integer> vertexList = new ArrayList<>();
        vertexList.add(0);
        vertexList.add(1);
        vertexList.add(2);
        vertexList.add(3);
        vertexList.add(4);
        vertexList.add(5);
        vertexList.add(6);

        ArrayList<int[]> edgeList = new ArrayList<>();
        edgeList.add(new int[]{0, 1});
        edgeList.add(new int[]{1, 2});
        edgeList.add(new int[]{1, 3});
        edgeList.add(new int[]{3, 4});
        edgeList.add(new int[]{4, 5});
        edgeList.add(new int[]{1, 6});
        
        MyBFS bfs = new MyBFS();
        ArrayList visitedNodeList = bfs.run(vertexList,edgeList, 0);
        System.out.println(visitedNodeList.toString());

    }

    private ArrayList run(ArrayList<Integer> vertexList, ArrayList<int[]> edgeList, int n) {
        ArrayList<Integer> visitedList = new ArrayList<>();
        myQueue queue = new myQueue();
        queue.enqueue(n);

        ArrayList<Integer>[] adjacencyList = new ArrayList[vertexList.size()];
        for(int i=0; i<adjacencyList.length; i++){
            adjacencyList[i] = new ArrayList<Integer>();
        }

        for(int[] edge : edgeList){
            adjacencyList[edge[0]].add(edge[1]);
        }

        int current;
        while(!queue.isEmpty()) {
            current = queue.dequeue();
            for (int neighbor : adjacencyList[current]) {
                if(!visitedList.contains(neighbor)){
                    queue.enqueue(neighbor);
                }
            }
            visitedList.add(current);
        }
        return visitedList;
    }
}

class myQueue {
    ArrayList<Integer> list = new ArrayList<Integer>();

    public void enqueue(int n){
        list.add(n);
    }

    public int dequeue(){
       return list.remove(0);
    }

    public boolean isEmpty(){
        return list.isEmpty();
    }
}