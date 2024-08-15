def isValid(s):
    if len(s)<=1:
        return False
    parentheses = ["(",")","[","]","{","}"]
    for i in range(len(s)):
        if s[i] not in parentheses:
            return False
        elif s[i] in ["(","{","["] and i ==len(s)-1:
            return False
        elif (s[i] == "(" and s[i+1] !=  ")") or (s[i]==")" and s[i-1]!="("):
            return False
        elif s[i] == "[" and s[i+1] != "]" or (s[i]=="]" and s[i-1]!="["):
            return False
        elif s[i] == "{" and s[i+1] != "}" or (s[i]=="}" and s[i-1]!="{"):
            return False
    return True
        


print(isValid("{}{)"))