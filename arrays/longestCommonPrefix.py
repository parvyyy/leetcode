def longestCommonPrefix(strs):
    prefix = []
    longest_word, shortest_word = max(strs, key=len), min(strs, key=len)
    
    for i in range(len(shortest_word)):
        for word in strs:
            if word[i] is not longest_word[i]:
                return ''.join(prefix)
            
        prefix.append(longest_word[i])   
    
    return ''.join(prefix)
        

def main():
    print(longestCommonPrefix(["flowers", "flow", "flight"]))
    print(longestCommonPrefix(["dog","racecar","car"]))
    return 0

if __name__ == "__main__":
    main()       