import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class TwoSumII {
    public int[] twoSum(int[] nums, int target) {
        List<Integer> numbers = Arrays.stream(nums).boxed().collect(Collectors.toList());

        for (Integer num : numbers) {
            int pair = target - num;

            if (pair == num) {
                if (numbers.indexOf(num) != numbers.lastIndexOf(num)) {
                    int[] indices = {numbers.indexOf(num), numbers.lastIndexOf(pair)};
                    return indices;
                }

                continue;
            }

            if (binarySearch(numbers, pair)) {
                int[] indices = {numbers.indexOf(num), numbers.lastIndexOf(pair)};
                return indices;
            }
        }

        return new int[0];
    }

    // Returns whether toFind is an element of values in log(n) time.
    // @Pre-conditions: values is sorted.
    public <T extends Comparable<T>> boolean binarySearch(List<T> values, T toFind) {
        int midIndex = values.size() / 2;
        int comparison = values.get(midIndex).compareTo(toFind);

        if (values.size() == 0) return false;
        if (values.size() == 1 && comparison != 0) return false;
        
        // Bottom-Half
        if (comparison > 0) {
            return binarySearch(values.subList(0, midIndex), toFind);
        // Top-Half
        } else if (comparison < 0) { 
            return binarySearch(values.subList(midIndex, values.size()), toFind);
        }

        return true;
    }

    public static void main(String[] args) {
        TwoSumII t = new TwoSumII();

        t.twoSum(new int[]{3, 2, 4}, 6);
    }
}
