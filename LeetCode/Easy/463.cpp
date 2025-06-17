// Island Perimeter
// Easy

#include <vector>
using namespace std;

int islandPerimeter(vector<vector<int>>& grid) {
    int perimeter = 0;
    int rowCount = grid.size();
    int colCount = grid.at(0).size();
    for (int i = 0; i < rowCount; i++) {
        for (int j = 0; j < colCount; j++) {
            if (grid[i][j] == 1) {
                // up
                if (i == 0 || grid[i-1][j] == 0)
                    perimeter++;

                // down
                if (i == rowCount - 1 || grid[i+1][j] == 0)
                    perimeter++;

                // left
                if (j == 0 || grid[i][j-1] == 0)
                    perimeter++;

                // right
                if (j == colCount - 1 || grid[i][j+1] == 0)
                    perimeter++;
            }
        }
    }

    return perimeter;
}
