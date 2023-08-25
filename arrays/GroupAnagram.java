import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;

public class GroupAnagram extends ValidAnagram {
    public String[][] groupAnagrams(String[] strs) {
        
        List<List<String>> anagramGroups = new ArrayList<>();

        List<String> strings = Arrays.stream(strs).collect(Collectors.toList());

        Set<String> visited = new HashSet<>();

        int index = 0;
        for (String str : strings) {
            if (!visited.contains(str)) {
                List<String> anagrams = strings.subList(index, strings.size()).stream().filter(p -> isAnagram(p, str)).collect(Collectors.toList());
                anagrams.forEach(a -> visited.add(a));

                if (!anagramGroups.contains(anagrams)) {
                    anagramGroups.add(anagrams);
                }
            }

            index++;
        }

        String[][] s = new String[strs.length][];

        int i = 0;
        for (List<String> strList : anagramGroups) {
            s[i] = strList.toArray(new String[strList.size()]);

            i++;
        }

        return s;
    }

    public static void main(String[] args) {
        String[] strArray = {"eat","tea","tan","ate","nat","bat"};

        GroupAnagram g = new GroupAnagram();
        System.out.println(g.groupAnagrams(strArray));
    }
}
