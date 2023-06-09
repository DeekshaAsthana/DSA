class Solution:

    def longestKSubstr(self, s, k):
        l = 0
        count = {}
        maxLen = float("-inf")

        for r in range(len(s)):
            if s[r] not in count:
                count[s[r]] = 0
            count[s[r]] +=1


            while len(count) > k:
                count[s[l]] -=1
                if count[s[l]] == 0:
                    del count[s[l]]
                l+=1

            if len(count) == k:
                maxLen = max(maxLen, r-l+1)

        return -1 if maxLen == float("-inf") else maxLen
