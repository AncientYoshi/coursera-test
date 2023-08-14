with open("sampletext.txt", "r") as f:
    file = f.readlines()

for i in range(1):
    print(file[i])

for i in range(2, 3):
    print(file[i])
