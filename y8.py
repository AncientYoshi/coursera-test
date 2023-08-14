def divide_by(x, y):
    return x / y


try:
    print(divide_by(10, 0))
except ZeroDivisionError as e:
    print(e, "we cannot divide by zero")
except Exception as e:
    print("Something went wrong", e)
