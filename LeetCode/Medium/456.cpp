// 132 Pattern
// Medium
// Stack

#include <vector>
#include <stack>
using namespace std;
bool find132pattern(vector<int>& nums) {
    // my solution
    // int min = nums[0];
    // int max;
    // for (int i = 1; i < nums.size(); i++) {
    //     for (; i < nums.size() && nums[i] < min; i++) {
    //         min = nums[i];
    //     }
    //
    //     max = nums[i];
    //     for (int j = i+1; j < nums.size(); j++) {
    //         if (nums[j] >= max) {
    //             max = nums[j];
    //         }
    //         else if (nums[j] > min) {
    //             return true;
    //         }
    //     }
    // }
    //
    // return false;

    // better solution
    // array의 뒤에서부터 체크하면서 지금까지의 middle후보들을 track함
    stack<int> stack; // 현재 middle보다 큰 숫자들이 가장 큰 숫자부터 들어있음
    int middle = INT_MIN;
    for (int i = nums.size() - 1; i >= 0; i--) { // from the back of the array
        if (nums[i] < middle) // 새로운 숫자가 middle보다 작다면 true
            return true;

        // 새로운 숫자가 middle보다 더 크다면
        while (!stack.empty() && stack.top() < nums[i]) { // 지금 숫자보다 작은 숫자들은 middle로 들어감
            middle = stack.top();
            stack.pop();
        }

        stack.push(nums[i]);
    }

    return false;
}