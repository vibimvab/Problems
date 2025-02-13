// Flipping an Image
// Easy

#include <vector>
using namespace std;

/* first method using (n+1)%2 to invert
vector<vector<int>> flipAndInvertImage(vector<vector<int>>& image) {
    auto copy = image;

    int rowLen = copy[0].size();
    for (int i = 0; i < copy.size(); i++) {
        for (int j = 0; j < rowLen/2; j++) {
            int temp = (copy[i][j]+1) % 2;
            copy[i][j] = (copy[i][rowLen-1-j]+1) % 2;
            copy[i][rowLen-1-j] = temp;
        }
    }

    if (rowLen % 2 == 1) {
        for (int i = 0; i < copy.size(); i++) {
            copy[i][rowLen/2] = (copy[i][rowLen/2]+1) % 2;
        }
    }

    return copy;
}
*/

/* second method using if ... else to invert
 * equal in time with first method (7ms)
vector<vector<int>> flipAndInvertImage(vector<vector<int>>& image) {
    auto copy = image;

    int rowLen = copy[0].size();
    for (int i = 0; i < copy.size(); i++) {
        for (int j = 0; j < rowLen/2; j++) {
            int temp;
            if (copy[i][j] == 0) temp = 1; else temp = 0;
            if (copy[i][rowLen-1-j] == 0) copy[i][j] = 1; else copy[i][j] = 0;
            copy[i][rowLen-1-j] = temp;
        }
    }

    if (rowLen % 2 == 1) {
        for (int i = 0; i < copy.size(); i++) {
            if (copy[i][rowLen/2] == 0) copy[i][rowLen/2] = 1; else copy[i][rowLen/2] = 0;
        }
    }

    return copy;
}
 */

// third method using ^ (xor) to invert
// fastest (0ms)
vector<vector<int>> flipAndInvertImage(vector<vector<int>>& image) {
    auto copy = image;

    int rowLen = copy[0].size();
    for (int i = 0; i < copy.size(); i++) {
        for (int j = 0; j < rowLen/2 + rowLen%2; j++) {
            int temp = 1 ^ copy[i][j];
            copy[i][j] = 1 ^ copy[i][rowLen-1-j];
            copy[i][rowLen-1-j] = temp;
        }
    }

    return copy;
}