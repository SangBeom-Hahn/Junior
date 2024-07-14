from collections import Counter

def MinWindowSubstring(strArr):
  n = strArr[0]
  k = strArr[1]

  cntK = Counter(k)
  min_leng = 51
  result = ""

  for i in range(len(n) - len(k) + 1):
    part_string = ""
    for j in range(i, len(n)):
      part_string += n[j]

      
      if(len(part_string) < len(k)):
        continue
      
      cntPart = Counter(part_string)

      if(len(cntK - cntPart) == 0):
        if(min_leng > len(part_string)):
          min_leng = len(part_string)
          result = part_string
  # print(result)

  # code goes here
  return result


# keep this function call here 
print(MinWindowSubstring(input()))