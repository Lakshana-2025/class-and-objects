class ExceptionDemo:

    def divide(self):
        try:
            a = int(input("Enter numerator: "))
            b = int(input("Enter denominator: "))
            result = a / b
            print("Result:", result)

        except ZeroDivisionError:
            print("Error: Divide by zero occurred")

        except ValueError:
            print("Error: Input not in specified data type")

    def access_list(self):
        try:
            lst = [100, 280, 3080, 4650, 5320]
            print("List:", lst)

            index = int(input("Enter index to access: "))
            print("Element:", lst[index])

        except IndexError:
            print("Error: Index greater than length of list")

        except ValueError:
            print("Error: Input not in specified data type")

    def access_dict(self):
        try:
            d = {"X": 10, "Y": 20, "Z": 30}
            print("Dictionary:", d)

            key = input("Enter key to access value: ")
            print("Value:", d[key])

        except KeyError:
            print("Error: Key not found in dictionary")

# Main program
obj = ExceptionDemo()

print("\n--- Division ---")
obj.divide()

print("\n--- List Access ---")
obj.access_list()

print("\n--- Dictionary Access ---")
obj.access_dict()
