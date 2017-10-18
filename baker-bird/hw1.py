# Baker-Bird algorithm for 2-D pattern matching
# Using Aho-Corasick algorithm & KMP algorithm

import Kmp
import AhoCorasick
import sys

# opens input file and reads text & pattern
input_file = open(str(sys.argv[1]), 'r')
f = input_file.read().splitlines()
firstline = f[0]
p_size = int(firstline.split()[0])
t_size = int(firstline.split()[1])

pattern = list()
for p_line in range(1, 1 + p_size):
  pattern.append(f[p_line])
text = list()
for t_line in range(1 + p_size, 1 + p_size + t_size):
  text.append(f[t_line])

# Aho-Corasick
nu_pattern = dict()
p_num = list()

for st in pattern:
  if not(st in nu_pattern):
    nu_pattern[st] = len(nu_pattern) + 1
  p_num.append(nu_pattern[st])
nu_text = list()

patterns = nu_pattern.keys()

# Making R
R = list()

for txt in text:
  root = AhoCorasick.add_trie_ff(patterns)
  R.append(AhoCorasick.find_pattern(txt, root, nu_pattern))

nu_r = [[0 for x in range(t_size)] for y in range(t_size)] 

for index, r in enumerate(R):
  for idx, ptn in r:
    nu_r[index][idx + len(pattern[0]) - 1] = ptn

# KMP
def column(matrix, i):
  return [row[i] for row in matrix]

rlist = list()

for i in range(0, t_size):
  result = Kmp.KMP().search(column(nu_r, i), p_num)
  if len(result) != 0:
    for res in result:
      rlist.append((res + p_size - 1, i))

# writes out the result of the pattern search
output_file = open(str(sys.argv[2]), 'w')

rlist.sort()
for rl, rr in rlist:
  output_file.write(str(rl) + ' ' + str(rr) + '\n')

