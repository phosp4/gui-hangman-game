import random

#creating "insert" for replacing "-" with characters
def nahradit (source_str, insert_str, pos):
    return source_str[:pos]+insert_str+source_str[pos+1:]

#allWordsO = open("D:/Sam/inf/dalsie/the-hangman/random-words.txt","r")
#allWords = allWordsO.read()
#allWords = allWords.split("\n")

#word = random.choice(allWords)
word = "hello"
letterNo = len(word)
solved = letterNo*"-"
allGuess = []
trials = 10

print("")
print("THE HANGMAN!")
print("")

while trials != 0:
    print("guess",str(11-trials)+"/10 |","word:",solved, "|", " ".join(allGuess))
    guess = (str(input("Try to guess one letter: "))[0]).lower()
    if guess not in allGuess:
        trials -= 1
        allGuess.append(guess)
    
        if guess in word:
            print("YES! Letter",guess,"is in the word!")
            print("")
            for j in range(letterNo):
                if word[j] == guess:
                    solved = nahradit(solved, guess, j)

        elif guess not in word:
            print("NOPE. Letter",guess.upper(),"is not in the word.")
            print("")

        if solved == word:
            print("WELL DONE! YOU WON !!!")
            print("The word was",solved.upper(),";D")
            break
    elif guess in allGuess:
        print("    Letter",guess,"was already used!")

if solved != word:
        print("OH DEAR! YOU DIED :/")
        print("The word was",word.upper())

#allWordsO.close()