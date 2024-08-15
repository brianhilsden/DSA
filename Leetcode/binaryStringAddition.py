"""Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"""

def addBinary(a, b):
    if len(a) < len(b):
      a,b = b, a

    carry = 0
    result = []

    i,j = len(a)-1,len(b)-1

    while i>=0:
       total = carry + int(a[i]) + (int(b[j]) if j>0 else 0)
       carry = total //2
       result.append(str(total%2))
       i-=1
       j-=1

    if carry:
       result.append('1')

    return "".join(result[::-1])




print(addBinary("1010", "111"))