"""
--------------companies-------------------------------------------
0 - 6 months
    Amazon 9
    Adobe 5
    Google 5
    Apple 3
6 months - 1 year
    Facebook 9
    Microsoft 8
    Bloomberg 7
    Walmart Labs 5
    Uber 4
    Yahoo 3
    Visa 3
    MakeMyTrip 3
    Goldman Sachs 2
    eBay 2
    Cisco 2
    TikTok 2
1 year - 2 years
    Qualtrics 6
    Salesforce 5
    VMware 5
    PayPal 4
    ByteDance 4
    Oracle 4
    Morgan Stanley 4
    American Express 4
    Infosys 4
    Intuit 3
    LinkedIn 3
    Tesla 3
    ServiceNow 2
    SAP 2
    Flipkart 2
    IBM 2
    Arcesium 2
    Intel 2
"""

"""
---------------------------------problem statement--------------------------------------
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.


Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
"""

#solution in python
def triplet(arr,n)->list[list[int]]:
    ans = []
    arr.sort()
    for i in range(n):
        if i>0 and arr[i] == arr[i-1]:
            continue
        j=i+1
        k=n-1
        while(j<k):
            sum1 = arr[i]+arr[j]+arr[k]
            if sum1>0:
                k-=1
            elif sum1<0:
                j+=1
            else:
                temp = []
                temp = [arr[i],arr[j],arr[k]]
                ans.append(temp)
                j+=1
                k-=1
                while j<k and arr[j] == arr[j-1]:
                    j+=1
                while k<k and arr[k] == arr[k+1]:
                    k-=1
    return ans


def main()->None:
    arr=list(map(int, input().split(" ")))
    print(triplet(arr,len(arr)))

main()
