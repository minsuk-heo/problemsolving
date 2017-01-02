package Arrays;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

/**
 * Created by Minsuk_Heo on 12/31/2016.
 */
public class MyArrayTest {
    public static void main(String[] args) {
        int[] array = { 2, 5, -2, 6, -3, 8, 0, -7, -9, 4 };
        //Sort
        Arrays.sort(array);
        printArray("Sorted array", array);
        int index = Arrays.binarySearch(array, 2);
        System.out.println("Found 2 @ " + index);

        // reverse
        ArrayList arrayList = new ArrayList();
        arrayList.add("A");
        arrayList.add("B");
        arrayList.add("C");
        arrayList.add("D");
        arrayList.add("E");
        System.out.println(arrayList);
        Collections.reverse(arrayList);
        System.out.println(arrayList);

        // merge two array
        String[] a = {"A", "B", "C"};
        String[] b = {"O", "U"};
        List list = new ArrayList(Arrays.asList(a));
        list.addAll(Arrays.asList(b));
        Object[] c = list.toArray();
        System.out.println(Arrays.toString(c));

        // fill array at once
        int[] arr = new int[6];
        Arrays.fill(arr, 100);
        for(int i : arr){
            System.out.println(i);
        }

        // remove array item
        ArrayList<Integer> intArr = new ArrayList<Integer>();
        intArr.add(0);
        intArr.add(1);
        intArr.add(300);
        System.out.println(intArr);
        intArr.remove(0);
        System.out.println(intArr);

        ArrayList<String> stArr = new ArrayList<String>();
        stArr.add("abc");
        stArr.add("efg");
        System.out.println(stArr);
        stArr.remove("efg");
        System.out.println(stArr);

        // compare two array
        int[] ary = {1,2,3,4,5,6};
        int[] ary1 = {1,2,3,4,5,6};
        int[] ary2 = {1,2,3,4};
        System.out.println("Is array 1 equal to array 2?? " +Arrays.equals(ary, ary1));
        System.out.println("Is array 1 equal to array 3?? " +Arrays.equals(ary, ary2));

    }

    private static void printArray(String message, int array[]) {
        System.out.println(message + ": [length: " + array.length + "]");

        for (int i = 0; i < array.length; i++) {
            if(i != 0) {
                System.out.print(", ");
            }
            System.out.print(array[i]);
        }
        System.out.println();
    }
}
