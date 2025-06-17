// Available Captures for Rook
// Easy

#include <vector>
using namespace std;

int numRookCaptures(vector<vector<char>>& board) {
    int count = 0;

    for (int i = 0; i < 8; i++) {
        for (int j = 0; j < 8; j++) {
            if (board[i][j] == 'R') {
                // check up
                for (int n = i-1; n >= 0; n--) {
                    if (board[n][j] == '.')
                        continue;
                    else if (board[n][j] == 'B')
                        break;
                    else if (board[n][j] == 'p') {
                        count++;
                        break;
                    }
                }

                // down
                for (int n = i+1; n < 8; n++) {
                    if (board[n][j] == '.')
                        continue;
                    else if (board[n][j] == 'B')
                        break;
                    else if (board[n][j] == 'p') {
                        count++;
                        break;
                    }
                }

                // left
                for (int n = j-1; n >= 0; n--) {
                    if (board[i][n] == '.')
                        continue;
                    else if (board[i][n] == 'B')
                        break;
                    else if (board[i][n] == 'p') {
                        count++;
                        break;
                    }
                }

                // right
                for (int n = j+1; n < 8; n++) {
                    if (board[i][n] == '.')
                        continue;
                    else if (board[i][n] == 'B')
                        return count;
                    else if (board[i][n] == 'p')
                        return count+1;
                }

                return count;
            }
        }
    }

    return count;
}
