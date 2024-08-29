from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Question", fill="black",
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        wrong = PhotoImage(file="images/false.png")
        self.false = Button(image=wrong, highlightthickness=0, command=self.is_wrong)
        self.false.grid(row=2, column=0)

        right = PhotoImage(file="images/true.png")
        self.true = Button(image=right, highlightthickness=0, command=self.is_right)
        self.true.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.false.config(state="normal")
        self.true.config(state="normal")
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            quiz_ques = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=quiz_ques)
        else:
            self.canvas.itemconfig(self.question_text, text="You reached at the end of the quiz!!")
            self.true.config(state="disabled")
            self.false.config(state="disabled")
        score = self.quiz.score
        self.score.config(text=f"Score: {score}")

    def is_right(self):
        result = self.quiz.check_answer("True")
        self.true.config(state="disabled")
        self.false.config(state="disabled")
        self.give_feedback(result)


    def is_wrong(self):
        result = self.quiz.check_answer("False")
        self.false.config(state="disabled")
        self.true.config(state="disabled")
        self.give_feedback(result)

    def give_feedback(self, result):
        if result:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

