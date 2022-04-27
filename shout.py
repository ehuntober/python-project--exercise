
file = input("Enter a file name: ")
try:
	with open(file) as f:
		for line in f:
			count = 0
			count = count + 1
			print(line.upper())
		print(f"There were {count} subject line in {file}")	
except:
	print('file not found')