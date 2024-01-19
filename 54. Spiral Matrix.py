"""
----------------------------------------------------------companies-----------------------------------------------------------------------
-> 0 - 6 months:
        Amazon 9
        Microsoft 4
        Apple 4
        Adobe 4
        TikTok 3
        Facebook 2
        
-> 6 months - 1 year:
        Google 5
        Cisco 4
        Epic Systems 2
        Bloomberg 2
        Uber 2
        Yahoo 2
        Oracle 2
        Virtu Financial 2
        
-> 1 year - 2 years:
        Intuit 6
        Zillow 5
        Walmart Labs 4
        VMware 4
        LiveRamp 4
        Nvidia 3
        Flipkart 3
        Redfin 2
        ByteDance 2
        Paytm 2
        HBO 2
        Snapdeal 2
        EPAM Systems 2
        Dunzo 2
"""

"""
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""

#------------------------------------------------------------Solution Time Complexity is O(N*M) and Space complexity is O(N)---------------------------------------------------

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
def spiral_matrix(matrix):
    n = len(matrix)
    m = len(matrix[0])
    top = 0
    right = m-1
    left = 0
    botoom = n-1
    temp = []
    while(top<=botoom and left<=right):
        for i in range(left,right+1):
            temp.append(matrix[top][i])
        top+=1
        
        for i in range(top,botoom+1):
            temp.append(matrix[i][right])
        right-=1

        if top<=botoom:
            for i in range(right,left-1,-1):
                temp.append(matrix[botoom][i])
            botoom-=1
        if left<=right:
            for i in range(botoom,top-1,-1):
                temp.append(matrix[i][left])
            left+=1
    return temp
print(spiral_matrix(matrix))
