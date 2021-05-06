"""   Given two strings s and t, determine if they are isomorphic. Two strings are
   isomorphic if the characters in s can be replaced by t. All occurrences
   of a character must be replaced with another character while preserving the
   order of characters. No two characters may map to the same character but a
   character may map to itself. 
   
   Example 1: Input: s = "egg", t = "add" Output: true
   
   IDEA:
    use 2 maps for source and dest
    1) use mapping: src => dest to dynamically build map
    2) use mapped map for destination letters to cover scenario a => c, b => c
"""

class Solution205:
    pass
