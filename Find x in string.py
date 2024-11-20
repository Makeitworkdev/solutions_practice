#given two strings needle and haystack, return the index of the first occurrence of needle in haystack or -1 if needle is not part of haystack

class findNeedle:
    def __init__(self, haystack, needle):
        self.haystack=haystack
        self.needle=needle
        print(haystack.find(needle))

findNeedle("sadbutsad", "sad")

findNeedle("leetcode", "leeto")

findNeedle("Absolutely disturbing and disturbingly absolute", "disturb")
    
