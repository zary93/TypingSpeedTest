from tkinter import *
import random


def the_time():
    global game_time
    timer.config(text=str(game_time))
    timer.place(x=20, y=20)
    if game_time > 0:
        game_time -= 1
        timer.config(text=str(game_time))
        timer.after(1000, the_time)
    elif game_time == 0:
        result()


def clean():
    title.config(font=("Helvetica", 48))
    instruction.pack_forget()
    title.place(x=150, y=150)
    start_game.pack_forget()
    update_countdown(3)


def game(event=None):
    global SCORE, WORD, MISTAKE
    word_to_check.place(x=250, y=150)
    user_word.place(x=250, y=250)
    word_get = user_word.get().replace(" ", "")
    if word_get != "":
        if WORD == word_get:
            SCORE += 1
        elif WORD != word_get:
            MISTAKE += 1
    user_word.delete(0, END)
    WORD = random.choice(list_text)
    word_to_check.config(text=WORD)
    window.bind("<space>", game)


def result():
    global SCORE, MISTAKE
    window.unbind('<space>')
    word_to_check.place_forget()
    user_word.place_forget()
    timer.place_forget()
    result_label.place(x=100, y=150)
    retry_button.place(x=350, y=250)
    if SCORE <= 15:
        result_label.config(text=f"You typed {SCORE} words correctly and {MISTAKE} incorrectly!\n "
                                 f"You can do better than that", fg="#fc3d03")
    elif 15 < SCORE <= 35:
        result_label.config(text=f"You typed {SCORE} words correctly and {MISTAKE} incorrectly!\n "
                                 f"This looks very good!", fg="#0390fc")
    elif SCORE > 35:
        result_label.config(text=f"You typed {SCORE} words correctly and {MISTAKE} incorrectly!\n "
                                 f"You are a fantastic typewriter!", fg="#0abf22")


def retry():
    global SCORE, MISTAKE, game_time
    SCORE = 0
    MISTAKE = 0
    game_time = 60
    result_label.place_forget()
    retry_button.place_forget()
    update_countdown(3)


def update_countdown(count):
    title.config(text=str(count))
    title.place(x=250, y=150)
    if count > 0:
        window.after(1000, update_countdown, count-1)
    else:
        title.config(text="")
        game()
        the_time()


window = Tk()
window.title("Typing Speed Test")
window.minsize(width=500, height=500)

words = ("sniff mass novel stop bond fraction ideal egg fade conscience  solution smash proof private feel "
         "responsibility replacement crossing crash basic appetite flavor despise bake arrogant channel cheap "
         "vision jungle rare amputate conference chew manager trust slime explain avenue moving jury")

list_text = list(words.split(" "))
game_time = 60
SCORE = 0
MISTAKE = 0
WORD = random.choice(list_text)

title = Label()
title.config(text="Typing Speed Test",
             font=('Comic Sans MS', 24, 'bold'),
             fg="purple",
             padx=100,
             pady=50)
title.pack()

instruction = Label()
instruction.config(text="How fast are your fingers? Do the one-minute typing test to find out! \n Press the space bar "
                        "after each word. At the end, you'll get your typing speed.\n Good Luck!",
                   font=('Comic Sans MS', 15),
                   padx=10,
                   pady=25)
instruction.pack()

start_game = Button(text="Start Game", command=clean)
start_game.pack()

timer = Label(font=("Arial", 18))

word_to_check = Label(window, text=WORD, font="comicsanms 20 bold", fg="#FFD60A",
                      bg="#001D3D", width=15, anchor="center")

user_word = Entry(window, font="comicsanms 18 bold", fg="grey", justify="center", bd=4)
user_word.focus()

result_label = Label(window, font="comicsanms 20 bold", anchor="center")

retry_button = Button(text="Try Again", command=retry)

window.mainloop()
