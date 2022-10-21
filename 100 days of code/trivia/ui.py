import tkinter
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = tkinter.Tk()
        self.window.config(padx = 20, pady = 20, bg = THEME_COLOR)
        self.window.title("Quizzler")

        #Question
        self.canvas = tkinter.Canvas(height = 250, width = 300)
        self.question_text = self.canvas.create_text(150, 125, text = "Question", fill = THEME_COLOR, width = 280, font = ("Ariel", 20, "italic"))
        self.canvas.grid(row = 1, column = 0, columnspan = 2, pady = 50)

        # Score
        self.score = tkinter.Label(text = "Score: 0", fg = "white", bg = THEME_COLOR)
        self.score.grid(row=0, column = 1)

        # Buttons
        true_image = tkinter.PhotoImage(file = "100 days of code/trivia/images/true.png")
        self.true_button = tkinter.Button(image = true_image, highlightthickness = 0, command = self.true_pressed)
        self.true_button.grid(row = 2, column = 0)

        false_image = tkinter.PhotoImage(file = "100 days of code/trivia/images/false.png")
        self.false_button = tkinter.Button(image = false_image, highlightthickness= 0, command = self.false_pressed)
        self.false_button.grid(row = 2, column = 1)


        self.get_next_question()

        self.window.mainloop()
    
    def get_next_question(self):
        self.canvas.config(bg="white")
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text = q_text)
    
    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
    
    def give_feedback(self, is_right):
        if is_right == True:
            self.update_score()
            self.canvas.config(bg="green")

        elif is_right == False:
            self.canvas.config(bg="red")
        
        if self.quiz.still_has_questions() == True:
            self.window.after(1000, self.get_next_question)
        
    def update_score(self):
        self.score.config(text = f"Score: {self.quiz.score}")