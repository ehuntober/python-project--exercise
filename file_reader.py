# with open('pi_digits.txt') as file_object:
# 	contents = file_object.read()
# print(contents)

# fhand = open('pi_digits.txt')
# count = 0
# for line in fhand:
# 	count = count + 1
# print('Line Count: ', count)

# fhand = open('pi_digits.txt')
# inp = fhand.read()
# # print(len(inp))
# print(inp[:20])

# fhand = open('pi_digits.txt')
# for line in fhand:
# 	line = line.rstrip()
# 	if line.startswith('From:'):
# 		print(line)


fhand = open('pi_digits.txt')
for line in fhand:
	line = line.rstrip()

	if not line.startswith('From'):
		continue
	print(line)