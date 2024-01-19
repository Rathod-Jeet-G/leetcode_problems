"""
----------------------------------companies---------------------------------------------
the below record of 2023 year and past
-> 0 - 6 months:

   Amazon 6
   Adobe 3
   Apple 2
   
-> 6 months - 1 year:

   Bloomberg 7
   Google 3
   tcs 3
   Microsoft 2
   Uber 2
   Goldman Sachs 2
   persistent systems 2
   
-> 1 year - 2 years:

   Yahoo 3
   Oracle 3
   Snapchat 2
   Facebook 2
   Infosys 2
   Twitter
"""
"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
Input: numRows = 1
Output: [[1]]
 
Constraints:

1 <= numRows <= 30
"""


-----------------solution in python---------
def generate(self, numRows: int) -> List[List[int]]:
       ans_t=[]
       for i in range(numRows):
           temp_t=[]
           for j in range(i+1):
               if j==0 or j==i:
                   temp_t.append(1)
               else:
                    temp_t.append(ans_t[i-1][j] + ans_t[i-1][j-1])
           ans_t.append(temp_t)
       return ans_t

#time complexity is O(N^2)
