"""
------companies--------
0 - 6 months
Amazon 6
Google 4
Bloomberg 2
Facebook 2
Yahoo 2

6 months - 1 year
Apple 7
Adobe 6
Microsoft 2

1 year - 2 years
Qualtrics 5
LinkedIn 4
Spotify 4
Visa 3
eBay 3
Morgan Stanley 3
Uber 2
Zillow 2
Goldman Sachs 2
Salesforce 2
Cisco 2
"""

"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
"""



# solution in python
def longestConsicutive(arr,n): #-> time complexity of this algorithm is O(3N)
    st = set()
    cnt = 0
    longest = 0
    if n == 0:
        return 0
    for i in range(n):
        st.add(arr[i])
    
    for number in st:
        if number-1 not in st:
            x = number
            cnt = 1
            while x+1 in st:
                x+=1
                cnt+=1
            longest = max(longest,cnt)
    return longest
