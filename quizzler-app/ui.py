from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizIntrface:
    def __init__(self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.user_answer: str
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR,)
        self.score = 0
        self.score_label = Label(text=f"Score: {self.score}",bg=THEME_COLOR,font=("Arial,20,italic"),fg="White")

        self.score_label.config(padx=20,pady=20)
        self.score_label.grid(row=0,column=1)
        self.canvas = Canvas(width=300,height=250,bg="white")
        self.question_text = self.canvas.create_text(150,
                                                125,
                                                width=280,
                                                text="lalala",
                                                font=("Arial",20,"italic"),fill=THEME_COLOR)
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)
        true_img = PhotoImage(file="quizzler-app/images/true.png")
        false_img = PhotoImage(file="quizzler-app/images/false.png")

        self.true_button = Button(image=true_img,width=95,
                                  height=95,
                                  highlightthickness=0,
                                  command=self.true_button_clicked)
        self.false_button = Button(image=false_img,
                                   width=95,
                                   height=95,
                                   highlightthickness=0,
                                   command=self.false_button_clicked)
        self.true_button.grid(row=2,column=0)
        self.false_button.grid(row=2,column=1)
 
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="White")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            
    def update_score(self):
        if self.quiz.check_answer(self.user_answer):
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.canvas.config(bg="Green")
        else:
            self.canvas.config(bg="Red")
        self.window.after(1000,self.get_next_question)

    def true_button_clicked(self):
        self.user_answer = "True"
        self.update_score()

    def false_button_clicked(self):
        self.user_answer = "False"
        self.update_score()
