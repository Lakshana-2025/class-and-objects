class Employee:
    def __init__(self, name, basic_salary):
        self.name = name
        self.basic_salary = basic_salary
        self.da = 0
        self.hra = 0
        self.gross_pay = 0
        self.final_salary = 0
        self.pf = 0

    def calculate_salary(self):
        self.da = self.basic_salary * 0.50
        self.hra = self.basic_salary * 0.20
        self.gross_pay = self.basic_salary + self.da + self.hra
        self.final_salary = self.gross_pay

    def display_details(self):
        print(f"\nEmployee Name: {self.name}")
        print(f"Basic Salary: {self.basic_salary}")
        print(f"DA (50%): {self.da}")
        print(f"HRA (20%): {self.hra}")
        print(f"Gross Pay: {self.gross_pay}")
        print(f"Final Salary (Net Pay): {self.final_salary}")

def get_employee_details():
    name = input("Enter employee name: ")
    while True:
        try:
            basic_salary = float(input("Enter basic salary: "))
            if basic_salary <= 0:
                print("Basic salary must be positive. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numerical value for salary.")
    return Employee(name, basic_salary)

employees = []
while True:
    new_employee = get_employee_details()
    new_employee.calculate_salary()
    employees.append(new_employee)

    another_employee = input("\nDo you want to enter details for another employee? (yes/no): ")
    if another_employee.lower() != 'yes':
        break

print("\n--- All Employee Details ---")
for employee in employees:
    employee.display_details()
