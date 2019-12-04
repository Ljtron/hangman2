"""
  This class is used to controll the word and the information with in it to help
  The game run more efficently
"""

class word:
  def __init__(self, wordString):
    self.wordString = wordString
    self.wordDict = {}
    self.index()

  """
    This is the first function ran and it helps setup the dictionary
    so each letter is attached to its index

    return void
  """
  def index(self):
    for i, y in enumerate(self.wordString):
      #print(i)
      #print(y)
      try:
        self.wordDict[y].append(i)
      
      except KeyError:
        self.wordDict[y] = [i]

  """
    This program checks the guess or letter in the dictionary and returns a list
    of indexs if the dictionary has the letter

    return Ex: [0,1,2]
  """
  def check(self, guess):
    for i, y in self.wordDict.items():
      if(guess == i):
        return y
      
      