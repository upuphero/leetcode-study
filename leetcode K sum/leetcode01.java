int binarySearch(int[] nums, int target) {
    int left = 0; 
    int right = nums.length - 1; // 注意

    while(left <= right) {
        int mid = left + (right - left) / 2;
        if(nums[mid] == target)
            return mid; 
        else if (nums[mid] < target)
            left = mid + 1; // 注意
        else if (nums[mid] > target)
            right = mid - 1; // 注意
    }
    return -1;
}

class Solution {
    bool binaryFind(vector<int>& nums, int l, int r, int val) {
        while(l <= r) {
            int mid = (l + r) >> 1;
            if(nums[mid] < val) {
                l = mid + 1;
            }else if(nums[mid] > val) {
                r = mid - 1;
            }else {
                return true;
            }
        }
        return false;
    }
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        for(int i = 0; i < nums.size(); ++i) {
            if(binaryFind(nums, i+1, nums.size()-1, target - nums[i])) {
                return {nums[i], target - nums[i]};
            }
        }
        return {};
    }
};
