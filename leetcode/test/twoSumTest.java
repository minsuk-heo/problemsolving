/**
 * Created by Minsuk_Heo on 12/17/2016.
 */

import org.junit.Assert;

public class twoSumTest {
    @org.junit.Test
    public void twoSumTest() throws Exception {
        int [] testSet = {2,7,11,15};
        int [] expected = {0,1};
        Assert.assertEquals(0, twoSum.twoSum(testSet, 9)[0]);
        Assert.assertEquals(1, twoSum.twoSum(testSet, 9)[1]);
    }
}
