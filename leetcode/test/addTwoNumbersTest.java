import org.junit.Assert;
import org.junit.Test;

/**
 * Created by Minsuk_Heo on 12/17/2016.
 * https://leetcode.com/problems/add-two-numbers/
 * You are given two linked lists representing two non-negative numbers.
 * The digits are stored in reverse order and each of their nodes contain a single digit.
 * Add the two numbers and return it as a linked list.
 * Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
 * Output: 7 -> 0 -> 8
 */

import static org.junit.Assert.*;

/**
 * Created by Minsuk_Heo on 12/17/2016.
 */
public class addTwoNumbersTest {
    @Test
    public void addTwoNumbers() throws Exception {
        ListNode l1 = new ListNode(2);
        l1.next = new ListNode(4);
        l1.next.next = new ListNode(3);

        ListNode l2 = new ListNode(5);
        l2.next = new ListNode(6);
        l2.next.next = new ListNode(4);

        ListNode expected = addTwoNumbers.addTwoNumbers(l1, l2);

        Assert.assertEquals(7, expected.val);
        expected = expected.next;
        Assert.assertEquals(0, expected.val);
        expected = expected.next;
        Assert.assertEquals(8, expected.val);

    }

}