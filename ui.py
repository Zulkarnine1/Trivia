from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"

class QuizUI:

    def __init__(self,quiz:QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Trivia")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        self.lbl1 = Label(text="Score: 0",bg=THEME_COLOR,fg="white",font=("Arial",15,"normal"))
        self.lbl1.grid(column=1,row=0)
        self.Canv1 = Canvas(width=400,height=300,bg="white")
        self.CanvText = self.Canv1.create_text(200,150,text="Quiz question",font=("Arial",20,"italic"),width=380)
        self.Canv1.grid(column=0,row=1,columnspan=2,pady=50)
        img1 = PhotoImage(file="images/false.png")
        self.falseBtn = Button(image = img1 ,highlightthickness=0,command=self.check_answer2)
        self.falseBtn.grid(column=1,row=3)
        img2 = PhotoImage(file="images/true.png")
        self.trueBtn = Button(image=img2,highlightthickness=0,command=self.check_answer1)
        self.trueBtn.grid(column=0, row=3)
        self.get_next_quesiton()
        self.window.mainloop()

    def get_next_quesiton(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.Canv1.itemconfig(self.CanvText,text=q_text)
        else:
            self.Canv1.itemconfig(self.CanvText, text="You've reached the end of the quiz")
            self.falseBtn.config(state="disabled")
            self.trueBtn.config(state="disabled")


    def check_answer1(self):
        ans = "true"
        cor = self.quiz.check_answer(ans)
        self.give_feedback(cor)


    def check_answer2(self):
        ans = "false"
        cor = self.quiz.check_answer(ans)
        self.give_feedback(cor)

    def give_feedback(self,cor):
        if cor:
            self.Canv1.config(bg="green")

        else:
            self.Canv1.config(bg="red")
        self.window.after(1000, func=self.reset_board)


    def reset_board(self):
        self.Canv1.config(bg="white")
        self.lbl1.config(text=f"Score: {self.quiz.score}")
        self.get_next_quesiton()




