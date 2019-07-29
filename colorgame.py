#import modules
import tkinter
import random

#list of possible colours
colours=['Red','Blue','Green','Pink','Black','Yellow','Orange','White','Purple','Brown']
score=0
#the time game left ,intially 30 seconds.
timeLeft=30

#function that will start game.
def startGame(event):
    if timeLeft==30:
        #start the time counter:
        countdown()
    #run the function to choose next colour.
    nextColour()

#function to choose and display the next colour.
def nextColour():
    #use the globally declared score and play variable.
    global score
    global timeleft
    #if a game is currently in play:
    if timeLeft>0:
        #make the text entry box active
        e.focus_set()
        #if the color typed is equal to the color of text
        if e.get().lower()==colours[1].lower():
            score+=1
        #clear the text entry box.
        e.delete(0,tkinter.END)
        random.shuffle(colours)
        #change the colour to type and by changing the text and the colour to a random colour value
        label.config(fg= str(colours[1]),text=str(colours[0]))
        #update the score
        scoreLabel.config(text="Score" +str(score))

#countdown timer function
def countdown():
    global timeLeft
    #if game is in play
    if timeLeft>0:
        #decreement the timer
        timeLeft-=1
        #update the timeleft label
        timeLabel.config(text="Time Left:"+str(timeLeft))
        #run the function again after 1 second
        timeLabel.after(1000,countdown)

#driver code
#create a gui window
root=tkinter.Tk()
#set the title
root.title("COLORGAME")
#set the size
root.geometry("375x200")
#add an instructions label
instructions=tkinter.Label(root,text="Type the colour of the text displayed!!",font=('Helvetica',12))
instructions.pack()
#add score label
scoreLabel=tkinter.Label(root,text="Press enter to start",font=('Helvetica',12))
scoreLabel.pack()
#add a time left label
timeLabel=tkinter.Label(root,text="Time left: "+str(timeLeft),font=('Helvetica',12))
timeLabel.pack()
#add a label for displaying colours
label=tkinter.Label(root,font=('Helvetica',60))
label.pack()
#add a text entry box
#typing the colours
e=tkinter.Entry(root)
#run the 'startGame' function when enter is pressed
root.bind('<Return>',startGame)
e.pack()

#set focus on the entry box
e.focus_set()
#start the GUI
root.mainloop()








            
    
