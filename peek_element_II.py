"""
A peak element in a 2D grid is an element that is strictly greater than all of its adjacent neighbors to the left, right, top, and bottom.

Given a 0-indexed m x n matrix mat where no two adjacent cells are equal, find any peak element mat[i][j] and return the length 2 array [i,j].

You may assume that the entire matrix is surrounded by an outer perimeter with the value -1 in each cell.

You must write an algorithm that runs in O(m log(n)) or O(n log(m)) time.

 

Example 1:



Input: mat = [[1,4],[3,2]]
Output: [0,1]
Explanation: Both 3 and 4 are peak elements so [1,0] and [0,1] are both acceptable answers.
Example 2:



Input: mat = [[10,20,15],[21,30,14],[7,16,32]]
Output: [1,1]
Explanation: Both 30 and 32 are peak elements so [1,1] and [2,2] are both acceptable answers.

"""


#solution in python
def RowInd(mat,col):
    maxVal = -1
    maxInd = -1
    for i in range(len(mat)):
        if mat[i][col]>maxVal:
            maxVal = mat[i][col]
            maxInd = i
    return maxInd
def findPeekInMat(mat):
    m = len(mat[0])
    low = 0
    high = m-1
    while low<=high:
        mid = (low + high)//2
        maxRowInd = RowInd(mat,mid)
        left = mid-1
        if left>=0:
            left = mat[maxRowInd][mid-1]
        else:
            left=-1
        right = mid+1
        if right<m:
            right = mat[maxRowInd][mid+1]
        else:
            right = -1

        if mat[maxRowInd][mid]>left and mat[maxRowInd][mid]>right:
            return [maxRowInd,mid]
        elif mat[maxRowInd][mid]<left:
            high = mid-1
        else:
            low = mid+1
    return [-1,-1]

def main():
    mat = [[10,20,15],[21,30,14],[7,16,32]]
    print(findPeekInMat(mat))

main() 
        
