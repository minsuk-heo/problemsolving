/**
 * Created by Minsuk_Heo on 12/17/2016.
 *  https://leetcode.com/problems/two-sum/
 *  Given nums = [2, 7, 11, 15], target = 9,
 *  Because nums[0] + nums[1] = 2 + 7 = 9,
 *  return [0, 1].
 *
 *  Time complexity: O(n)
 */
import java.util.*;

public class twoSum {

    public static int[] twoSum(int[] nums, int target) {
        Hashtable hash = new Hashtable();
        int[] answer = new int[2];

        // iterate given array
        for(int i=0; i<nums.length; i++){
            // if hash has key which same with current value, return hash value with i
            if(hash.containsKey(nums[i])){
                answer[0] = (int)hash.get(nums[i]);
                answer[1] = i;
            }
            // if i is not in hash keys, add key: target - current value, value: current index
            else {
                hash.put(target - nums[i], i);
            }
        }
        return answer;
    }

    public static void main(String [] args) {
        int[] arr = {2,7,11,15};

        for (int item : twoSum(arr, 9)) {
            System.out.println(item);
        }
    }
}
