package Graphs;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * Created by Minsuk_Heo on 1/6/2017.
 */
public class FindShortestPathNoWeight {
    public static void main(String[] args) {
        FindShortestPathNoWeight solution = new FindShortestPathNoWeight();

        List<Integer> vertexList = new ArrayList<>();
        vertexList.add(0);
        vertexList.add(1);
        vertexList.add(2);
        vertexList.add(3);
        vertexList.add(4);
        vertexList.add(5);
        vertexList.add(6);

        List<int[]> edgeList = new ArrayList<>();
        edgeList.add(new int[]{0, 1});
        edgeList.add(new int[]{1, 2});
        edgeList.add(new int[]{1, 3});
        edgeList.add(new int[]{3, 4});
        edgeList.add(new int[]{4, 5});
        edgeList.add(new int[]{1, 6});


        List visitedNodeList = solution.bfs(vertexList,edgeList, 1, 5);
        System.out.println("path is : " + visitedNodeList.toString());
        System.out.println("distance is : " + visitedNodeList.size());
    }

    private List bfs(List<Integer> vertexList, List<int[]> edgeList, int start, int target) {
        List<Integer> visitedList = new ArrayList<>();
        Map<Integer, Integer> parentMap = new HashMap<>();
        parentMap.put(start, null);
        myQueue1 queue = new myQueue1();
        queue.enqueue(start);

        List<Integer>[] adjacencyList = new ArrayList[vertexList.size()];
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
                    parentMap.put(neighbor, current);
                    if(neighbor == target) {
                        break;
                    }
                }
            }
            visitedList.add(current);
        }
        List<Integer> pathToTarget = new ArrayList<>();
        int cur = target;
        while(parentMap.get(cur) != null) {
            pathToTarget.add(0,parentMap.get(cur));
            cur = parentMap.get(cur);
        }
        return pathToTarget;
    }
}

class myQueue1 {
    List<Integer> list = new ArrayList<Integer>();

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
