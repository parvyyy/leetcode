import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class ValidAnagram {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        List<String> sChars = Arrays.stream(s.split("")).collect(Collectors.toList());
        List<String> tChars = Arrays.stream(t.split("")).collect(Collectors.toList());
        
        sChars.sort(null);
        tChars.sort(null);

        return sChars.equals(tChars);
    }

    public static void main (String[] args) {
        ValidAnagram v = new ValidAnagram();
        System.out.println(v.isAnagram("anagram", "nagaram"));
        System.out.println(v.isAnagram("rat", "car"));
    }
}
