##write a function to find the length of the longest substring containing the same letter in a given string s
# after performing at most k operations (number of times you can change letter)

# in order for a substring to be valid, k + the frequency of the most frequent character 
# must be greater than or equal to the length of the substring

#example: if k = 2, and subtring is AABBB, most freq char is B, 2+3 > = 5
# but if k = 2 and substring is AAABBB, then substring is invalid bc 2+3 < 6, (not all of them can be changed)

def characterReplacement(s, k):
    state = {}
    max_freq = 0
    max_length = 0
    start = 0

    for end in range(len(s)):
        state[s[end]] = state.get(s[end], 0) + 1
        max_freq = max(max_freq, state[s[end]])

        if k + max_freq < end - start + 1:
            state[s[start]] -= 1
            start += 1
        
        max_length = max(max_length, end - start + 1)
    
    return max_length