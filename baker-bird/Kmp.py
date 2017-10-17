class KMP:
  def partial(self, pattern):
    """ Calculate partial match table: String -> [Int] """
    ret = [0]

    for i in range(1, len(pattern)):
      j = ret[i - 1]
      while j > 0 and pattern[j] != pattern[i]:
        j = ret[j - 1]
      ret.append(j + 1 if pattern[j] == pattern[i] else j)
    return ret

  def search(self, T, P):
    """ KMP search main algorithm: String -> String -> [int] """
    partial, ret, j = self.partial(P), [], 0

    for i in range(len(T)):
      while j > 0 and T[i] != P[j]:
        j = partial[j - 1]
      if T[i] == P[j]: j += 1
      if j == len(P):
        ret.append(i - (j - 1))
        j = 0

    return ret

kmp1 = KMP()
result = kmp1.search(['a','a','b','a','b','a','b','b','c','a','b','a','b','b','a','c','a'], ['c','a'])
for p in result: print p
