package data_structure;


/**
 * Created by Minsuk_Heo on 1/1/2017.
 */
public class MyStack <T> {
    private T[] arr;
    private int top = 0;
    private static final int defaultStackSize = 3;

    public MyStack(){
        this(defaultStackSize);
    }

    public MyStack(int stSize) {
        arr = (T[]) new Object[stSize];
    }

    public void push(T element){
        if(arr.length == top) {
            // prevent stack overflow
            System.out.println("stack is full, can't push");
        } else {
            arr[top++] = element;
        }
    }

    public T pop() {
        if(top == 0) {
            System.out.println("no more item in the stack, can't pop");
            throw new java.util.NoSuchElementException();
        } else {
            T ele = arr[--top];
            // prevent memory leak
            arr[top] = null;
            return ele;
        }
    }



    public static void main(String[] args) {
        MyStack<Integer> intStack = new MyStack<Integer>(5);
        intStack.push(2);
        intStack.push(3);
        System.out.println(intStack.pop());
        System.out.println(intStack.pop());
        MyStack<String> stringStack = new MyStack<String>();
        stringStack.push("abc");
        stringStack.push("def");
        System.out.println(stringStack.pop());
        System.out.println(stringStack.pop());
    }
}
