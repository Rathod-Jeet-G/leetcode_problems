"""
----------------------comapnies------------------------------------
-> 6 months - 1 year
    Amazon 3
-> 1 year - 2 years
    Goldman Sachs 5
    Microsoft 3
    Yahoo 2
"""


"""
-----------------------problem statement-------------------------------------
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]
 
"""


# solution in pytho
def generatePascalTriangel(rowIndex):
    pascal = []
    for i in range(rowIndex+1):
        temp = []
        for j in range(i+1):
            if j == 0 or j==i:
                temp.append(1)
            else:
                temp.append(pascal[i-1][j] + pascal[i-1][j-1])
        pascal.append(temp)
    return pascal[rowIndex]
        
def main():
    print(generatePascalTriangel(3))

main()
