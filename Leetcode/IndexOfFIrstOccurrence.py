def strStr(haystack, needle):
    needleLen = len(needle) 
    if len(needle) ==0:
        return -1

    for i in range(len(haystack)):
        if haystack[i]==needle[0]:
            if haystack[i:i+needleLen] == needle:
                return i
    return -1
            


print(strStr("leetcode",""))

