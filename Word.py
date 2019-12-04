"""
  This class is used to controll the word and the information with in it to help
  The game run more efficently
"""

class word:
  def __init__(self, wordString):
    self.wordString = wordString
    self.wordDict = {}
    self.index()

  def index(self):
    for i, y in enumerate(self.wordString):
      #print(i)
      #print(y)
      try:
        self.wordDict[y].append(i)
      
      except KeyError:
        self.wordDict[y] = [i]

  def check(self, guess):
    for i, y in self.wordDict.items():
      if(guess == i):
        return y
      
      