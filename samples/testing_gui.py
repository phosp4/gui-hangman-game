from tkinter import *

def tryLetter():
    pass

master = Tk()
master.title("THE HANGMAN!")

plocha = Canvas(master, width=500, height=500, background="white")
title = Label(master, text="---", font="Courier 50", fg=None, bg="lightblue")
clueL = Label(master, text="clue", font="Courier 20", width=5,fg=None, bg="pink")
descL = Label(master, text="some description here", font="Courier 10", height=14, fg=None, bg="lightgreen")
clueB = Button(master, text="?", font="Courier 20 bold", fg=None, width=3, command=tryLetter, state="normal")

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
letterFont = "Courier 20 bold"
letterFg = "black"
letterWidth = 3

aL = Button(master, text="A", font=letterFont, fg=letterFg, width=letterWidth, command=tryLetter, state="normal")
bL = Button(master, text="B", font=letterFont, fg=letterFg, width=letterWidth, command=tryLetter, state="normal")
cL = Button(master, text="C", font=letterFont, fg=letterFg, width=letterWidth, command=tryLetter, state="normal")
dL = Button(master, text="D", font=letterFont, fg=letterFg, width=letterWidth, command=tryLetter, state="normal")
eL = Button(master, text="E", font=letterFont, fg=letterFg, width=letterWidth, command=tryLetter, state="normal")
fL = Button(master, text="F", font=letterFont, fg=letterFg, width=letterWidth, command=tryLetter, state="normal")
gL = Button(master, text="G", font=letterFont, fg=letterFg, width=letterWidth, command=tryLetter, state="normal")
hL = Button(master, text="H", font=letterFont, fg=letterFg, width=letterWidth, command=tryLetter, state="normal")
iL = Button(master, text="I", font=letterFont, fg=letterFg, width=letterWidth, command=tryLetter, state="normal")
jL = Button(master, text="J", font=letterFont, fg=letterFg, width=letterWidth, command=tryLetter, state="normal")
kL = Button(master, text="K", font=letterFont, fg=letterFg, width=letterWidth, command=tryLetter, state="normal")
lL = Button(master, text="L", font=letterFont, fg=letterFg, width=letterWidth, command=tryLetter, state="normal")
mL = Button(master, text="M", font=letterFont, fg=letterFg, width=letterWidth, command=tryLetter, state="normal")
nL = Button(master, text="N", font=letterFont, fg=letterFg, width=letterWidth, command=tryLetter, state="normal")
oL = Button(master, text="O", font=letterFont, fg=letterFg, width=letterWidth, command=tryLetter, state="normal")
pL = Button(master, text="P", font=letterFont, fg=letterFg, width=letterWidth, command=tryLetter, state="normal")
qL = Button(master, text="Q", font=letterFont, fg=letterFg, width=letterWidth, command=tryLetter, state="normal")
rL = Button(master, text="R", font=letterFont, fg=letterFg, width=letterWidth, command=tryLetter, state="normal")
sL = Button(master, text="S", font=letterFont, fg=letterFg, width=letterWidth, command=tryLetter, state="normal")
tL = Button(master, text="T", font=letterFont, fg=letterFg, width=letterWidth, command=tryLetter, state="normal")
uL = Button(master, text="U", font=letterFont, fg=letterFg, width=letterWidth, command=tryLetter, state="normal")
vL = Button(master, text="V", font=letterFont, fg=letterFg, width=letterWidth, command=tryLetter, state="normal")
wL = Button(master, text="W", font=letterFont, fg=letterFg, width=letterWidth, command=tryLetter, state="normal")
xL = Button(master, text="X", font=letterFont, fg=letterFg, width=letterWidth, command=tryLetter, state="normal")
yL = Button(master, text="Y", font=letterFont, fg=letterFg, width=letterWidth, command=tryLetter, state="normal")
zL = Button(master, text="Z", font=letterFont, fg=letterFg, width=letterWidth, command=tryLetter, state="normal")

title.grid(row=0,column=0, columnspan=9, sticky="news")
clueL.grid(row=1,column=0, columnspan=9, sticky="news")
descL.grid(row=2,column=0, columnspan=9, sticky="news")

aL.grid(row=3, column=0)
bL.grid(row=3, column=1)
cL.grid(row=3, column=2)
dL.grid(row=3, column=3)
eL.grid(row=3, column=4)
fL.grid(row=3, column=5)
gL.grid(row=3, column=6)
hL.grid(row=3, column=7)
iL.grid(row=3, column=8)

jL.grid(row=4, column=0)
kL.grid(row=4, column=1)
lL.grid(row=4, column=2)
mL.grid(row=4, column=3)
nL.grid(row=4, column=4)
oL.grid(row=4, column=5)
pL.grid(row=4, column=6)
qL.grid(row=4, column=7)
rL.grid(row=4, column=8)

sL.grid(row=5, column=0)
tL.grid(row=5, column=1)
uL.grid(row=5, column=2)
vL.grid(row=5, column=3)
wL.grid(row=5, column=4)
xL.grid(row=5, column=5)
yL.grid(row=5, column=6)
zL.grid(row=5, column=7)
clueB.grid(row=5,column=8)

plocha.grid(row=0,column=9, rowspan=6)

master.mainloop()