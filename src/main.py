from tkinter import *
import random

#-----LOADING FILES-----
termsO = open("../res/terms.txt","r")
descrO = open("../res/definitions.txt","r")
cluesO = open("../res/clues.txt","r")

termsR = termsO.readlines()
descrR = descrO.readlines()
cluesR = cluesO.readlines()

termsL = []
descrL = []
cluesL = []

for i in range(len(termsR)):
    termsL.append((termsR[i])[0:-1])
    descrL.append((descrR[i])[0:-1])
    cluesL.append((cluesR[i])[0:-1])

#-----VARIABLES-----
allWords = termsL

x = 30
y = 330
defColor = "black"
defWidth = 5
trialsDefault = 11

global word, solved, allGuess, trials, desc, letterNo
word = random.choice(allWords)
desc = descrL[termsL.index(word)]
letterNo = len(word)
solved = letterNo*"-"
allGuess = []
trials = trialsDefault

#-----FUNCTIONS-----
def tryLetter(guess):
    global trials, solved
    if trials > 0:
        if guess in word:
            for j in range(letterNo):
                if word[j] == guess:
                    solved = replace_letter(solved, guess, j)
            title.configure(text=solved)
        elif guess not in word:
            trials -= 1
            trialsCount.configure(text=trials)
            draw_next()

        if solved == word:
            victory()
        if trials == 0:
            gameover()

def draw_next():
    global zem, tyc1, tyc2, tyc3, lano, hlava, telo, noha1, noha2, ruka1, ruka2
    if trials == 10:
        zem = plocha.create_arc(x,y,x+150,y+150, style="arc", extent=180, width=defWidth, outline=defColor)
    if trials == 9:
        tyc1 = plocha.create_line(x+75,y,x+75,y-300, width=defWidth, fill=defColor)
    if trials == 8:
        tyc2 = plocha.create_line(x+75,y-300,x+300,y-300, width=defWidth, fill=defColor)
    if trials == 7:
        tyc3 = plocha.create_line(x+75,y-220,x+145,y-300, width=defWidth, fill=defColor)
    if trials == 6:
        lano = plocha.create_line(x+300,y-300,x+300,y-240, width=defWidth, fill=defColor)
    if trials == 5:
        hlava = plocha.create_oval(x+270,y-180,x+330,y-240, width=defWidth, outline=defColor)
    if trials == 4:
        telo = plocha.create_line(x+300,y-180,x+300,y-110, width=defWidth, fill=defColor)
    if trials == 3:
        noha1 = plocha.create_line(x+300,y-110,x+270,y-50, width=defWidth, fill=defColor)
    if trials == 2:
        noha2 = plocha.create_line(x+300,y-110,x+330,y-50, width=defWidth, fill=defColor)
    if trials == 1:
        ruka1 = plocha.create_line(x+300,y-180,x+260,y-130, width=defWidth, fill=defColor)
        title.configure(fg="red")
        trialsCount.configure(fg="red")
    if trials == 0:
        ruka2 = plocha.create_line(x+300,y-180,x+340,y-130, width=defWidth, fill=defColor)
    plocha.update()

def replace_letter (source_str, insert_str, pos):
    return source_str[:pos]+insert_str+source_str[pos+1:]

def playagain():
    global word, solved, allGuess, trials, desc, letterNo
    plocha.delete(ALL)
    word = random.choice(allWords)
    desc = descrL[termsL.index(word)]
    letterNo = len(word)
    solved = letterNo*"-"
    allGuess = []
    trials = trialsDefault

    trialsCount.configure(text=trials)
    title.configure(text=solved, fg=defColor)
    trialsCount.configure(fg=defColor)
    descL.configure(text=desc)

    for i in alphabet2:
        i.configure(state="normal", cursor="hand2")

def gameover():
    for i in alphabet2:
        i.configure(state="disabled", cursor="arrow")
    title.configure(text=word)
    plocha.create_text(200,400, text="GAME OVER!", font="Courier 40 bold", fill="red")
def victory():
    title.configure(fg="green")
    plocha.create_text(200,400, text="WELL DONE!", font="Courier 40 bold", fill="limegreen")

#-----GUI-----
master = Tk()
master.title("THE HANGMAN!")
master.iconbitmap("../res/favicon.ico")

plocha = Canvas(master, width=400, height=430, background=None)
title = Label(master, text=solved, font="Courier 40", fg=None, bg="lightblue")
#clueL = Label(master, text="clue", font="Courier 20", width=5,fg=None, bg="pink")
descL = Label(master, text=desc, font="Courier 16", height=11, fg=None, bg="lightgreen", wraplength=500, justify=CENTER)
trialsCount = Label(master, text=trials, font="Courier 40", fg=None, bg=None)

letterFont = "Courier 20 bold"
letterFg = "white"
letterBg = "darkorange"
letterWidth = 3

aL = Button(master, text="A", font=letterFont, fg=letterFg, bg=letterBg, width=letterWidth, cursor="hand2", command= lambda: [aL.configure(state="disabled", cursor="arrow"),tryLetter("A")])
bL = Button(master, text="B", font=letterFont, fg=letterFg, bg=letterBg, width=letterWidth, cursor="hand2", command= lambda: [bL.configure(state="disabled", cursor="arrow"),tryLetter("B")])
cL = Button(master, text="C", font=letterFont, fg=letterFg, bg=letterBg, width=letterWidth, cursor="hand2", command= lambda: [cL.configure(state="disabled", cursor="arrow"),tryLetter("C")])
dL = Button(master, text="D", font=letterFont, fg=letterFg, bg=letterBg, width=letterWidth, cursor="hand2", command= lambda: [dL.configure(state="disabled", cursor="arrow"),tryLetter("D")])
eL = Button(master, text="E", font=letterFont, fg=letterFg, bg=letterBg, width=letterWidth, cursor="hand2", command= lambda: [eL.configure(state="disabled", cursor="arrow"),tryLetter("E")])
fL = Button(master, text="F", font=letterFont, fg=letterFg, bg=letterBg, width=letterWidth, cursor="hand2", command= lambda: [fL.configure(state="disabled", cursor="arrow"),tryLetter("F")])
gL = Button(master, text="G", font=letterFont, fg=letterFg, bg=letterBg, width=letterWidth, cursor="hand2", command= lambda: [gL.configure(state="disabled", cursor="arrow"),tryLetter("G")])
hL = Button(master, text="H", font=letterFont, fg=letterFg, bg=letterBg, width=letterWidth, cursor="hand2", command= lambda: [hL.configure(state="disabled", cursor="arrow"),tryLetter("H")])
iL = Button(master, text="I", font=letterFont, fg=letterFg, bg=letterBg, width=letterWidth, cursor="hand2", command= lambda: [iL.configure(state="disabled", cursor="arrow"),tryLetter("I")])
jL = Button(master, text="J", font=letterFont, fg=letterFg, bg=letterBg, width=letterWidth, cursor="hand2", command= lambda: [jL.configure(state="disabled", cursor="arrow"),tryLetter("J")])
kL = Button(master, text="K", font=letterFont, fg=letterFg, bg=letterBg, width=letterWidth, cursor="hand2", command= lambda: [kL.configure(state="disabled", cursor="arrow"),tryLetter("K")])
lL = Button(master, text="L", font=letterFont, fg=letterFg, bg=letterBg, width=letterWidth, cursor="hand2", command= lambda: [lL.configure(state="disabled", cursor="arrow"),tryLetter("L")])
mL = Button(master, text="M", font=letterFont, fg=letterFg, bg=letterBg, width=letterWidth, cursor="hand2", command= lambda: [mL.configure(state="disabled", cursor="arrow"),tryLetter("M")])
nL = Button(master, text="N", font=letterFont, fg=letterFg, bg=letterBg, width=letterWidth, cursor="hand2", command= lambda: [nL.configure(state="disabled", cursor="arrow"),tryLetter("N")])
oL = Button(master, text="O", font=letterFont, fg=letterFg, bg=letterBg, width=letterWidth, cursor="hand2", command= lambda: [oL.configure(state="disabled", cursor="arrow"),tryLetter("O")])
pL = Button(master, text="P", font=letterFont, fg=letterFg, bg=letterBg, width=letterWidth, cursor="hand2", command= lambda: [pL.configure(state="disabled", cursor="arrow"),tryLetter("P")])
qL = Button(master, text="Q", font=letterFont, fg=letterFg, bg=letterBg, width=letterWidth, cursor="hand2", command= lambda: [qL.configure(state="disabled", cursor="arrow"),tryLetter("Q")])
rL = Button(master, text="R", font=letterFont, fg=letterFg, bg=letterBg, width=letterWidth, cursor="hand2", command= lambda: [rL.configure(state="disabled", cursor="arrow"),tryLetter("R")])
sL = Button(master, text="S", font=letterFont, fg=letterFg, bg=letterBg, width=letterWidth, cursor="hand2", command= lambda: [sL.configure(state="disabled", cursor="arrow"),tryLetter("S")])
tL = Button(master, text="T", font=letterFont, fg=letterFg, bg=letterBg, width=letterWidth, cursor="hand2", command= lambda: [tL.configure(state="disabled", cursor="arrow"),tryLetter("T")])
uL = Button(master, text="U", font=letterFont, fg=letterFg, bg=letterBg, width=letterWidth, cursor="hand2", command= lambda: [uL.configure(state="disabled", cursor="arrow"),tryLetter("U")])
vL = Button(master, text="V", font=letterFont, fg=letterFg, bg=letterBg, width=letterWidth, cursor="hand2", command= lambda: [vL.configure(state="disabled", cursor="arrow"),tryLetter("V")])
wL = Button(master, text="W", font=letterFont, fg=letterFg, bg=letterBg, width=letterWidth, cursor="hand2", command= lambda: [wL.configure(state="disabled", cursor="arrow"),tryLetter("W")])
xL = Button(master, text="X", font=letterFont, fg=letterFg, bg=letterBg, width=letterWidth, cursor="hand2", command= lambda: [xL.configure(state="disabled", cursor="arrow"),tryLetter("X")])
yL = Button(master, text="Y", font=letterFont, fg=letterFg, bg=letterBg, width=letterWidth, cursor="hand2", command= lambda: [yL.configure(state="disabled", cursor="arrow"),tryLetter("Y")])
zL = Button(master, text="Z", font=letterFont, fg=letterFg, bg=letterBg, width=letterWidth, cursor="hand2", command= lambda: [zL.configure(state="disabled", cursor="arrow"),tryLetter("Z")])
clueB = Button(master, text="Play again", font="Courier 10 bold", fg="black", bg="orange", width=3, cursor="hand2", wraplength=50, justify=CENTER, command=playagain)

alphabet2 = [aL, bL, cL, dL, eL, fL, gL, hL, iL, jL, kL, lL, mL, nL, oL, pL, qL, rL, sL, tL, uL, vL, wL, xL, yL, zL]

trialsCount.grid(row=0,column=0, columnspan=2, sticky="news")
title.grid(row=0,column=2, columnspan=7, sticky="news")
#clueL.grid(row=1,column=0, columnspan=9, sticky="news")
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
clueB.grid(row=5,column=8, sticky="news")

plocha.grid(row=0,column=9, rowspan=6)

#allWordsO.close()

termsO.close()
descrO.close()
cluesO.close()

master.resizable(False, False)
master.mainloop()