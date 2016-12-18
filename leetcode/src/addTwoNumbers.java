/**
 * Created by Minsuk_Heo on 12/17/2016.
 * https://leetcode.com/problems/add-two-numbers/
 * You are given two linked lists representing two non-negative numbers.
 * The digits are stored in reverse order and each of their nodes contain a single digit.
 * Add the two numbers and return it as a linked list.
 * Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
 * Output: 7 -> 0 -> 8
 */
public class addTwoNumbers {
    public static ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int carry = 0;
        ListNode head = new ListNode(0);
        ListNode result = head;

        // when two number still available
        while (l1 !=  null && l2 !=  null) {
            head.next = new ListNode((l1.val + l2.val + carry) % 10);
            head = head.next;
            carry = (l1.val + l2.val + carry) / 10;
            l1 = l1.next;
            l2 = l2.next;
        }

        // when l2 is done
        while (l1 != null) {
            head.next = new ListNode( (l1.val + carry) % 10 );
            carry = (l1.val + carry) / 10;
            head = head.next;
            l1 = l1.next;
        }

        // when l1 is done
        while (l2 != null) {
            head.next = new ListNode( (l2.val + carry) % 10 );
            carry = (l2.val + carry) / 10;
            head = head.next;
            l2 = l2.next;
        }

        // when carry has value
        if(carry != 0) {
            head.next = new ListNode(carry);
            carry = 0;
        }

        // abandon first value of result which is garbage
        return result.next;
    }

    public static void main(String [] args) {
        ListNode l1 = new ListNode(2);
        l1.next = new ListNode(4);
        l1.next.next = new ListNode(3);

        ListNode l2 = new ListNode(5);
        l2.next = new ListNode(6);
        l2.next.next = new ListNode(4);

        ListNode result = addTwoNumbers(l1, l2);
        while(result != null) {
            System.out.println(result.val);
            result = result.next;
        }
    }
}

class ListNode {
    int val;
    ListNode next;
    ListNode(int x) {val = x;}
}