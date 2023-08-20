import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;

public class containsDuplicate {
    public boolean containsDuplicates(int[] nums) {
        List<Integer> l = Arrays.stream(nums).boxed().collect(Collectors.toList());
        Collections.sort(l);

        for (int i = 0, j = 0; j < l.size(); i++, j++) {
            if (l.get(i) == l.get(j)) return true;
        }

        return false;
    }
    public static void main (String[] args) {

    }
}
