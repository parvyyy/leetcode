import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;

public class ThreeSum {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> ans = new ArrayList<>();

        Arrays.sort(nums);
        
        for (int i = 0; i < nums.length; i++) {
            int[] clone = new int[nums.length - 1];

            for (int j = 0, k = 0; j < nums.length; j++){
                if (j != i) {
                    clone[k] = nums[j];
                    k++;
                }
            }

            int[] pairs = twoSum(clone, -nums[i]);

            for (int j = 0; j < pairs.length;) {
                List<Integer> trio = new ArrayList<>();
                trio.add(pairs[j++]);
                trio.add(pairs[j++]);
                trio.add(nums[i]);

                trio.sort(null);

                ans.add(trio);

                
            }

        }

        return new ArrayList<>(new HashSet<>(ans));
    }

    // Nums must be a sorted list.
    public int[] twoSum(int[] nums, int target) {
        int i = 0;
        int j = nums.length - 1;

        List<Integer> pairs = new ArrayList<>();

        while (i < j) {
            if (nums[i] + nums[j] > target) {
                j--;
            } else if (nums[i] + nums[j] < target) {
                i++;
            } else if (nums[i] + nums[j] == target) {
                pairs.add(nums[i]);
                pairs.add(nums[j]);

                while (i < j && nums[i] == nums[i + 1]) {
                    i++;
                }

                while (i < j && nums[j] == nums[j - 1]) {
                    j--;
                }

                i++;
                j--;
            }
        }


        return pairs.stream().mapToInt(x -> x).toArray();
    }



    public static void main(String[] args) {
        ThreeSum t = new ThreeSum();

        System.out.println(t.threeSum(new int[]{-1,0,1,2,-1,-4}).toString());
        System.out.println(t.threeSum(new int[]{0, 1, 1}).toString());
        System.out.println(t.threeSum(new int[]{0, 0, 0}).toString());
        System.out.println(t.threeSum(new int[]{-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0}).toString());
    }
}
