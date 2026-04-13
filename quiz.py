class InvalidOptionError(Exception):
    pass

class Quiz:
    def __init__(self):
        # Questions list
        self.questions = [

            "1. Smallest planet?\nA. Earth\nB. Mercury\nC. Jupiter",
            "2. 50 + 3 = ?\nA. 6\nB. 53\nC. 10",
            "3. Capital of Finland?\nA. Helsinki\nB. Delhi\nC. Ethiopia",
            "4. H2O is a chemical formula for?\nA. Water\nB. Ammonia\nC. Oxygen",
            "5. Sun sets in?\nA. East\nB. West\nC. North",
            "6. 100 * 20 = ?\nA. 2000\nB. 150\nC. 2500",
            "7. Fastest water animal?\nA. Lion\nB. Sailfish\nC. Tiger",
            "8. State animal of TN?\nA. Lion\nB. Nilgiri Tahr\nC. Elephant"
        ]

        # Correct answers
        self.answers = ['C', 'B', 'A', 'A', 'B', 'A', 'B', 'B', ]

        # Score variable
        self.score = 0

    def start_quiz(self):
        for i in range(len(self.questions)):
            while True:  # Loop until valid input
                try:
                    print("\n" + self.questions[i])
                    user_ans = input("Enter option (A/B/C): ").upper()

                    if user_ans not in ['A', 'B', 'C']:
                        raise InvalidOptionError("Invalid option selected!")

                    # Check answer
                    if user_ans == self.answers[i]:
                        print("CORRECT!")
                        self.score += 1
                    else:
                        print("Wrong :(")

                    break  # Exit loop after valid input

                except InvalidOptionError as e:
                    print(e)

    def display_score(self):
        print("\nQuiz Completed!")
        print(f"Your final score is: {self.score} / {len(self.questions)}")

# Create object and call methods
q = Quiz()
q.start_quiz()
q.display_score()
