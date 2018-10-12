


def mostCommonChar(s):
  dic = {}
  mostCommon = ''
  maxFreq = 0
  for i in s:
    dic[i] = dic.get(i,0) + 1
    if dic[i] > maxFreq:
      mostCommon = i
      maxFreq = dic[i]
  return mostCommon


test = "abcdefabdfgfco"
print(mostCommonChar(test))