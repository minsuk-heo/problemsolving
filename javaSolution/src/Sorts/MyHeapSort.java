package Sorts;

/**
 * Created by Minsuk_Heo on 1/2/2017.
 */
public class MyHeapSort {

    public static void main(String[] args) {
        int [] arr = {4,2,8,1,3,5,7,9,6};
        MyHeapSort mh = new MyHeapSort();
        mh.heapsort(arr);
    }

    private void heapsort(int[] arr) {
        heapify(arr);
        int end = arr.length - 1;
        while(end > 0) {
            swap(arr, 0, end);
            siftdown(arr,0,end);
            end -= 1;
        }
        for(int i : arr){
            System.out.println(i);
        }
    }

    private void heapify(int[] arr) {
        int p = arr.length / 2 - 1;
        while (p>=0) {
            siftdown(arr, p, arr.length);
            p -= 1;
        }
        
    }

    private void siftdown(int[] arr, int p, int size) {
        int l = 2*p + 1;
        int r = 2*p + 2;
        int largest = p;

        if (l <= size - 1 && arr[l] > arr[p]) {
            largest = l;
        }

        if (r <= size - 1 && arr[r] > arr[largest]) {
            largest = r;
        }

        if (largest != p) {
            swap(arr, p, largest);
            siftdown(arr, largest, size);
        }
    }

    private void swap(int[] arr, int i,int j){
        int tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    }
}
