# https://leetcode.com/problems/unique-length-3-palindromic-subsequences/
# 4/1/25
""" 
    How to efficiently generate a subsequence of length 3.
    Can we skip any?

    Checking if it is a palindrome is O(1).
    Adding to a set ensures uniqueness in O(1).
"""
def countPalindromicSubsequence(s: str) -> int:
    n = len(s)

    # If the string is not of size 3, there can be no length-3 subseq.
    if n < 3:
        return 0

    unique_palindromes = set()

    def isPalindrome(s: str) -> bool:
        return s == s[::-1]
    
    ### Naive w/ Personal Optimisation
    # Consider a string like "aabca". The length-3 subsequences generated using the
    # second 'a' would have already been covered by the first 'a'. Hence, we may skip this
    # as a starting element. We apply the same for the second letter.
    first_letters = set()
    second_letters = set()

    for i in range(n):
        # Skips to the next element as all length-3 palindromes starting with this letter
        # have been discovered.
        if s[i] in first_letters:
            continue

        first_letters.add(s[i])

        for j in range(i + 1, n):
            if s[j] in second_letters:
                continue

            second_letters.add(s[j])

            for k in range(j + 1, n):
                s_3 = s[i] + s[j] + s[k]

                if s_3 in unique_palindromes:
                    continue

                if isPalindrome(s_3):
                    unique_palindromes.add(s_3)

            second_letters.clear()

    return len(unique_palindromes)

# O(n) total time complexity.
def countPalindromicSubsequenceOptimised(s: str) -> int:
    letters = set(s[::])

    num_palindromes = 0

    # At most 26 iterations,
    for letter in letters:
        # O(n)
        l, r = s.find(letter), s.rfind(letter)
        btwn = s[l + 1 : r]

        num_palindromes += len(set(btwn[::]))

    return num_palindromes

print(countPalindromicSubsequenceOptimised("aabca"))
print(countPalindromicSubsequenceOptimised("bbcbaba"))
print(countPalindromicSubsequence("zqpppgacudvmqekmefkzyyfrffeylqrwxlupvskyonqsbclwwgnzbktzelwuhehxrxmqcnepxokialxxwciqsetcsqcsszpeobeiwwedtbisyhexyatammupmfrllpawhqvfebjdappicczehrsooztjatixvtvbmdwikffbozncspuslwgoqypmsmvwghfdmutfpkbjufqrgbhotcikoyvfvxmmadelwxmvybnoroapixubdvijnepeduiwshcwjvhnejafcnuxeimwiiucznzfakwdibwwixcttatqffhnurhecyocoohyuoeixobaxbjcksxqrljiftvcxtocusciqtmydxgjexiwimbcmvhjonkscobhlpggembfslzoisertsvcpiclikprpviqbfdptvtrlhqlfwhurxysxzppnwwbxzaozchalpqsklfedovjkhwdaqdxrzdduwxsyqllvkflamtshyoaamjpzcsnwthnnpgqrrroppxnalxoijzhesphugqporhtamdbugqhgtpxtrjeugenazzpvvtkjrsepvbgvbmmmyxgrkgnlhujinycnjvpqhhugplrgrunrziaabknrjsgaqbpxfpdycpjtquecehrblzurruguhbkzgvebzfkqcolpclgabsuamqaakdikasumksvbfjrudnzihbzqjwivthfozrhkcrmxleaazgkuqmzvzaiiskfrnywntgbtmaxqgqaqxvcpvbvcpqbfivtkdroizfbebhtejegpduqjewcaysphsumddhlgerpspcvhkoezzqwznmqfbcdvxmexbjfgqxlcbneanbglpktxfcfgkfxbpblfpejlfjhiaohcmktfheuyxpof"))