// Largest Perimeter Triangle
// Easy

#include <vector>
using namespace std;

// not sure if there's better solution than sorting
int largestPerimeter(vector<int>& nums) {
    sort(nums.begin(), nums.end());

    for (int i = nums.size()-1; i >= 2; i--) {
        int n = nums[i-1] + nums[i-2];
        if (nums[i] < n) {
            return nums[i] + n;
        }
    }

    return 0;
}
