# 3. Longest Substring Without Repeating Characters
# Given a string, find the length of the longest substring without repeating characters.

def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        maxLen = 0
        dic = {}
        length = len(s)

        for i in range(length):
            # check if character is repeated within the current running word
            if s[i] in dic and start <= dic[s[i]]:
                # This is like a rolling window.
                # If you see a letter again, you exclude that letter from the start and count the second occurence.
                # Set the new running word to start from the last time char was seen + 1
                start = dic[s[i]] + 1
                # print(start, i, s[i])
            else:
                # max word is either current running word or not
                maxLen = max(maxLen, i - start + 1)

            dic[s[i]] = i

        return maxLen
