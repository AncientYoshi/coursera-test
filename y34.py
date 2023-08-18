class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class supervisor(Employee):
    def __init__(self, name, salary, password):
        super().__init__(name, salary)
        self.supervisor = None
        self.password = password


class chef(Employee):
    def leave_request(self, days):
        return "may I take a leave request for " + days + " days"


emery = Employee("Honey", "970000")

anni = supervisor("Annie", "900000", "93278859")
emery = chef("Mannan", "8799990")

print(emery.leave_request("7"))
print(anni.password)
print(emery.name)
