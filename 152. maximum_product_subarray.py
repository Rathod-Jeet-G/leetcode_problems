"""
----------------------------------------------Companies----------------------------------------------------------
0 - 6 months
    Amazon 2
    Microsoft 2
    Apple 2
    Uber 2
6 months - 1 year
    LinkedIn 3
    Google 3
    Adobe 3
    Expedia 2
    Facebook 2
    Yahoo 2
1 year - 2 years
    Bloomberg 3
    Infosys 3
    Oracle 2
    JPMorgan 2
"""

"""
----------------------------------------problem statement------------------------------------------------------
Given an integer array nums, find a 
subarray
 that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""

#solution in python
def maximum_product_subarray(arr,n):
    prefix = 1
    sufix = 1
    maxpro = float('-inf')

    for i in range(n):
        if prefix == 0:
            prefix = 1
        if sufix == 0:
            sufix =1
        
        prefix *=arr[i]
        sufix *=arr[n-i-1]

        maxpro = max(maxpro,max(prefix,sufix))
    return maxpro
    
def main():
    arr = list(map(int,input().split(" ")))
    print(maximum_product_subarray(arr,len(arr)))

main()
