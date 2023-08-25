import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class ArrayProductExceptSelf {
    public static int[] productExceptSelf(int[] nums) {
        List<Integer> left = new ArrayList<>();
        List<Integer> right = new ArrayList<>();

        List<Integer> numbers = Arrays.stream(nums).boxed().collect(Collectors.toList());

        left.add(0, numbers.get(0));

        for (int i = 1; i < numbers.size(); i++) {
            int next = left.get(i - 1) * numbers.get(i);
            left.add(i, next);
        }

        int index = numbers.size() - 1;
        right.add(0, numbers.get(index));
        
        for (int i = 1; i < numbers.size(); i++) {
            int next = right.get(i - 1) * numbers.get(index - i);
            right.add(i, next);
        }

        List<Integer> answers = new ArrayList<>(nums.length);

        // Edge cases - first & last element.
        answers.add(0, right.get(index - 1));

        for (int i = 1; i < numbers.size() - 1; i++) {
            int prod = left.get(i - 1) * right.get(index - i - 1);
            answers.add(i, prod);          
        }

        answers.add(index, left.get(index - 1));

        // For Debuggin
        // answers.stream().forEach(s -> System.out.print(s + " "));
        return answers.stream().mapToInt(i -> i).toArray();
    }


    public static void main(String[] args) {
        int[] nums = {1, 2, 3, 4};
        ArrayProductExceptSelf.productExceptSelf(nums);
    }

    
}
