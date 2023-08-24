import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class TwoSum {
    public int[] twoSum(int[] nums, int target) {
        List<Integer> numbers = Arrays.stream(nums).boxed().collect(Collectors.toList());

        for (Integer num : numbers) {
            Integer pair = target - num;

            List<Integer> dup = new ArrayList<>(numbers);
            dup.remove(num);

            if (dup.contains(pair)) {
                int[] indices = {numbers.indexOf(num), numbers.lastIndexOf(pair)};
                return indices;
            }
        }

        return new int[0];
    }

    public static void main(String[] args) {
        int[] nums = {3, 3};

        TwoSum s = new TwoSum();
        s.twoSum(nums, 6);

    }
}