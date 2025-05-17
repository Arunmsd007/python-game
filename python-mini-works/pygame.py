#used modules
import tkinter as tk
import random
import winsound  #for sound effects

# list of colours
colours = ['Red', 'Blue', 'Green', 'Pink', 'Black',
           'Yellow', 'Orange', 'White', 'Purple', 'Brown']

score = 0
high_score = 0
timeleft = 30

# function that will start the game.
def startGame(event=None):
    global timeleft, score
    if timeleft == 30:
        score = 0
        countdown()
    nextColour()

# Function to choose and display the next colour.
def nextColour():
    global score, timeleft

    if timeleft > 0:
        e.focus_set()

        if e.get().lower() == colours[1].lower():
            score += 1
            winsound.Beep(1000, 100)  #beep sound for correct answer

        e.delete(0, tk.END)
        random.shuffle(colours)
        label.config(fg=str(colours[1]), text=str(colours[0]))
        scoreLabel.config(text="Score: " + str(score))

# Countdown timer function 
def countdown():
    global timeleft, high_score

    if timeleft > 0:
        timeleft -= 1
        timeLabel.config(text="Time left: " + str(timeleft))
        timeLabel.after(1000, countdown)
    else:
        label.config(text="Game Over!", fg="black")
        e.delete(0, tk.END)
        if score > high_score:
            high_score = score
        highScoreLabel.config(text="High Score: " + str(high_score))
        winsound.Beep(500, 300)  # game over sound
        restart_button.config(state=tk.NORMAL)

# Restart the game
def restartGame():
    global timeleft, score
    timeleft = 30
    score = 0
    scoreLabel.config(text="Score: 0")
    timeLabel.config(text="Time left: 30")
    restart_button.config(state=tk.DISABLED)
    startGame()

# user interface setup
root = tk.Tk()
root.title("COLORGAME")
root.geometry("400x300")

instructions = tk.Label(root, text="Type the font color, not the word!", font=('Helvetica', 12))
instructions.pack()

scoreLabel = tk.Label(root, text="Press enter to start", font=('Helvetica', 12))
scoreLabel.pack()

highScoreLabel = tk.Label(root, text="High Score: 0", font=('Helvetica', 12))
highScoreLabel.pack()

timeLabel = tk.Label(root, text="Time left: 30", font=('Helvetica', 12))
timeLabel.pack()

label = tk.Label(root, font=('Helvetica', 60))
label.pack()

e = tk.Entry(root)
e.pack()

root.bind('<Return>', startGame)
e.focus_set()

restart_button = tk.Button(root, text="Restart", font=('Helvetica', 12), state=tk.DISABLED, command=restartGame)
restart_button.pack(pady=10)

root.mainloop()
