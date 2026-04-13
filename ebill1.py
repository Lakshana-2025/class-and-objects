class ElectricityBill:
    def __init__(self, units):
        self.units = units
        self.bill_amount = 0

    def calculate_bill(self):
        if self.units <= 100:
            self.bill_amount = 0
        elif self.units <= 200:
            self.bill_amount = (self.units - 100) * 1.5
        elif self.units <= 300:
            self.bill_amount = (100 * 0) + (100 * 1.5) + (self.units - 200) * 2.5
        elif self.units <= 400:
            self.bill_amount = (100 * 0) + (100 * 1.5) + (100 * 2.5) + (self.units - 300) * 4
        else:
            self.bill_amount = (100 * 0) + (100 * 1.5) + (100 * 2.5) + (100 * 4) + (self.units - 400) * 5

    def display_bill(self):
        print(f"Total units consumed: {self.units}")
        print(f"Total electricity bill amount: {self.bill_amount:.2f}")

user_units = int(input("Enter the total units consumed: "))

bill_calculator = ElectricityBill(user_units)
bill_calculator.calculate_bill()
bill_calculator.display_bill()
