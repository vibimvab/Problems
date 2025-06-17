//
// Created by Insung Seo on 6/10/24.
//

#include <vector>
#include <iostream>

using namespace std;

int heightChecker(vector<int>& heights) {
    vector<int> sortedHeights = heights;
    sort(sortedHeights.begin(), sortedHeights.end());

    int result = 0;
    for (int i = 0; i < heights.size(); i++) {
        if (heights.at(i) != sortedHeights.at(i))
            result++;
    }

    return result;
}

int main() {
    vector<int> nums1 = {1,1,4,2,1,3};
    cout << heightChecker(nums1) << endl;

    vector<int> nums2 = {5,1,2,3,4};
    cout << heightChecker(nums2) << endl;

    vector<int> nums3 = {1,2,3,4,5};
    cout << heightChecker(nums3) << endl;
}