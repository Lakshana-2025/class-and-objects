[25bcs146@mepcolinux ex5py]$cat stddetails.py
class Student:
    def __init__(self, name):
        self.name = name
        self.marks = []
        self.total_marks = 0
        self.average_marks = 0
        self.grade = ""

    def input_marks(self):
        print(f"Enter marks for {self.name} in five subjects:")
        for i in range(5):
            while True:
                try:
                    mark = float(input(f"Subject {i + 1} mark: "))
                    if 0 <= mark <= 100:
                        self.marks.append(mark)
                        break
                    else:
                        print("Invalid marks. Please enter a value between 0 and 100.")
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")

    def calculate_results(self):
        self.total_marks = sum(self.marks)
        self.average_marks = self.total_marks / 5
        self.determine_grade()

    def determine_grade(self):
        if self.average_marks >= 90:
            self.grade = "A"
        elif self.average_marks >= 80:
            self.grade = "B"
        elif self.average_marks >= 70:
            self.grade = "C"
        elif self.average_marks >= 60:
            self.grade = "D"
        else:
            self.grade = "F"

    def display_details(self):
        print("\nStudent Details:")
        print(f"Name: {self.name}")
        print(f"Total Marks: {self.total_marks}")
        print(f"Average Marks: {self.average_marks:.2f}")
        print(f"Grade: {self.grade}")

def main():
    student_name = input("Enter student name: ")
    student1 = Student(student_name)
    student1.input_marks()
    student1.calculate_results()
    student1.display_details()

if __name__ == "__main__":
    main()
