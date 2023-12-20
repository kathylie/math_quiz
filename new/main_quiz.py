import random 

class SimpleMathQuiz:
    def __init__(self):
        self.score = 0
        self.num_correct = 0
        self.num_wrong = 0
        self.level = 1
        self.operator = "Addition"
        self.max_difference = 10

    def generate_question(self):
        """Generate a random math question based on the current level and operator."""
        if self.operator == "Addition":
            num1 = random.randint(1, self.level * 10)
            num2 = random.randint(1, self.level * 10)
            correct_answer = num1 + num2
        elif self.operator == "Subtraction":
            num1 = random.randint(self.level * 10, self.level * 20)
            num2 = random.randint(1, self.level * 10)
            correct_answer = num1 - num2
        elif self.operator == "Multiplication":
            num1 = random.randint(1, self.level * 5)
            num2 = random.randint(1, self.level * 5)
            correct_answer = num1 * num2
        else:
            # Custom operator handling (you can add more operators as needed)
            print("Invalid operator")
            return None

        return f"{num1} {self.operator} {num2}", correct_answer

    def start_quiz(self):
        while True:
            print("Simple Mathematics Quiz")
            print(f"Level: {self.level} | Operator: {self.operator}")
            print("[1] Start Quiz")
            print("[2] Settings")
            print("[3] Close")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.run_quiz()
            elif choice == "2":
                self.update_settings()
            elif choice == "3":
                print("Closing the quiz. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")

    def run_quiz(self):
        num_items = int(input("Enter the number of items for the quiz: "))
        for _ in range(num_items):
            question, correct_answer = self.generate_question()
            user_answer = int(input(f"{question} = "))
            
            if user_answer == correct_answer:
                print("Correct!\n")
                self.num_correct += 1
            else:
                print(f"Wrong! The correct answer is {correct_answer}\n")
                self.num_wrong += 1

        self.score = self.num_correct * 10
        print(f"Quiz completed. Score: {self.score}\n")

    def update_settings(self):
        print("Settings Menu")
        print("[1] Level")
        print("[2] Operator")
        print("[3] Max difference of choices from the correct answer")
        print("[4] Back to Main Menu")

        setting_choice = input("Enter your choice: ")

        if setting_choice == "1":
            self.level = int(input("Enter the level (1-10): "))
        elif setting_choice == "2":
            print("Available Operators:")
            print("[1] Addition")
            print("[2] Subtraction")
            print("[3] Multiplication")
            operator_choice = input("Enter your choice: ")

            if operator_choice == "1":
                self.operator = "Addition"
            elif operator_choice == "2":
                self.operator = "Subtraction"
            elif operator_choice == "3":
                self.operator = "Multiplication"
            else:
                print("Invalid operator choice.")
        elif setting_choice == "3":
            self.max_difference = int(input("Enter the max difference of choices from the correct answer: "))
        elif setting_choice == "4":
            return
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    math_quiz = SimpleMathQuiz()
    math_quiz.start_quiz()
