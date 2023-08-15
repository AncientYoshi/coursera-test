usingrange = {x: x * 2 for x in range(12)}
print("Using range(): ", usingrange)

months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "June",
    "July",
    "Aug",
    "Sept",
    "Oct",
    "Nov",
    "Dec",
]
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

numdict = {x: x**2 for x in number}
print("Using one input list to create dict: ", numdict)

months_dict = {key: value for (key, value) in zip(number, months)}
print("Using two lists: ", months_dict)
