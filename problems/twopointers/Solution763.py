"""   
   A string S of lowercase English letters is given. We want to partition this
   string into as many parts as possible so that each letter appears in at most
   one part, and return a list of integers representing the size of these parts.
   
   
   
   Example 1:
   
   Input: S = "ababcbacadefegdehijhklij" Output: [9,7,8] Explanation: The
   partition is "ababcbaca", "defegde", "hijhklij". This is a partition so that
   each letter appears in at most one part.
   
   A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it
   splits S into less parts.
   
   IDEA:
   during traversing take care of upperBoundary for all letters seen so far
   if it coincides with i, then => from [lastCut,curIdx] we have seen all letters
   
   abca  dd
   
"""

class Solution763:
    pass
