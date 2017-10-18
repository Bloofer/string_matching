import sys

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

# The checker seeks pattern in text with naive algorithm

def check_pattern(p, q):
  p_i = 0
  p_j = 0

  for m in range(p, p + p_size):
    p_j = 0
    for n in range(q, q + p_size):
      if text[m][n] != pattern[p_i][p_j]:
        return False
      p_j += 1
    p_i += 1
  return True

rlist = list()

for i in range(0, t_size - p_size + 1):
  for j in range(0, t_size - p_size + 1):
    if check_pattern(i, j): rlist.append((str(i + p_size - 1) + ' ' + str(j + p_size - 1)))

input_file = open(str(sys.argv[2]), 'r')
o = input_file.read().splitlines()

output_file = open(str(sys.argv[3]), 'w')

rlist.sort()

if rlist == o:
  output_file.write('yes')
else:
  output_file.write('no')

