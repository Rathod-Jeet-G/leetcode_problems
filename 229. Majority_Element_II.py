"""
----------------------------------companies-------------------------------------------
-> 0 - 6 months
      Amazon 2
      Adobe 2
-> 6 months - 1 year
      Apple 4
      Google 3
-> 1 year - 2 years
      Microsoft 4
      Bloomberg 4
      Facebook 2
      Rubrik 2
      Zenefits
"""

"""
------------------------------------problem statment---------------------------------------
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

 

Example 1:

Input: nums = [3,2,3]
Output: [3]
Example 2:

Input: nums = [1]
Output: [1]
Example 3:

Input: nums = [1,2]
Output: [1,2]
"""

# problem solution in python
def majorityElement2(arr,n):
    cnt1,cnt2,el1,el2=0,0,0,0
    ans = []
    for i in range(n):
        if cnt1==0 and arr[i]!=el2:
            cnt1=1
            el1 = arr[i]
        elif cnt2 == 0 and arr[i]!=el1:
            cnt2=1
            el2 = arr[i]
        elif arr[i] == el1:
            cnt1+=1
        elif arr[i] == el2:
            cnt2+=1
        else:
            cnt1-=1
            cnt2-=1
    
    cnt1,cnt2=0,0
    for i in range(n):
        if arr[i] == el1:
            cnt1+=1
        if arr[i] == el2:
            cnt2+=1
    
    if cnt1>(n//3):
        ans.append(el1)
    if cnt2>(n//3):
        ans.append(el2)

    if el1 == 0 and el2 == 0:
        return [0]
    return ans

def main():
    arr = [3,2,3]
    print(majorityElement2(arr,len(arr)))

main()

        

