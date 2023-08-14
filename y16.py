# even read lines from text files

rfile = open(r"sampletext.txt")
li = []

c = rfile.readlines()

for i in range(0, len(c)):
    if i % 2 != 0:
        li.append(c[i])

print(li)
