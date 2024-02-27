"""Problem statement
You're given two sorted arrays 'arr1' and 'arr2' of size 'n' and 'm' respectively and an element 'k'.
Find the element that would be at the 'kth' position of the combined sorted array.
Position 'k' is given according to 1 - based indexing, but arrays 'arr1' and 'arr2' are using 0 - based indexing.

For example :
Input: 'arr1' = [2, 3, 45], 'arr2' = [4, 6, 7, 8] and 'k' = 4
Output: 6
Explanation: The merged array will be [2, 3, 4, 6, 7, 8, 45]. The element at position '4' of this array is 6. Hence we return 6.

Sample Input 1:
5
2 3 6 7 9
4
1 4 8 10
4
Sample Output 1:
4
Explanation of sample input 1 :
The merged array will be: [1, 2, 3, 4, 6, 7, 8, 9, 10]

The element at position '4' is 4 so we return 4.
Sample Input 2:
5
1 2 3 5 6
5
4 7 8 9 100  
6
Sample Output 2:
6
Explanation of sample input 2 :
The merged array will be: [1, 2, 3, 4, 5, 6, 7, 8, 9, 100]

The element at position '6'  is 6, so we return 6.
Constraints :
1 <= 'n' <= 5000
1 <= 'm' <= 5000
0 <= 'arr1[i]', 'arr2[i]' <= 10^9
1 <= 'k' <= 'n' + 'm'

'n' and 'm' denote the size of 'arr1' and 'arr2'.

Time limit: 1 second
Expected time complexity :
The expected time complexity is O(log('n') + log('m')). 
"""


#solution in python:
def kthel(a,b,n1,n2,k):
    if n1>n2:
        return kthel(b,a,n2,n1,k)
    left = k
    low = max(0,k-n2)
    high = min(k,n1)
    n = n1+n2
    while low<=high:
        mid1 = (low + high)//2
        mid2 = left - mid1
        l1,l2 = float('-inf'),float('-inf')
        r1,r2 = float('inf'),float('inf')
        if mid1<n1:
            r1 = a[mid1]
        if mid2<n2:
            r2 = b[mid2]
        if mid1-1>=0:
            l1 = a[mid1-1]
        if mid2-1>=0:
            l2 = b[mid2-1]
        if l1<=r2 and l2<=r1:
            return max(l1,l2)
        elif l1>r2:
            high = mid1-1
        else:
            low = mid1+1
    return 0

def main():
    a = [2,3,6,7,9]
    b = [1,4,8,10]
    k = 5
    print(kthel(a,b,len(a),len(b),k))

main()


