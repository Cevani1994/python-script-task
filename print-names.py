# This program prints Hello, world!
print('Hello, world!')

print('===================================================================')

# Print all names of names.txt file
f = open("names.txt", "r")
print(f.read())

print('===================================================================')


# Prints all dublicate on names.txt file
with open('names.txt') as f:
    seen = set()
    for line in f:
        line_lower = line.lower()
        if line_lower in seen:
            print(line)
        else:
            seen.add(line_lower)


print('===================================================================')


# Prints the number of dublicates in names.txt
import collections

with open('names.txt') as infile:
    counts = collections.Counter(l.strip() for l in infile)
for line, count in counts.most_common():
    print(line, count) 
