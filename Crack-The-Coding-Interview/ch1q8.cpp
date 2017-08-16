#include <iostream>
#include <stdlib.h>
#include <ctime>
using namespace std;


template <int R, int C>
void setRowZero(int row, int col, int(&mat)[R][C])
{
    for (int i = 0; i < col; i++) {
        mat[row][i] = 0;
    }
}

int main() {
    int m = 5;
    int n = 3;
    int matrix[5][3];

    srand(time(NULL));

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            matrix[i][j] = rand() % 10;
        }
    }

    for (int i = 0; i < m; i++) {
        cout << endl;
        for (int j = 0; j < n; j++) {
            cout << matrix[i][j] << " ";
        }
    }

        cout << endl << endl;

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (matrix[i][j] == 0) {
                setRowZero(i, n, matrix);
            }
        }
    }

    for (int i = 0; i < m; i++) {
        cout << endl;
        for (int j = 0; j < n; j++) {
            cout << matrix[i][j] << " ";
        }
    }


}
