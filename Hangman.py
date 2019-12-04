from Word import word

"""
  This class is the main class that controlls the game and most of the methods that 
  are called come from this class
"""
class hangman(word):
  def __init__(self, wordString, attempts):
    word.__init__(self, wordString)
    self.guess = "" #This variable holds the guess the user made
    self.attempts = attempts #holds the amount of attempts by the user
    self.EncryptedWord = "" #letters and dashes the player sees

    #This loop helps with the encoded list of words that the user sees
    for i in wordString:
      self.EncryptedWord += ("_" + " ")

  """
    calls the check method and uses the array given to help 
    find the words found by the player

    return void
  """
  def decend(self):
    data = self.check(self.guess)
    for i in data:
      #print(i)
      s = list(self.EncryptedWord)
      s[i] = self.guess
      self.EncryptedWord = "".join(s)

  """
    This is the statement give everytime the player gives a response

    return void
  """
  def whileStatement(self):
    print(self.EncryptedWord)
    print("You have {} attempts left".format(self.attempts))
  
  """
    This function is the backbone of the program and runs the while loop 
    so the program doesn't stop running until the users win or max out their attempts

    return void
  """
  def start(self):
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
