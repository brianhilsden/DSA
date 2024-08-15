"""Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal 
substring
 consisting of non-space characters only."""


def lengthOfLastWord(s):
    if len(s.split())==1:
        return len(s.split()[-1])
    
    arr = s.split()
    print(arr[-1])
    return len(arr[-1])
    

    



print(lengthOfLastWord("     day"))