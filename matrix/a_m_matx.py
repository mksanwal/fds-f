# Function to add two matrices
def add_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

# Function to multiply two matrices
def multiply_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            # Calculate the dot product of row i of matrix1 and column j of matrix2
            dot_product = 0
            for k in range(len(matrix2)):
                dot_product += matrix1[i][k] * matrix2[k][j]
            row.append(dot_product)
        result.append(row)
    return result

# Function to check if the matrix is upper triangular
def is_upper_triangular(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(1, rows):
        for j in range(i):
            if matrix[i][j] != 0:
                return False
    return True

# Function to check if the matrix is a magic square
def is_magic_square(matrix):
    n = len(matrix)
    
    # Flatten the matrix and sort to check for all numbers from 1 to n^2
    elements = []
    for row in matrix:
        elements.extend(row)
    elements.sort()
    if elements != list(range(1, n*n + 1)):
        return False

    # Calculate the magic sum (sum of the first row)
    magic_sum = sum(matrix[0])

    # Check row sums
    for row in matrix:
        if sum(row) != magic_sum:
            return False

    # Check column sums
    for j in range(n):
        col_sum = sum(matrix[i][j] for i in range(n))
        if col_sum != magic_sum:
            return False

    # Check diagonal sums
    if sum(matrix[i][i] for i in range(n)) != magic_sum:
        return False
    if sum(matrix[i][n-i-1] for i in range(n)) != magic_sum:
        return False

    return True

# Function to take input from user and form a matrix
def input_matrix():
    n = int(input("Enter the number of rows/columns for the matrix: "))
    matrix = []
    print(f"Enter the elements of the matrix (row by row):")
    for i in range(n):
        row = list(map(int, input(f"Row {i+1}: ").split()))
        matrix.append(row)
    return matrix

# Function to print a matrix
def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

# Main program
def main():
    print("Enter details for matrix 1:")
    matrix1 = input_matrix()
    
    print("Enter details for matrix 2:")
    matrix2 = input_matrix()
    
    print("\nAddition of matrices:")
    result_addition = add_matrices(matrix1, matrix2)
    print_matrix(result_addition)
    
    print("\nMultiplication of matrices:")
    result_multiplication = multiply_matrices(matrix1, matrix2)
    print_matrix(result_multiplication)

    print("\nCheck if Matrix 1 is Upper Triangular:")
    if is_upper_triangular(matrix1):
        print("Matrix 1 is upper triangular.")
    else:
        print("Matrix 1 is not upper triangular.")
    
    print("\nCheck if Matrix 1 is a Magic Square:")
    if is_magic_square(matrix1):
        print("Matrix 1 is a magic square.")
    else:
        print("Matrix 1 is not a magic square.")

if __name__ == "__main__":
    main()


# Overall Time Complexity:
# Matrix Addition (add_matrices): O(n²)
# Matrix Multiplication (multiply_matrices): O(n³)
# Check Upper Triangular (is_upper_triangular): O(n²)
# Check Magic Square (is_magic_square): O(n² log n)
# Matrix Input (input_matrix): O(n²)

# the overall time complexity of the program is dominated by the matrix multiplication function (multiply_matrices),
# which has a complexity of O(n³). Therefore, the overall time complexity of the program is O(n³).