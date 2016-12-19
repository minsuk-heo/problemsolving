import org.junit.Assert;

import static org.junit.Assert.*;

/**
 * Created by Minsuk_Heo on 12/18/2016.
 */
public class lengthOfLongestSubstringTest {
    @org.junit.Test
    public void lengthOfLongestSubstringTest() throws Exception {
        Assert.assertEquals(3, lengthOfLongestSubstring.solution("abcabcbb"));
    }
}