package Graphs;

import java.util.ArrayList;
import java.util.Stack;

/**
 * Created by Minsuk_Heo on 1/5/2017.
 */
public class MyDFS {
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
        edgeList.add(new int[]{0, 2});
        edgeList.add(new int[]{1, 0});
        edgeList.add(new int[]{1, 3});
        edgeList.add(new int[]{2, 0});
        edgeList.add(new int[]{2, 4});
        edgeList.add(new int[]{2, 5});
        edgeList.add(new int[]{3, 1});
        edgeList.add(new int[]{4, 2});
        edgeList.add(new int[]{4, 6});
        edgeList.add(new int[]{4, 5});
        edgeList.add(new int[]{5, 4});
        edgeList.add(new int[]{5, 2});
        edgeList.add(new int[]{6, 4});

        MyDFS dfs = new MyDFS();
        ArrayList visitedNodeList = dfs.run(vertexList,edgeList, 0);
        System.out.println(visitedNodeList.toString());

    }

    private ArrayList run(ArrayList<Integer> vertexList, ArrayList<int[]> edgeList, int n) {
        ArrayList<Integer> visitedList = new ArrayList<>();
        Stack<Integer> myStack = new Stack();
        myStack.push(n);

        ArrayList<Integer>[] adjacencyList = new ArrayList[vertexList.size()];
        for(int i=0; i<adjacencyList.length; i++){
            adjacencyList[i] = new ArrayList<Integer>();
        }

        for(int[] edge : edgeList){
            adjacencyList[edge[0]].add(edge[1]);
        }

        int current;
        while(!myStack.isEmpty()) {
            current = myStack.pop();
            for (int neighbor : adjacencyList[current]) {
                if(!visitedList.contains(neighbor)){
                    myStack.push(neighbor);
                }
            }
            visitedList.add(current);
        }
        return visitedList;
    }
}