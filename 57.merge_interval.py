"""
-------------------------------------------companies-------------------------------------------------------------
0 - 6 months:
    Amazon 9
    Google 5
    LinkedIn 4
    Apple 3
    Adobe 3
    Uber 3
    Yahoo 3
    Yandex 3
    TikTok 3
    Facebook 2
    Bloomberg 2
6 months - 1 year:
    Microsoft 9
    Cisco 5
    Palantir Technologies 4
    eBay 3
    Salesforce 3
    Booking.com 3
    Expedia 3
    ByteDance 3
    PayPal 2
    Pinterest 2
    Oracle 2
    VMware 2
    Coupang 2
    Atlassian 2
    JPMorgan 2
    Shopee 2
    Cognizant 2
1 year - 2 years:
    IBM 18
    Snapchat 9
    Walmart Labs 9
    Twitter 7
    Reddit 5
    Nvidia 4
    Morgan Stanley 4
    Qualtrics 4
    Wish 3
    ServiceNow 3
    Visa 3
    Splunk 3
    Intuit 2
    Goldman Sachs 2
    Netflix 2
    Twilio 2
    Two Sigma 2
    BlackRock 2
    Tesla 2
    Hotstar 2
    Citadel 2
    Arcesium 2
    Samsung 2
"""

"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

Constraints:
1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104

"""

#---------------solution in python------------------
#worst case solution with time complexity is O(n^2)
    class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:    
        n = len(intervals)
        ans = []
        intervals.sort()

         for i in range(n):
             start, end = intervals[i][0], intervals[i][1]
             if ans and end <= ans[-1][1]:
                 continue
        
             for j in range(i + 1,n):
                 if intervals[j][0] <= end:
                     end = max(end,intervals[j][1])
                 else:
                     break
             ans.append([start, end])
         return ans



#optimal solution with time complexity is O(N)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
         n = len(intervals)
        ans = []
        intervals.sort()
        
        for i in range(n):
            if not ans or ans[-1][1]<intervals[i][0]:
                ans.append(intervals[i])
            else:
                ans[-1][1] = max(ans[-1][1],intervals[i][1])
        return ans

         
