"""
There is an integer array ‘a’ of size ‘n’.

An element is called a Superior Element if it is greater than all the elements present to its right.

You must return an array all Superior Elements in the array ‘a’.

Note:

The last element of the array is always a Superior Element. 


Example
Input: a = [1, 2, 3, 2], n = 4
Output: 2 3
Explanation: 
a[ 2 ] = 3 is greater than a[ 3 ]. Hence it is a Superior Element. 
a[ 3 ] = 2 is the last element. Hence it is a Superior Element.
The final answer is in sorted order.
Detailed explanation ( Input/output format, Notes, Images )

Sample Input 1:
4 
1 2 2 1


Sample Output 1:
1 2


Explanation of Sample Input 1:
Element present at the last index is '1' and is a superior element since there are no integers to the right of it.
Element present at index 2 (0-indexed) is '2' and is greater than all the elements to the right of it.
There are no other superior elements present in the array.
Hence the final answer is [1,2].


Sample Input 2:
3
5 4 3


Sample Output 2:
3 4 5 


Expected Time Complexity:
Try to solve this in O(n).
"""
# solution in python
def leadersInArray(arr,n):
    ans = []
    max_no = 0
    for i in range(n-1,-1,-1):
        if arr[i] > max_no:
            ans.append(arr[i])
        max_no = max(max_no,arr[i])

    return ans

def main():
    arr = [10,22,12,3,0,6]
    print(leadersInArray(arr,len(arr)))

main()
