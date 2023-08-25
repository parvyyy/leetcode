import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class LongestConsecutiveSequence {
    public int longestConsecutive(int[] nums) {
        Map<Integer, Integer> adj = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            adj.put(nums[i], 0);
        }

        int max = 0;
        Set<Integer> visited = new HashSet<>();

        for (int i : adj.keySet()) {
            // O(n), as we do not repeat visits.
            if (!visited.contains(i)) {

                int numAdj = recurseLeft(adj, visited, i) + recurseRight(adj, visited, i);
                max = Math.max(max, numAdj + 1);
            }
        }

        return max;
    }

    public int recurseLeft(Map<Integer, Integer> adj, Set<Integer> visited, int key) {
        visited.add(key);

        if (adj.containsKey(key - 1)) {
            return recurseLeft(adj, visited, key - 1) + 1;
        }

        return 0;
    }

    public int recurseRight(Map<Integer, Integer> adj, Set<Integer> visited, int key) {
        visited.add(key);

        if (adj.containsKey(key + 1)) {
            return recurseRight(adj, visited, key + 1) + 1;
        }

        return 0;
    }

    public static void main (String[] args) {
        int[] nums = {100,4,200,1,3,2};

        LongestConsecutiveSequence l = new LongestConsecutiveSequence();
        System.out.println(l.longestConsecutive(nums));
    }
}
