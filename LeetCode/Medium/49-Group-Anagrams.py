'''
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
'''

def groupAnagrams(strs):
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


def checkIfAnagram(s,t):
  letters = {}
  for i in s:
    letters[i] = letters.get(i,0) + 1

  for j in t:
    letters[j] = letters.get(j,0) - 1

  for v in letters.values():
    if v != 0:
      return False

  return True

print(checkIfAnagram("cat", "act"))

