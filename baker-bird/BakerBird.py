import Kmp
import AhoCorasick

input_file = open('bb_in.txt', 'r')
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
  root = AhoCorasick.aho_create_statemachine(patterns)
  R.append(AhoCorasick.aho_find_all(txt, root, AhoCorasick.on_occurence, nu_pattern))

nu_r = [[0, 0, 0, 0 ,0, 0, 0, 0, 0, 0], [0, 0, 0, 0 ,0, 0, 0, 0, 0, 0], [0, 0, 0, 0 ,0, 0, 0, 0, 0, 0], [0, 0, 0, 0 ,0, 0, 0, 0, 0, 0], [0, 0, 0, 0 ,0, 0, 0, 0, 0, 0], [0, 0, 0, 0 ,0, 0, 0, 0, 0, 0], [0, 0, 0, 0 ,0, 0, 0, 0, 0, 0], [0, 0, 0, 0 ,0, 0, 0, 0, 0, 0], [0, 0, 0, 0 ,0, 0, 0, 0, 0, 0], [0, 0, 0, 0 ,0, 0, 0, 0, 0, 0]]

for index, r in enumerate(R):
  for idx, ptn in r:
    nu_r[index][idx + len(pattern[0]) - 1] = ptn

"""
for i in range(0,9):
  for j in range(0,10):
    print nu_r[i][j],
  print '\n'
"""

# KMP

def column(matrix, i):
  return [row[i] for row in matrix]

rlist = list()

for i in range(0, 10):
  result = Kmp.KMP().search(column(nu_r, i), p_num)
  if len(result) != 0:
    for res in result:
      rlist.append((res + 4, i))

output_file = open('bb_out.txt', 'w')

rlist.sort()
for rl, rr in rlist:
  print rl, rr
  output_file.write(str(rl) + ' ' + str(rr) + '\n')

# print column(nu_r, 9)


