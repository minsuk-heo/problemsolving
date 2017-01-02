package data_structure;

/**
 * Created by Minsuk_Heo on 1/1/2017.
 */
public class MyLinkedList {
    Node head = null;

    public void add(int n){
        Node newNode = new Node(n);
        if(head == null){
            head = newNode;
        } else{
            Node cur = head;
            while(cur.next != null){
                cur = cur.next;
            }
            cur.next = newNode;
        }
    }

    public void remove(int n){
        Node cur = head;

        if(head.val == n) {
            head = cur.next;
            cur = null;
        } else {
            while(cur.next != null) {
                if(cur.next.val == n) {
                    cur.next = cur.next.next;
                    System.out.println(n+ " removed successfully");
                    return;
                }
                cur = cur.next;
            }
            System.out.println(n+" is not in linkedlist");
        }
    }

    public void reverse(){
        Node cur = head;
        Node prev = null;
        Node next = null;

        while(cur != null){
            next = cur.next;
            cur.next = prev;
            prev = cur;
            cur = next;
        }
        head = prev;
    }

    public void print(){
        Node cur = head;

        while(cur != null){
            System.out.println(cur.val);
            cur = cur.next;
        }
    }

    public static void main(String[] args) {
        MyLinkedList ml = new MyLinkedList();
        ml.add(1);
        ml.add(2);
        ml.add(3);
        ml.add(4);
        ml.print();
        ml.reverse();
        ml.print();
    }
}

class Node{
    int val;
    Node next;

    public Node(int n){
        val = n;
        next = null;
    }
}