
def longestSubstring(s):
    state = {}
    start = 0
    max_ = 0

    for end in range(len(s)):
        state[s[end]] = state.get(s[end], 0) + 1

        while state[s[end]] > 1:
            state[s[start]] -= 1
            if state[s[start]] == 0:
                del state[s[start]]
            start+=1
        
        max_ = max(max_, end-start + 1)

    return max_
