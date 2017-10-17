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

print pattern
print text

