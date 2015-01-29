import tkinter
from tkinter import *
from random import randint
import tkinter.font



class Hangman(object):#This class represents a hangman game
  blanks = [] #Initialize accumalators
  count = 0
  guessL = []
  blanksL = []
  check = False
  def __init__(self): #gets secret word from txt file, puts secret word as blanks
    file = open("wordlist.txt","r")
    line = randint(1,56)
    count = 0
    word = ""
    for lines in file:
      count += 1
      if count == line:
        word = lines
    word.lower()
    secretWord = word
    self.__secretWord = secretWord
    
    self.__blanks = "___ " *(len(secretWord) - 1)
    Hangman.guessL = self.__blanks.split(" ")
    self.__incorrectLetters = []
    self.__correctLetters = []
    count = 0
    for letter in secretWord:
      if count < len(secretWord) - 1:
        Hangman.blanks.append(letter)
        Hangman.blanksL.append(letter)
      count += 1
    if Hangman.guessL[-1] == "":
      Hangman.guessL.pop(-1)
        
  def guess(self,letter): #determines if guessed letter is in secret word
    if letter.lower() in Hangman.blanks:
      Hangman.check = True
      for letters in Hangman.blanks:
        if letters == letter.lower():
          count = 0
          for items in Hangman.blanksL:
            if letter == items or letter.lower() == items:
              Hangman.guessL[count] = letter
            count += 1
          Hangman.blanks.pop(Hangman.blanks.index(letter.lower()))
      if len(Hangman.blanks) == 0: #if the blanks are all filled, then the user wins
        messagebox.showinfo("YOU WIN!", "You guessed all the correct letters!")
      
    else:
      Hangman.count += 1
      if Hangman.count < 9:
        messagebox.showerror("Incorrect!","This letter \'" + letter + "\' is not in the word!\nYou now have " + str(Hangman.count) + " incorrect choice(s)!\nYou have "+str(9 - Hangman.count) + " guesses remaining!")
      else:#if user runs out of guesses, then they lose
        messagebox.showerror("You LOSE!","You took too many guesses the word was " + str(self.__secretWord))

class HangmanGUI(Frame):
 
  
  def __init__(self):
    self.__hangman = Hangman()
    self.__mainWindow = tkinter.Tk()
    self.__topFrame = tkinter.Frame(self.__mainWindow)

    Frame.__init__(self,bg="skyblue")
    self.master.title("Hangman by Danny Wong & Samier Trabilsy")
    self.grid()

    #hangman pics
    self.__A = PhotoImage(file = "1.gif")
    self.__B = PhotoImage(file = "2.gif")
    self.__C = PhotoImage(file = "3.gif")
    self.__D = PhotoImage(file = "4.gif")
    self.__E = PhotoImage(file = "5.gif")
    self.__F = PhotoImage(file = "6.gif")
    self.__G = PhotoImage(file = "7.gif")
    self.__H = PhotoImage(file = "8.gif")
    self.__I = PhotoImage(file = "9.gif")
    self.__Start = PhotoImage(file = "0.gif")
    self.__picture = [self.__Start,self.__A,self.__B,self.__C,self.__D,self.__E,self.__F,self.__G,self.__H,self.__I]
    #puts appropriate picture based on total incorrect guesses
    self.__hPic = Label(self, image = self.__picture[Hangman.count])
    self.__hPic.grid()

    

    #buttons
    self.__a = Button(self, text = "A", command = lambda: self.callback("A"))
    self.__b = Button(self, text = "B", command = lambda: self.callback("B"))
    self.__c = Button(self, text = "C", command = lambda: self.callback("C"))
    self.__d = Button(self, text = "D", command = lambda: self.callback("D"))
    self.__e = Button(self, text = "E", command = lambda: self.callback("E"))
    self.__f = Button(self, text = "F", command = lambda: self.callback("F"))
    self.__g = Button(self, text = "G", command = lambda: self.callback("G"))
    self.__h = Button(self, text = "H", command = lambda: self.callback("H"))
    self.__i = Button(self, text = "I", command = lambda: self.callback("I"))
    self.__j = Button(self, text = "J", command = lambda: self.callback("J"))
    self.__k = Button(self, text = "K", command = lambda: self.callback("K"))
    self.__l = Button(self, text = "L", command = lambda: self.callback("L"))
    self.__m = Button(self, text = "M", command = lambda: self.callback("M"))
    self.__n = Button(self, text = "N", command = lambda: self.callback("N"))
    self.__o = Button(self, text = "O", command = lambda: self.callback("O"))
    self.__p = Button(self, text = "P", command = lambda: self.callback("P"))
    self.__q = Button(self, text = "Q", command = lambda: self.callback("Q"))
    self.__r = Button(self, text = "R", command = lambda: self.callback("R"))
    self.__s = Button(self, text = "S", command = lambda: self.callback("S"))
    self.__t = Button(self, text = "T", command = lambda: self.callback("T"))
    self.__u = Button(self, text = "U", command = lambda: self.callback("U"))
    self.__v = Button(self, text = "V", command = lambda: self.callback("V"))
    self.__w = Button(self, text = "W", command = lambda: self.callback("W"))
    self.__x = Button(self, text = "X", command = lambda: self.callback("X"))
    self.__y = Button(self, text = "Y", command = lambda: self.callback("Y"))
    self.__z = Button(self, text = "Z", command = lambda: self.callback("Z"))

    self.__a.grid(row = 5, column = 2)
    self.__b.grid(row = 5, column = 3)
    self.__c.grid(row = 5, column = 4)
    self.__d.grid(row = 5, column = 5)
    self.__e.grid(row = 5, column = 6)
    self.__f.grid(row = 5, column = 7)
    self.__g.grid(row = 5, column = 8)
    self.__h.grid(row = 5, column = 9)
    self.__i.grid(row = 5, column = 10)
    self.__j.grid(row = 5, column = 11)
    self.__k.grid(row = 5, column = 12)
    self.__l.grid(row = 5, column = 13)
    self.__m.grid(row = 5, column = 14)
    self.__n.grid(row = 6, column = 2)
    self.__o.grid(row = 6, column = 3)
    self.__p.grid(row = 6, column = 4)
    self.__q.grid(row = 6, column = 5)
    self.__r.grid(row = 6, column = 6)
    self.__s.grid(row = 6, column = 7)
    self.__t.grid(row = 6, column = 8)
    self.__u.grid(row = 6, column = 9)
    self.__v.grid(row = 6, column = 10)
    self.__w.grid(row = 6, column = 11)
    self.__x.grid(row = 6, column = 12)
    self.__y.grid(row = 6, column = 13)
    self.__z.grid(row = 6, column = 14)

    #changes font of letters in blanks
    font = tkinter.font.Font(family="Helvetica", size=20,)
    
    self.__lText = ""
    for item in Hangman.guessL:
      self.__lText += str(item) + " "
    self.__guess = Label(self, text = self.__lText, font = font)
    self.__guess.grid(row = 7)
    
  def gameDone(self):
    self.__a["state"] = DISABLED
    self.__b["state"] = DISABLED
    self.__c["state"] = DISABLED
    self.__d["state"] = DISABLED
    self.__e["state"] = DISABLED
    self.__f["state"] = DISABLED
    self.__g["state"] = DISABLED
    self.__h["state"] = DISABLED
    self.__i["state"] = DISABLED
    self.__j["state"] = DISABLED
    self.__k["state"] = DISABLED
    self.__l["state"] = DISABLED
    self.__m["state"] = DISABLED
    self.__n["state"] = DISABLED
    self.__o["state"] = DISABLED
    self.__p["state"] = DISABLED
    self.__q["state"] = DISABLED
    self.__r["state"] = DISABLED
    self.__s["state"] = DISABLED
    self.__t["state"] = DISABLED
    self.__u["state"] = DISABLED
    self.__v["state"] = DISABLED
    self.__w["state"] = DISABLED
    self.__x["state"] = DISABLED
    self.__y["state"] = DISABLED
    self.__z["state"] = DISABLED
    

  def callback(self, letter): #the two functions that are invoked when you click on a letter button
    self.guessLetter(letter) 
    self.disableLetter(letter)
    self.__lText = ""
    for item in Hangman.guessL:
      self.__lText += str(item) + " "
    self.__guess["text"] = self.__lText
    if len(Hangman.blanks) == 0:
      messagebox.showinfo("YAY","YOU WIN")
    
    
  def disableLetter(self, letter): #disables the letter after clicking it
    if letter == "A":
      self.__a["state"] = DISABLED
    if letter == "B":
      self.__b["state"] = DISABLED
    if letter == "C":
      self.__c["state"] = DISABLED
    if letter == "D":
      self.__d["state"] = DISABLED
    if letter == "E":
      self.__e["state"] = DISABLED
    if letter == "F":
      self.__f["state"] = DISABLED
    if letter == "G":
      self.__g["state"] = DISABLED
    if letter == "H":
      self.__h["state"] = DISABLED
    if letter == "I":
      self.__i["state"] = DISABLED
    if letter == "J":
      self.__j["state"] = DISABLED
    if letter == "K":
      self.__k["state"] = DISABLED
    if letter == "L":
      self.__l["state"] = DISABLED
    if letter == "M":
      self.__m["state"] = DISABLED
    if letter == "N":
      self.__n["state"] = DISABLED
    if letter == "O":
      self.__o["state"] = DISABLED
    if letter == "P":
      self.__p["state"] = DISABLED
    if letter == "Q":
      self.__q["state"] = DISABLED
    if letter == "R":
      self.__r["state"] = DISABLED
    if letter == "S":
      self.__s["state"] = DISABLED
    if letter == "T":
      self.__t["state"] = DISABLED
    if letter == "U":
      self.__u["state"] = DISABLED
    if letter == "V":
      self.__v["state"] = DISABLED
    if letter == "W":
      self.__w["state"] = DISABLED
    if letter == "X":
      self.__x["state"] = DISABLED
    if letter == "Y":
      self.__y["state"] = DISABLED
    if letter == "Z":
      self.__z["state"] = DISABLED
      
  def guessLetter(self, letter): #checks to see if the guess was correct or not 
    Hangman.check = False
    self.__hangman.guess(letter)
    self.__hPic["image"] = self.__picture[Hangman.count]
    if len(Hangman.blanks) == 0 or Hangman.count > 8:
      self.gameDone()

#invoke main
def main():
  HangmanGUI().mainloop()
main()
