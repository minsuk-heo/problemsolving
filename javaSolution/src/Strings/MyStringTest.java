package Strings;

/**
 * Created by Minsuk_Heo on 12/30/2016.
 */
public class MyStringTest {

    public static void main(String [] args){
        String str1 = "hello";
        String str2 = "hello";

        // How to Compare two string
        if(str1.equals(str2)) {
            System.out.println("same");
        }
        // How to Remove character in string
        str1 = "this is java";
        System.out.println(removeCharAt(str1,1));
        // How to Replace character or substring by new one
        System.out.println(str1.replace("t", "T"));
        System.out.println(str1.replaceAll("is", "ARE"));
        // How to reverse string
        StringBuffer sb = new StringBuffer(str1);
        String reversed = sb.reverse().toString();
        System.out.println(reversed);
        // How to split
        str1 = "jan-feb-march";
        String[] temp;
        String delimeter = "-";
        temp = str1.split(delimeter);
        for(String item : temp) {
            System.out.println(item);
        }
        // to uppercase
        System.out.println(str1.toUpperCase());
        // string + string
        System.out.println(str1+str2);
        // string + string using stringbuffer
        sb.append("ap1");
        sb.append("ap2");
        System.out.println(sb);

    }

    private static String removeCharAt(String s, int pos) {
        return s.substring(0, pos) + s.substring(pos+1);
    }
}
