class re:
    def __init__(self, d, name, type, value) -> None:
        self.d = d
        self.name = name
        self.type = type
        self.value = value

    def contents(self):
        return self.d, self.name, self.type, self.value


pizza = re("Meat Pizzas", "LApzilla", "Nice Pizzas", 5000)
burger = re("Hamburger", ["Milk", "Yogur"], ["Tengin"], 2100)

print(pizza.name)
print(burger.name)

print(pizza.contents())
