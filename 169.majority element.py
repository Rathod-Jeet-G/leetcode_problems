Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:
n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109

-------------------solution in c++-------------------------
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int count=0;
        int val = 0;
        int n = nums.size();
        for(int i=0;i<n;i++){
            if(count==0){
                val = nums[i];
            }
            if(nums[i] == val){
                count+=1;
            }else{
                count-=1;
            }
        }
        return val;
    }
};

----------------solution in java-----------------------------
class Solution {
    public int majorityElement(int[] nums) {
        int count=0;
        int val = 0;
        int n = nums.length;
        for(int i=0;i<n;i++){
            if(count==0){
                val = nums[i];
            }
            if(nums[i] == val){
                count+=1;
            }else{
                count-=1;
            }
        }
        return val;
    }
}
 -----------solution in python------------------------------------
 def majorityElement(self, nums: List[int]) -> int:
        count = 0
        val = 0
        for i in nums:
            if count == 0:
                val = i
            if i == val:
                count+=1
            else:
                count-=1
        return val
