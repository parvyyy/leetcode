public class ValidPalindrome {
    public boolean isPalindrome(String s) {
        String stripped = s.toLowerCase().replaceAll("[^A-Za-z0-9]", "");
        
        StringBuilder sb = new StringBuilder(stripped);
        return stripped.equals(sb.reverse().toString());
    }

    public boolean recurse(char[] s) {
        int len = s.length;
        if (s[0] != s[len - 1]) return false;
        if (len == 0 || len == 1) return true;

        return true;
    }

    public static void main(String[] args) {
        ValidPalindrome v = new ValidPalindrome();

        System.out.println(v.isPalindrome("A man, a plan, a canal: Panama"));
        System.out.println(v.isPalindrome("race a car"));
    }
    
}
