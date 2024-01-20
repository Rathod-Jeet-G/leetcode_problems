"""
----------------------------------companies-------------------------------------------------
0 - 6 months
    Amazon 5
6 months - 1 year
    Bloomberg 5
    Facebook 4
    Apple 4
    Adobe 2
    Rubrik 2
    Audible 2
1 year - 2 years
    Google 9
    Microsoft 6
    Infosys 4
    Uber 3
    Yahoo 3
    Snapchat 3
    LinkedIn 2
"""

"""
-----------------------------problem statment-----------------------------------------------
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
"""

# solution in python
def fourSum(arr,n,target):
    ans = []
    arr.sort()
    for i in range(n):
        if i>0 and arr[i] == arr[i-1]:
            continue
        for j in range(i+1,n):
            if j>i+1 and arr[j] == arr[j-1]:
                continue
            k = j+1
            l = n-1
            while(k<l):
                sum1 = arr[i]+arr[j]+arr[k]+arr[l]
                if sum1 == target:
                    temp = [arr[i],arr[j],arr[k],arr[l]]
                    ans.append(temp)
                    k+=1
                    l-=1
                    while k<l and arr[k] == arr[k-1]:
                        k+=1
                    while k<l and arr[l] == arr[l+1]:
                        l-=1
                elif sum1<target:
                    k+=1
                else:
                    l-=1
    return ans

def main():
    arr = list(map(int,input().split(" ")))
    target = int(input())
    print(fourSum(arr,len(arr),target))

main()

                    
