
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizUI:
    
    def __init__(self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        
        
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        
        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg='white')
        self.question_text = self.canvas.create_text(150,125, text='stuff',font=('Arial',20,'italic'),width=280,fill=THEME_COLOR)
        self.canvas.grid(row=1,columnspan=2,pady=50)
        
        self.score_text = Label(text=f'Score:0',font=('Arial',13,'normal'),bg=THEME_COLOR,fg='white')
        self.score_text.grid(column=1,row = 0)
        
        RIGHT_BUTTON = PhotoImage(file=r'S:\Code_Projects\100 Days of Python\Day34\Quiz App with API\images\true.png')
        WRONG_BUTTON = PhotoImage(file=r'S:\Code_Projects\100 Days of Python\Day34\Quiz App with API\images\false.png')
        
        self.right_button = Button(image=RIGHT_BUTTON, highlightthickness=0,bg=THEME_COLOR,command=self.true_pressed)
        self.right_button.config(pady=50)
        self.right_button.grid(row=2)
        
        self.wrong_button = Button(image=WRONG_BUTTON, highlightthickness=0,bg=THEME_COLOR,command=self.false_pressed)
        self.wrong_button.config(pady=50)
        self.wrong_button.grid(column=1,row=2)
        

        
        
        self.get_next_question()
        
        self.window.mainloop()
        
    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_text.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text='End of quiz!')
            self.right_button.config(state='disabled')
            self.wrong_button.config(state='disabled')
        
    def true_pressed(self):
        is_right = self.give_feedback(self.quiz.check_answer('True'))
        
    def false_pressed(self):
        is_right = self.give_feedback(self.quiz.check_answer('False'))
    
    
    
    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000,self.get_next_question)