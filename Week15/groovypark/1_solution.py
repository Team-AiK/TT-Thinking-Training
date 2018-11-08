class Solution:
    def lengthOfLongestSubstring(self, s):
        answer = [0]
        for i in range(len(s)):
            cur = ""
            count = 0
            sub_str = s[i:]
            for _s in sub_str:
                if _s not in cur:
                    cur += _s
                    count += 1
                else:
                    break
            answer.append(count)
        return max(answer)