# Function to compute the transpose of a matrix
def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transposed = [[0] * rows for _ in range(cols)]  # Create an empty matrix of the transposed dimensions

    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]  # Swap row and column for transpose
    
    return transposed

# Function to add two matrices
def add_matrices(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])
    result = [[0] * cols for _ in range(rows)]  # Create an empty matrix for the result

    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix1[i][j] + matrix2[i][j]  # Element-wise addition
    
    return result

# Function to multiply two matrices
def multiply_matrices(matrix1, matrix2):
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])

    # Ensure the matrices can be multiplied (cols of matrix1 must equal rows of matrix2)
    if cols1 != rows2:
        print("Matrix multiplication is not possible (shape mismatch).")
        return None

    # Initialize the result matrix
    result = [[0] * cols2 for _ in range(rows1)]

    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]  # Multiply row of matrix1 by column of matrix2

    return result

# Function to find the saddle point
def find_saddle_point(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    saddle_points = []

    for i in range(rows):
        # Find the minimum value in the ith row
        row_min = min(matrix[i])
        col_index = matrix[i].index(row_min)

        # Check if it's the largest value in its column
        col_max = max(matrix[k][col_index] for k in range(rows))
        
        if row_min == col_max:
            saddle_points.append((i, col_index, row_min))

    return saddle_points

# Function to take input from user and form a matrix
def input_matrix():
    rows = int(input("Enter the number of rows for the matrix: "))
    cols = int(input("Enter the number of columns for the matrix: "))
    matrix = []
    print(f"Enter the elements of the matrix (row by row):")
    for i in range(rows):
        row = list(map(int, input(f"Row {i+1}: ").split()))
        matrix.append(row)
    return matrix

# Main program
def main():
    print("Enter details for matrix 1:")
    matrix1 = input_matrix()

    print("\nTranspose of Matrix 1:")
    transposed = transpose_matrix(matrix1)
    for row in transposed:
        print(row)

    print("\nEnter details for matrix 2:")
    matrix2 = input_matrix()

    if len(matrix1) == len(matrix2) and len(matrix1[0]) == len(matrix2[0]):
        print("\nAddition of matrices:")
        added = add_matrices(matrix1, matrix2)
        for row in added:
            print(row)
    else:
        print("\nMatrix addition is not possible (shape mismatch).")

    if len(matrix1[0]) == len(matrix2):
        print("\nMultiplication of matrices:")
        multiplied = multiply_matrices(matrix1, matrix2)
        for row in multiplied:
            print(row)
    else:
        print("\nMatrix multiplication is not possible (shape mismatch).")

    print("\nFinding saddle points in Matrix 1:")
    saddle_points = find_saddle_point(matrix1)
    if saddle_points:
        for (i, j, val) in saddle_points:
            print(f"Saddle point found at row {i+1}, column {j+1} with value {val}.")
    else:
        print("No saddle point found in Matrix 1.")

if __name__ == "__main__":
    main()


# The transpose operation has 𝑂(𝑚×𝑛)
# The matrix addition has O(m×n).
# The matrix multiplication has O(m×p×n), which can vary depending on the dimensions of the matrices.
# The saddle point detection has O(m×n).
# The matrix input takes O(m×n)


# Final Time Complexity Summary:
# Overall Time Complexity: O(m×n) for most operations, except for matrix multiplication, which is O(m×p×n).