package data_structure;

import java.util.ArrayList;

/**
 * Created by Minsuk_Heo on 1/1/2017.
 */
public class MyQueue {
    ArrayList<Integer> queue = new ArrayList<Integer>();

    public void enqueue(Integer n) {
        queue.add(n);
    }

    public Integer dequeue() {
        if(queue.isEmpty()) {
            System.out.println("queue is empty");
            throw new java.util.NoSuchElementException();
        }
        return queue.remove(0);
    }

    public static void main(String[] args) {
        MyQueue mq = new MyQueue();
        mq.enqueue(1);
        mq.enqueue(2);
        mq.enqueue(3);
        mq.enqueue(4);
        System.out.println(mq.dequeue());
        System.out.println(mq.dequeue());
        System.out.println(mq.dequeue());
        System.out.println(mq.dequeue());
    }
}


