// First Completely Painted Row or Column
// Medium

#include <set>
#include <map>
#include <vector>
using namespace std;

/* first method, TLE
int firstCompleteIndex(vector<int>& arr, vector<vector<int>>& mat) {
    map<int, map<int, int>*> rows;
    map<int, set<int>*> cols;

    int rowCount = mat.size();
    int colCount = mat.at(0).size();
    for (int i = 0; i < rowCount; i++) {
        rows.emplace(i, new map<int, int>);
        for (int j = 0; j < colCount; j++) {
            rows.at(i)->emplace(mat[i][j], j);
        }
    }

    for (int j = 0; j < colCount; j++) {
        cols.emplace(j, new set<int>);
        for (int i = 0; i < rowCount; i++) {
            cols.at(j)->emplace(mat[i][j]);
        }
    }

    for (int i = 0; i < arr.size(); i++) {
        for (auto pair: rows) {
            auto loc = pair.second->find(arr[i]);
            if (loc != pair.second->end()) {
                cols.at(loc->second)->erase(arr[i]);
                if (cols.at(loc->second)->empty())
                    return i;

                pair.second->erase(arr[i]);
                if (pair.second->empty())
                    return i;
            }
        }
    }
}
*/

/* Second method using map, passed
class Solution {
public:
    int firstCompleteIndex(vector<int>& arr, vector<vector<int>>& mat) {
        map<int, int> index; // num to position
        int rowCount = mat.size();
        int colCount = mat.at(0).size();

        for (int i = 0; i < rowCount; i++) {
            for (int j = 0; j < colCount; j++) {
                index.emplace(mat[i][j], i*colCount + j);
            }
        }

        vector<short> rows(rowCount, colCount);
        vector<short> cols(colCount, rowCount);

        for (int i = 0; i < arr.size(); i++) {
            auto pos = index.find(arr[i]);

            if (--rows.at(pos->second / colCount) == 0)
                return i;

            if (--cols.at(pos->second % colCount) == 0)
                return i;

            // index.erase(pos);
        }

        return -1;
    }
};
*/

// Third method using vector, much faster
int firstCompleteIndex(vector<int>& arr, vector<vector<int>>& mat) {
    int rowCount = mat.size();
    int colCount = mat.at(0).size();
    vector<int> index(rowCount * colCount);

    for (int i = 0; i < rowCount; i++) {
        for (int j = 0; j < colCount; j++) {
            index.at(mat[i][j]-1) = i*colCount + j; // vector is 0-indexed, but input is 1-indexed
        }
    }

    vector<int> rows(rowCount, colCount);
    vector<int> cols(colCount, rowCount);

    for (int i = 0; i < arr.size(); i++) {
        auto pos = index.at(arr[i]-1);

        if (--rows.at(pos / colCount) == 0)
            return i;

        if (--cols.at(pos % colCount) == 0)
            return i;
    }

    return -1;
}
