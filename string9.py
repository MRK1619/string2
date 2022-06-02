# Longest Repeating Character
import collections
from numpy import arange
class Solution(object):
    def characterReplacement(self, s, k):
        result, max_count = 0, 0
        count = collections.Counter()
        for i in arange(len(s)):
            count[s[i]] += 1
            max_count = max(max_count, count[s[i]])
            if result - max_count >= k:
                count[s[i-result]] -= 1
            else:
                result += 1
        return result
ob1=Solution()
print(ob1.characterReplacement(s = "AABABBA", k = 1)) 
