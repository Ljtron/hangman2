from Word import word

"""
  This class is the main class that controlls the game and most of the methods that 
  are called come from this class
"""
class hangman(word):
  def __init__(self, wordString, attempts):
    word.__init__(self, wordString)
    self.guess = ""
    self.attempts = attempts
    self.EncryptedWord = ""
    for i in wordString:
      self.EncryptedWord += ("_" + " ")

  def decend(self):
    data = self.check(self.guess)
    for i in data:
      #print(i)
      s = list(self.EncryptedWord)
      s[i] = self.guess
      self.EncryptedWord = "".join(s)

  def whileStatement(self):
    print(self.EncryptedWord)
    print("You have {} attempts left".format(self.attempts))
  
  def game(self):
    #print(self.check(self.guess))
    print("Welcome to hangman")
    print("You will be given a word to guess and you only have {} attempts".format(self.attempts))
    print("In order to continue press enter")
    input()

    print("The word that you are guessing has {} letters".format(len(self.wordString)))
    print(self.EncryptedWord)

    while(0 <= self.attempts):
      print("please enter a letter")
      self.guess = input("")
      if(self.guess in self.wordString):
        self.decend()
        self.whileStatement()
      else:
        self.whileStatement()
        self.attempts -= 1
    #print(self.EncryptedWord)
