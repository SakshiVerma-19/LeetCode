class Solution {
    public void setZeroes(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == 0) {
                    for (int col = 0; col < matrix[0].length; col++) {
                        if (matrix[i][col] != 0)
                            matrix[i][col] = -10;
                    }
                    for (int row = 0; row < matrix.length; row++) {
                        if (matrix[row][j] != 0)
                            matrix[row][j] = -10;
                    }
                }

            }

        }
        for (int k = 0; k < m; k++) {
            for (int j = 0; j < n; j++) {
                if (matrix[k][j] == -10) {
                    matrix[k][j] = 0;
                }
            }
        }
    }
}

