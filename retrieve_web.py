

# import urllib.request , urllib.parse , urllib.error

# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# for line in fhand:
# 	print(line.decode().strip())



# import urllib.request, urllib.parse, urllib.error
# counts = dict()
# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# for line in fhand:
# 	words = line.decode().split()
# 	for word in words:
# 		counts[word] = counts.get(word, 0) + 1
# print(counts)


import urllib.request, urllib.parse, urllib.error
import re
url = input('Enter - ')
html = urllib.request.urlopen(url).read()

links = re.findall(b'href="(http://.*?"',html)
for link in links:
	print(link.decode())