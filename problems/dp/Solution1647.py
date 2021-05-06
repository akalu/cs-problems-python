"""   A string s is called good if there are no two different characters in s that
   have the same frequency.
   
   Given a string s, return the minimum number of characters you need to delete
   to make s good.
   
   The frequency of a character in a string is the number of times it appears in
   the string. For example, in the string "aab", the frequency of 'a' is 2,
   while the frequency of 'b' is 1.
   
   
   
   Example 1:
   
   Input: s = "aab" Output: 0 Explanation: s is already good. Example 2:
   
   Input: s = "aaabbbcc" Output: 2 Explanation: You can delete two 'b's
   resulting in the good string "aaabcc". Another way it to delete one 'b' and
   one 'c' resulting in the good string "aaabbc".
   
   IDEA:
   because there are more than one way to solve problem, this is a hint to use DP 
   (in other words, investigate all possible variants using some caching techniques to decrease the 
    space of all possible variants)
    
   For example, let start from the string aaabbbcc
   
                aaabbbcc
               /      \
           aaabbcc     aaabbbc
          /             \
        aaabcc          aaabbc
        
    Reformulated problem:
     what is the min # of update operations to make this map containing only unique values    
        id1 => 3
        id2 => 3
        id3 => 2
        
        OO        O#
        OOO   --> OO# 
        OOO       OOO
        
     case with big deficit of values:
           
        OO        O#
        OO   -->  OO 
        OOO       OOO
        
"""

class Solution1647:
    pass
