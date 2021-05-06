"""   Given a string s of '(' , ')' and lowercase English characters.
   
   Your task is to remove the minimum number of parentheses ( '(' or ')', in any
   positions ) so that the resulting parentheses string is valid and return any
   valid string.
   
   Formally, a parentheses string is valid if and only if:
   
   It is the empty string, contains only lowercase characters, or It can be
   written as AB (A concatenated with B), where A and B are valid strings, or It
   can be written as (A), where A is a valid string.
   
   
   Example 1:
   
   Input: s = "lee(t(c)o)de)" Output: "lee(t(c)o)de" 
   
   Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
   
   IDEA:
   1) eliminate all deficits of ( brackets counting the balance from left to right - 
      each time the balance dips lower than 0, omit symbol
   2) eliminate all deficits of ) brackets counting the balance from right to left - 
      each time the balance dips lower than 0, omit symbol
   
   O(2n)
   
"""

class Solution1249:
    pass
