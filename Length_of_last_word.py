#Given a string consisting of words and spaces, return the length of the last word in the string
import re

class Solution:
    def __init__(self, sentence):
        self.sentence=sentence
        last_word = re.compile(r'\s(\w+)$')
        matches = last_word.findall(sentence)
        for match in matches:
            print(match)  #returns the range that contains the last word
            print(len(match)) #returns the length of the last word

Solution("To be or not to be, that is the question")       

Solution("Unbreak My Heart is a classic song")
        
Solution("I can't think of any more sentences")
    
