package Collections;

import java.util.Collection;
import java.util.HashMap;
import java.util.Iterator;

/**
 * Created by Minsuk_Heo on 1/1/2017.
 */
public class MyCollectionsTest {
    public static void main(String[] args) {
        HashMap<String, String> hMap = new HashMap<String, String>();
        hMap.put("1","first");
        hMap.put("2","second");

        Collection cl = hMap.values();
        Iterator itr = cl.iterator();

        while(itr.hasNext()){
            System.out.println(itr.next());
        }
    }
}
