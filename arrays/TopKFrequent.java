import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

public class TopKFrequent {
    public static int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> frequencyMap = new HashMap<>();
        List<Integer> numbers = Arrays.stream(nums).boxed().collect(Collectors.toList());

        // O(n) complexity
        for (Integer num : numbers) {
            if (!frequencyMap.containsKey(num)) {
                frequencyMap.put(num, 0);
            } else {
                frequencyMap.put(num, frequencyMap.get(num) + 1);
            } 
        }

        List<Integer> topKFrequent = new ArrayList<>();

        // O(kN)
        for (int i = 0; i < k; i++) {
            // Find the max key-value pair
            Integer max = null;
            
            for (Integer key : frequencyMap.keySet()) {
                if (max == null) {
                    max = key;
                }

                if (frequencyMap.get(key) > frequencyMap.get(max)) {
                    max = key;
                }
            }

            topKFrequent.add(max);
            frequencyMap.remove(max);
        }

        return topKFrequent.stream().mapToInt(i->i).toArray();
    }

    public static void main(String[] args) {
        int[] nums = {1,1,1,2,2,3};
        System.out.println(TopKFrequent.topKFrequent(nums, 2));
        int[] nums2 = {1};
        System.out.println(TopKFrequent.topKFrequent(nums2, 1));
    }
}