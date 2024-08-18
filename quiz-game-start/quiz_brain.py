class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ").title()
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, u_answer, c_answer):
        if u_answer == c_answer:
            self.score += 1
            print("You are correct.")
        else:
            print("You are wrong")
        print(f"The correct answer is: {c_answer}")
        print(f"Your score is: {self.score}/{self.question_number}")
        print("\n")

    def show_final_result(self):
        print(f"Thanks for participating in the Quiz. Here is ur final result: {self.score}/{self.question_number}.")
