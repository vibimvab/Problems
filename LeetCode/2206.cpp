// Divide Array into Equal Parts
// Easy

#include <vector>
#include <set>
using namespace std;

/* first method using set
bool divideArray(vector<int>& nums) {
    set<int> set;
    for (int num: nums) {
        auto loc = set.find(num);
        if (loc == set.end()) {
            set.insert(num);
        } else {
            set.erase(loc);
        }
    }

    return set.empty();
}
*/

// second method using vector
// might be slower if the constraint of nums is much bigger
bool divideArray(vector<int>& nums) {
    vector<bool> count(501, false);
    for (int num: nums) {
        count[num] = !count[num];
    }

    for (bool loc: count)
        if (loc) return false;
    return true;
}
