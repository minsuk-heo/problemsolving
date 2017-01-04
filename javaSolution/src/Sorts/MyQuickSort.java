package Sorts;
import java.util.Arrays;

/**
 * Created by Minsuk_Heo on 1/3/2017.
 */
public class MyQuickSort {
    public static void main(String[] args) {
        int[] arr = {4,5,1,3,8,6,9,7,2};
        MyQuickSort qsort = new MyQuickSort();
        qsort.sort(arr);
        System.out.println(Arrays.toString(arr));
    }

    public void sort(int[] arr) {
        quicksort(arr, 0, arr.length-1);
    }

    private void quicksort(int[] arr, int start, int end) {
        // repeat until sublist has one item
        // because the algorithm is using in-place space, we can not use len(list) instead we use start, end for sublist
        if(start < end) {
            // get pivot using partition method
            int pivot = partition(arr, start, end);
            // recurse quick sort left side from pivot
            quicksort(arr, start, pivot-1);
            // recurse quick sort right side from pivot
            quicksort(arr,pivot+1, end);
        }
    }

    private int partition(int[] arr, int start, int end) {
        // use end item as initial pivot
        int pivot = end;
        // use start as initial wall index
        int wall = start;
        int left = start;
        // repeat until left item hit the end of list
        while (left < pivot) {
            // if left item is smaller than pivot, swap left item with wall and move wall to right
            // this will ensure items smaller than pivot stay left side from the wall and
            // the items greater than pivot stay right side from the wall
            if (arr[left] < arr[pivot]) {
                swap(arr, wall, left);
                wall = wall + 1;
            }
            left = left + 1;
        }

        // when left hit the end of list, swap pivot with wall
        swap(arr, wall, pivot);
        // now left side of wall are the items smaller than wall
        // now right side of pivot are the items greater than wall
        // wall is the new pivot
        pivot = wall;
        return pivot;
    }

    private void swap(int[] arr, int i,int j){
        int tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    }
}
