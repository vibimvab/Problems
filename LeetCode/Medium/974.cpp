//
// Created by Insung Seo on 6/9/24.
//

#include <vector>
#include <map>
#include <iostream>

using namespace std;

int subarraysDivByK(vector<int>& nums, int k) {
    // method using vector
    std::vector<int> newSubarray(k, 0);
    newSubarray.at(0) = 1;
    int result = 0;
    int currentSum = 0;

    for (int num : nums) {
        // shifting
        currentSum = (num + currentSum) % k;
        if (currentSum < 0)
            currentSum += k;

        // finding
        result += newSubarray.at(currentSum)++;

        // adding
        // newSubarray.at(currentSum)++;
    }

    // method using map
//    map<int, int> elementToNumNewSubarray;
//    elementToNumNewSubarray[0] = 1;
//    int result = 0;
//    int currentSum = 0;
//
//    for (int num : nums) {
//        // shifting
//        currentSum = (num + currentSum) % k;
//        if (currentSum < 0)
//            currentSum += k;
//
//        // finding
//        try {
//            result += elementToNumNewSubarray.at(currentSum);
//        } catch (const out_of_range& e) {
//            result += 0;
//        }
//
//        // adding
//        try {
//            elementToNumNewSubarray.at(currentSum)++;
//        } catch (const out_of_range& e) {
//            elementToNumNewSubarray[currentSum] = 1;
//        }
//    }

    return result;
}

int main() {
    vector<int> nums = {7, 4, -10};
    int k = 5;
    cout << subarraysDivByK(nums, k) << endl;
}
