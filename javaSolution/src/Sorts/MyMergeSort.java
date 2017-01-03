package Sorts;
import java.util.Arrays;
/**
 * Created by Minsuk_Heo on 1/2/2017.
 */
public class MyMergeSort {
    int [] tmpArr;
    public static void main(String[] args) {
        int [] arr = {4,2,8,1,3,5,7,9,6};
        MyMergeSort msort = new MyMergeSort();
        msort.mergesort(arr);
    }

    public void mergesort(int[] arr) {
        tmpArr = new int[arr.length];
        System.out.println("splitting"+Arrays.toString(arr));
        merge(arr, 0, arr.length-1);

    }

    private void merge(int[] arr, int begin, int end) {
        if(begin < end) {
            int mid = (begin+end) / 2;
            merge(arr, begin, mid);
            merge(arr, mid+1, end);

            for(int i = begin; i<=end;i++) {
                tmpArr[i] = arr[i];
            }

            int i=begin, j=mid+1, k=begin;
            while(i <= mid && j <= end) {
                if (tmpArr[i] < tmpArr[j]) {
                    arr[k] = tmpArr[i];
                    i++;
                }
                else{
                    arr[k] = tmpArr[j];
                    j++;
                }
                k++;
            }
            while(i<=mid) {
                arr[k] = tmpArr[i];
                i++;
                k++;
            }
            while(j<=end) {
                arr[k] = tmpArr[j];
                j++;
                k++;
            }
        }

        System.out.println(Arrays.toString(arr));
    }

    private void swap(int[] arr, int i,int j){
        int tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    }
}
