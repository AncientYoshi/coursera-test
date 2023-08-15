menu = ["coffee", "capachino", "collarine", "americano", "espresso"]


def find_coffee(coffee):
    if coffee[0] == "c":
        return coffee


map_coffee = map(find_coffee, menu)
print(list(map_coffee))

filter_coffee = filter(find_coffee, menu)
# print(list(filter_coffee))
for i in filter_coffee:
    print(i)
