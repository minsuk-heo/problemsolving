import java.util.Map;
import java.util.HashMap;

/**
 * Created by Minsuk_Heo on 12/18/2016.
 *
 * Given a string, find the length of the longest substring without repeating characters.
 * Given "abcabcbb", the answer is "abc", which the length is 3.
 * Given "bbbbb", the answer is "b", with the length of 1.
 * Given "pwwkew", the answer is "wke", with the length of 3.
 * Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
 *
 */
public class lengthOfLongestSubstring {

    public static void main(String [] args) {
        String str = "abcabcbb";
        int result = solution(str);
        System.out.println(result);
    }

    public static int solution(String s) {
        Map<Character, Integer> indexHash = new HashMap<Character, Integer>();
        int lengthOfLongestSubstring = 0;
        int substring_ptr = -1;

        for(int runner_idx = 0; runner_idx < s.length(); runner_idx++) {
            char c = s.charAt(runner_idx);
            if(indexHash.containsKey(c)) {
                int duplicate_ptr = indexHash.get(c);
                substring_ptr = Math.max(substring_ptr, duplicate_ptr);
            }
            lengthOfLongestSubstring = Math.max(lengthOfLongestSubstring, runner_idx - substring_ptr);
            indexHash.put(c, runner_idx);
        }
        return lengthOfLongestSubstring;
    }
}
