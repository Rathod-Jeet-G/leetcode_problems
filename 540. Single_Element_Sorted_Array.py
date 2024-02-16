"""
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.

 

Example 1:
Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:
Input: nums = [3,3,7,7,10,11,11]
Output: 10

Example 3:
Input: nums = [1,2,2,3,3]
Output: 1

Example 4:
Input: nums = [1,1,2]
Output: 2
"""


# solution in python
def single(arr):
    n = len(arr)
    if n == 1:
        return arr[0]
    if arr[0]!=arr[1]:
        return arr[0]
    if arr[n-1]!=arr[n-2]:
        return arr[n-1]
    low = 1
    high = n-2
    while low<=high:
        mid = (low + high)//2
        if arr[mid]!=arr[mid-1] and arr[mid]!=arr[mid+1]:
            return arr[mid]
        
        if ((mid % 2 == 1 and arr[mid] == arr[mid-1]) or (mid % 2 == 0 and arr[mid] == arr[mid+1] )):
            low = mid+1
        else:
            high = mid-1
    return -1

def main():
#->simple test case:    # arr = [1,1,2,3,3,4,4,8,8]
    """
    this is a test case where we need to check the edge cases like
    if arr[n-1]!=arr[n-2]:
        return arr[n-1]
    if you are not under stand the you can driye run the code with writen above step

    arr = [1,1,2]
    """

    """
    this is a test case where we need to check the edge cases like
    if arr[0]!=arr[1]:
        return arr[0]
    
    arr = [1,2,2,3,3]
    """
    arr = [1,2,2,3,3]
    print("single element is: ",single(arr))

main()
    
