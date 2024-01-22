"""
--------------------------------------------Companies------------------------------------------------------------
0 - 6 months
    Amazon 3
    Apple 2
    Amazon 4
6 months - 1 year
    Google 2
    Adobe 2
1 year - 2 years
    Bloomberg 5
    Uber 4
    Facebook 3
    Adobe 3
    Microsoft 3
    Yahoo 2
    TikTok 2
"""

"""
--------------------------------------------problem statement------------------------------------------------------------------
Given an integer array nums, return the number of reverse pairs in the array.

A reverse pair is a pair (i, j) where:

0 <= i < j < nums.length and
nums[i] > 2 * nums[j].
 

Example 1:

Input: nums = [1,3,2,3,1]
Output: 2
Explanation: The reverse pairs are:
(1, 4) --> nums[1] = 3, nums[4] = 1, 3 > 2 * 1
(3, 4) --> nums[3] = 3, nums[4] = 1, 3 > 2 * 1
Example 2:

Input: nums = [2,4,3,5,1]
Output: 3
Explanation: The reverse pairs are:
(1, 4) --> nums[1] = 4, nums[4] = 1, 4 > 2 * 1
(2, 4) --> nums[2] = 3, nums[4] = 1, 3 > 2 * 1
(3, 4) --> nums[3] = 5, nums[4] = 1, 5 > 2 * 1
"""

#problem solution in python:
def merge(arr,low,mid,high):
    left = low
    i = low
    right = mid + 1
    ans = []
    while (left<=mid and right<=high):
        if arr[left] <= arr[right]:
            ans.append(arr[left])
            left+=1
        else:
            ans.append(arr[right])
           
            right+=1
    while left<=mid:
        ans.append(arr[left])
        left+=1
    
    while right<=high:
        ans.append(arr[right])
        right+=1

    for num in ans:
        arr[i] = num
        i+=1

def countpair(arr,low,mid,high):
    cnt = 0
    right = mid+1
    for i in range(low,mid+1):
        while right<=high and arr[i]>2*arr[right]:
            right+=1
        cnt +=(right - (mid+1))
    return cnt

def mergeSort(arr,low,high):
    cnt=0
    if low>=high:
        return cnt 
    mid = (low + high)//2
    cnt+=mergeSort(arr,low,mid)
    cnt+=mergeSort(arr,mid+1,high)
    cnt+=countpair(arr,low,mid,high)
    merge(arr,low,mid,high)
    
    return cnt

def reversePair(arr,n):
    return mergeSort(arr,0,n-1)

def main():
    arr = [2,4,3,5,1]
    print(reversePair(arr,len(arr)))

main()
