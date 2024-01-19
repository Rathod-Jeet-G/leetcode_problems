"""
----------------------------------companies---------------------------------------------------------------------
-> 0 - 6 months

    Amazon 6
    Yandex 4
    Apple 3
    Facebook 2
    Microsoft 2
    
-> 6 months - 1 year

    Google 6
    Bloomberg 5
    MathWorks 5
    TikTok 4
    Expedia 3
    Citadel 3
    Adobe 2
    Oracle 2
    Nutanix 2
    Infosys 2
    Bolt 2
    DRW 2
    
-> 1 year - 2 years

    ByteDance 7
    Quora 7
    Visa 7
    Walmart Labs 4
    Tesla 4
    PayPal 4
    Snapchat 3
    LinkedIn 3
    Yahoo 3
    ServiceNow 3
    Twilio 2
    Uber 2
    eBay 2
    Nvidia 2
    JPMorgan 2
    Zillow 2
    DoorDash 2
    Samsung 2

"""

"""
--------------------------------problem description------------------------------------------------------
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
"""

# solution in python 
from collections import defaultdict


def countSubArray(arr,n,k):
    hashMap = defaultdict(int)
    cnt = 0
    preSum = 0
    hashMap[0] = 1
    for i in range(len(arr)):
        preSum += arr[i]
        rem = preSum - k
        cnt += hashMap[rem]
        hashMap[preSum] += 1
    
    return cnt

def main():
    arr = [1,2,3]
    k = 3
    print("Total subArray are:",countSubArray(arr,len(arr),k))

main()

