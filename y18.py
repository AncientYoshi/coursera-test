y = "Despicables"
test = y[::-1]

print("Testing", test)

for i in range(len(test)):
    if test[i] == y[i]:
        print("Correct")
    else:
        print("Incorrect")
