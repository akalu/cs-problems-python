"""   Given a 2D grid consists of 0s (land) and 1s (water). An island is a maximal
   4-directionally connected group of 0s and a closed island is an island
   totally (all left, top, right, bottom) surrounded by 1s.
   
   Return the number of closed islands.
   
   Input: grid =
   [
   [1,1,1,1,1,1,1,0],
   [1,0,0,0,0,1,1,0],
   [1,0,1,0,1,1,1,0],
   [1,0,0,0,0,1,0,1],
   [1,1,1,1,1,1,1,0]
   ]
   Output: 2 
   
   Explanation: Islands in gray are closed because they are completely
   surrounded by water (group of 1s).
   
   IDEA:
   1) detect and remove boundary land using dfs
   2) detect and count lands using dfs
"""

class Solution1254:
    pass
