package data_structure;

/**
 * Created by Minsuk_Heo on 1/1/2017.
 */
public class myBST {
    treeNode head;

    public void insert(int n){
        if (head == null) {
            head = new treeNode(n);
        } else {
            insertNode(head, n);
        }
    }

    private void insertNode(treeNode cur, int n){
        if (cur.val > n) {
            if(cur.left == null){
                cur.left = new treeNode(n);
            } else {
                insertNode(cur.left, n);
            }
        } else {
            if(cur.right == null){
                cur.right = new treeNode(n);
            } else {
                insertNode(cur.right, n);
            }
        }
    }

    public void remove(int n){
        // if head is the value
        if(head.val == n) {
            if(head.left != null && head.right == null) {
                head = head.left;
            }
            else if (head.left == null && head.right != null) {
                head = head.right;
            }
            else if (head.left != null && head.right != null) {
                head.val = getMostLeftChild(head.right).val;
                removeMostLeftChild(head, head.right);
            }
            // head has no children
            else{
                head = null;
            }
        }
        // else, find the value using binary search and remove
        else {
            if(head.val > n) {
                removeItem(head, head.left, n);
            }
            else{
                removeItem(head, head.right, n);
            }
        }
    }

    private void removeMostLeftChild(treeNode parent, treeNode cur) {
        if(cur.left != null) {
            removeMostLeftChild(cur, cur.left);
        } else {
            // if most left item is the head's right child, just remove right child
            if(parent == head) {
                parent.right = null;
            } else {
                parent.left = null;
            }
        }
    }

    private void removeItem(treeNode parent, treeNode cur, int n){
        if(cur.val == n ) {
            if(cur.left != null && cur.right == null) {
                if(parent.val > n) {
                    parent.left = cur.left;
                }
                else {
                    parent.right = cur.left;
                }
            }
            else if (cur.left == null && cur.right != null) {
                if(parent.val > n) {
                    parent.left = cur.right;
                }
                else {
                    parent.right = cur.right;
                }
            }
            else if (cur.left != null && cur.right != null) {
                cur.val = getMostLeftChild(cur.right).val;
                removeMostLeftChild(cur, cur.right);
            }
            // head has no children
            else{
                if(parent.val > n) {
                    parent.left = null;
                }
                else {
                    parent.right = null;
                }
            }
        }
        else {
            if(cur.val > n) {
                removeItem(cur, cur.left, n);
            }
            else{
                removeItem(cur, cur.right, n);
            }
        }
    }

    private treeNode getMostLeftChild(treeNode cur) {
        if(cur.left != null) {
            return getMostLeftChild(cur.left);
        } else {
            return cur;
        }
    }

    public void inorder() {
        inorderTraverse(head);
    }

    private void inorderTraverse(treeNode cur){
        if(cur != null){
            inorderTraverse(cur.left);
            System.out.println(cur.val);
            inorderTraverse(cur.right);
        }
    }

    public static void main(String[] args) {
        myBST bst = new myBST();
        bst.insert(7);
        bst.insert(5);
        bst.insert(15);
        bst.insert(14);
        bst.insert(17);
        bst.insert(16);
        //bst.inorder();
        bst.remove(15);
        bst.inorder();
    }
}

class treeNode{
    int val;
    treeNode left;
    treeNode right;

    public treeNode(int n){
        val = n;
        left = null;
        right = null;
    }
}
