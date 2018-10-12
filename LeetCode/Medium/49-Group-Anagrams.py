'''
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
'''

def groupAnagrams(self, strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    d = {}
    for s in strs:
        ss = tuple(sorted(s))
        d[ss] = d.get(ss, []) + [s]
    return list(d.values())

    # O(n * (k)log(k))