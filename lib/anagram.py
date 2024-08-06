# your code goes here!

class Anagram:

  def __init__(self, word):
    self.word = word

  def match(self, words):
    original_sorted = sorted(self.word)
    return [word for word in words if sorted(word) == original_sorted]