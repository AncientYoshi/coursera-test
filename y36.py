class payslip:
    def __init__(self, name, payment, amount) -> None:
        self.name = name
        self.payment = payment
        self.amount = amount

    def pay(self):
        self.payment = "yes"

    def status(self):
        if self.payment == "yes":
            return self.name + " (paid) " + self.amount
        else:
            return self.name + " (unpaid) " + self.amount


pai = payslip("Pai", "yes", "10000")
print(pai.status())
Yoshi = payslip("Yoshi", "no", "2000")
print(Yoshi.status())
