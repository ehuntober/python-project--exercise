

# file = input('Enter the file name: ')

# fhand = open(file)
# count = 0
# for line in fhand:
# 	count = count + 1
# print(f"There were {count} subject line in {file}")

# fname = input('Enter the file name: ')
# try:
# 	fhand = open(fname)

# except:
# 	print('File cannot be opend: ' fname)
# 	exit()

# count = 0
# for line in fhand:
# 	if line.startswith('Subject:'):
# 		count = count + 1

# print(f'There were {count} subject lines in  {fname}')




fname = input('Enter the file name: ')
try:
	fhand = open(fname)

except:
	print('File cannot be opened:', fname)
	exit()

count = 0
for line in fhand:
	if line.startswith('Subject:'):
		count = count + 1
print('There were', count, 'subject lines in', fname)









