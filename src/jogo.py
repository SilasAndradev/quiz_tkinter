from tkinter import *
from tkinter import ttk, messagebox
import json
from PIL import ImageTk, Image, ImageDraw
from random import choice

class jogo:
    def __init__(self):
        self.master = Tk()
        self.master.title("Quiz")
        self.master.geometry('400x500')
        self.master.iconbitmap("assets/icon.ico")

        self.color_background = "#F0F0EC"
        self.color_background_text = "#87ceeb"

        self.frame_principal = Frame(
        self.master, 
        bg=self.color_background, 
        width= 400, 
        height= 500
        )

        self.title_game = Label(
        self.frame_principal, 
        text="QUIZ", 
        font=('Helvetica', 40, 'bold'), 
        fg='green'
        )

        self.button_start = Button(self.frame_principal, text='Start', bg=self.color_background_text,
        font=('Helvetica', 20, 'bold'), foreground='green',command=lambda: self.StartGame()
        )

        self.button_quit = Button(self.frame_principal, text='Quit', bg=self.color_background_text,
        font=('Helvetica', 20, 'bold'), foreground='green',command=lambda: self.QuitGame()
        )

        self.button_credits = Button(self.frame_principal, text='Credits', bg=self.color_background_text,
        font=('Helvetica', 20, 'bold'), foreground='green',command=lambda: self.CreditsGame()
        )


        self.frame_questions = Frame(self.master, bg=self.color_background, width= 400, height= 500)
        self.label_question = Label(self.frame_questions)

        self.var_game = StringVar()

        self.radio_buttons_alternative = Radiobutton(self.frame_questions, variable=self.var_game) 

        self.answers = []


        self.next_question_button = Button(self.frame_questions, text='Next', font=('Helvetica', 20, 'bold'), fg='green', command= lambda: self.nextQuestion())

        self.holder_list = []

        
        


        self.Start_Screen()


    def StartGame(self):
        try:
            with open('assets/question.json', encoding='utf-8') as file:
                self.questions_archive = json.load(file)
        except Exception as e:
            messagebox.showerror("Something is wrong", e)




        self.frame_principal.place_forget()
        self.number_question_for_check = -1

        self.player_answers = []

        self.score = 0

        self.Game()

    def QuitGame(self):
        self.master.quit()

    def CreditsGame(self):
        messagebox.showinfo("Credits", "Made by Silas Andrade\ngithub.com/SilasAndradev")

    def Start_Screen(self):
        self.frame_principal.place(relx=0, rely=0)
        self.title_game.place(relx=0.5, rely = 0.15 ,anchor=CENTER)

        self.button_start.place(relx=0.5, rely=0.40, relheight=0.1, relwidth=0.4, anchor=CENTER)
        
        self.button_credits.place(relx=0.5, rely=0.60, relheight=0.1, relwidth=0.4, anchor=CENTER)


        self.button_quit.place(relx=0.5, rely=0.80, relheight=0.1, relwidth=0.4, anchor=CENTER)

    def run(self):
        self.master.mainloop()

    def SearchQuestion(self):
        for alternative in self.questions_archive["question" + str(self.number_question)]:
            self.question = alternative[0]
            self.answers = [
                alternative[1],
                alternative[2],
                alternative[3],
                alternative[4]
            ]

    def check(self):
        for self.question_numbers in self.questions_archive:
            for self.question_number in self.question_numbers:
                for quesitons_and_response in self.questions_archive["question" + str(self.number_question)]:
                    if quesitons_and_response[1] == self.player_answers[self.number_question_for_check] :
                        self.score += 1
                        break
                    break
                break
            break
        self.number_question += 1
                    
                    

    def printScore(self):
        messagebox.showinfo("Your score", f"Your score is {self.score}!")


    def nextQuestion(self):
        self.player_answers.append(self.var_game.get())

        self.number_question_for_check +=1
        self.check()

        for widget in self.holder_list:
            widget.place_forget()

        self.holder_list = []
        self.label_question.place_forget()
        self.position_alternative_lista = [0.3, 0.4, 0.5, 0.6]

        if self.number_question > 5:
            self.frame_questions.place_forget()
            self.printScore()
            self.Start_Screen()

        else:

            self.SearchQuestion()
            self.var_game.set(choice(self.answers))

            self.label_question.config(text=self.question,  font=('Helvetica', 14, 'bold'), 
            fg='green')
            self.label_question.place(relx=0.5, rely = 0.15 , anchor=CENTER)


            for text in self.answers:
                self.position_alternative = choice(self.position_alternative_lista)

                self.position_alternative_lista.remove(self.position_alternative)

                self.radio = Radiobutton(self.frame_questions, 
                variable=self.var_game,font=('Helvetica', 14, 'bold'), fg='green', text=text, value=text,
                )
                self.radio.place(anchor=CENTER, relx=0.5, rely=self.position_alternative)
                self.holder_list.append(self.radio)





    def Game(self):
        self.number_question = 1

        self.position_alternative_lista = [0.3, 0.4, 0.5, 0.6]

        self.SearchQuestion()

        self.var_game.set(choice(self.answers))

        
        for text in self.answers:
            self.position_alternative = choice(self.position_alternative_lista)
            self.position_alternative_lista.remove(self.position_alternative)

            self.radio = Radiobutton(self.frame_questions, 
            variable=self.var_game,font=('Helvetica', 14, 'bold'), fg='green', text=text, value=text,
            )
            self.radio.place(anchor=CENTER, relx=0.5, rely=self.position_alternative)
            self.holder_list.append(self.radio)
            

        self.frame_questions.place(relx=0, rely=0)


        self.label_question.config(text=self.question,  font=('Helvetica', 14, 'bold'), 
        fg='green')

        self.label_question.place(relx=0.5, rely = 0.15 , anchor=CENTER)
        
        self.next_question_button.place(relx=0.5, rely=0.9, anchor=CENTER)

