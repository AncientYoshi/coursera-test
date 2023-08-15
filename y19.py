def reverse_function(string):
    if len(string) == 0:
        return string
    else:
        return reverse_function(string[1:]) + string[0]


print(reverse_function("hello"))
