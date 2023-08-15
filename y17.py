def iscanrev(string):
    string_index = 0
    string_end_index = len(string) - 1

    for i in range(int(len(string) / 2)):
        string_index = string_index + 1
        string_end_index = string_end_index - 1
        if string[string_index] != string[string_end_index]:
            return False

    return True


print(iscanrev("urocecopru"))
