from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"



class QuizInterface:

    def __init__(self,quizz:QuizBrain):
        self.quizz = quizz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)

        self.label = Label(text=f"Score:{self.quizz.score}",bg=THEME_COLOR,borderwidth=0)
        self.label.grid(column=1,row=0)

        self.canvas = Canvas(height=250,width=300,bg="white",borderwidth=0,highlightthickness=0)
        self.q_t = self.canvas.create_text(150,125,
                                           text="some question",
                                           fill=THEME_COLOR,
                                           font=("Arial",20,"italic"),
                                           width=280)
        self.canvas.grid(column=0,row=1,columnspan=2,pady=50)


        true_image = PhotoImage(file="images/true.png")
        self.right_button = Button(image=true_image,borderwidth=0,command=self.right_button_pressed)
        self.right_button.grid(column=0,row=2)
        self.right_button.config(padx=20,pady=20)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image,borderwidth=0,command=self.wrong_button_pressed)
        self.false_button.grid(column=1,row=2)
        self.false_button.config(padx=20, pady=20)


        self.next_question()

        self.window.mainloop()



    def next_question(self):
        if self.quizz.still_has_questions():
            next_q = self.quizz.next_question()
            self.canvas.itemconfig(self.q_t,text=next_q)
        else:
            self.canvas.itemconfig(self.q_t,text= f"you've reached end of the quiz,"
                                                  f"your final score {self.quizz.score} / {self.quizz.question_number}")
            self.right_button.config(state="disabled")
            self.false_button.config(state="disabled")




    def right_button_pressed(self):
        is_true = self.quizz.check_answer("True")
        self.give_feed_back(is_true)

    def wrong_button_pressed(self):
        is_true = self.quizz.check_answer("False")
        self.give_feed_back(is_true)


    def change_color(self):
        self.canvas.config(bg="white")
        self.next_question()

    def give_feed_back(self,is_true):
        if is_true == True:
            self.canvas.config(bg="green")
            self.label.config(text=self.quizz.score)
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, func=self.change_color)














