import AhoCorasick
import Kmp

# Aho-Corasick

pattern = ["aabba", "aaabb", "ababa", "aabba", "aaabb"]
nu_pattern = dict()
p_num = list()

for st in pattern:
  if not(st in nu_pattern):
    nu_pattern[st] = len(nu_pattern) + 1
  p_num.append(nu_pattern[st])

text = ["aabbaaabba", "aaabbaaabb", "ababaababa", "aabbaaabba", "aaabbaaabb", "baaabbabab", "aababaabba", "aaabbaaabb", "baaabbaaab"]
nu_text = list()

patterns = nu_pattern.keys()

# Making R

R = list()

for txt in text:
  root = AhoCorasick.aho_create_statemachine(patterns)
  R.append(AhoCorasick.aho_find_all(txt, root, AhoCorasick.on_occurence, nu_pattern))

nu_r = [[0, 0, 0, 0 ,0, 0, 0, 0, 0, 0], [0, 0, 0, 0 ,0, 0, 0, 0, 0, 0], [0, 0, 0, 0 ,0, 0, 0, 0, 0, 0], [0, 0, 0, 0 ,0, 0, 0, 0, 0, 0], [0, 0, 0, 0 ,0, 0, 0, 0, 0, 0], [0, 0, 0, 0 ,0, 0, 0, 0, 0, 0], [0, 0, 0, 0 ,0, 0, 0, 0, 0, 0], [0, 0, 0, 0 ,0, 0, 0, 0, 0, 0], [0, 0, 0, 0 ,0, 0, 0, 0, 0, 0]]

for index, r in enumerate(R):
  for idx, ptn in r:
    nu_r[index][idx + len(pattern[0]) - 1] = ptn

for i in range(0,9):
  for j in range(0,10):
    print nu_r[i][j],
  print '\n'

# KMP

def column(matrix, i):
  return [row[i] for row in matrix]

for i in range(0, 10):
  print Kmp.KMP().search(column(nu_r, i), p_num)

# print column(nu_r, 9)



