# Function to display a sparse matrix
def display_sparse_matrix(matrix):
    print(f"Sparse Matrix Representation: [row, col, value]")
    for element in matrix:
        print(f"[{element[0]}, {element[1]}, {element[2]}]")

# Simple Transpose: swaps row and column for each element
def simple_transpose(matrix, rows, cols):
    transposed_matrix = []
    for element in matrix:
        transposed_matrix.append([element[1], element[0], element[2]])  # Swap row and col
    
    # Manual sorting by row first and then by column
    for i in range(len(transposed_matrix) - 1):
        for j in range(i + 1, len(transposed_matrix)):
            if (transposed_matrix[i][0] > transposed_matrix[j][0]) or \
               (transposed_matrix[i][0] == transposed_matrix[j][0] and transposed_matrix[i][1] > transposed_matrix[j][1]):
                # Swap
                transposed_matrix[i], transposed_matrix[j] = transposed_matrix[j], transposed_matrix[i]
    
    return transposed_matrix, cols, rows  # Returning the transposed matrix and swapped dimensions

# Function to add two sparse matrices
def add_sparse_matrices(matrix1, matrix2, rows, cols):
    if len(matrix1) == 0 and len(matrix2) == 0:
        print("Both matrices are empty.")
        return []
    
    result_matrix = []
    i, j = 0, 0
    while i < len(matrix1) and j < len(matrix2):
        r1, c1, v1 = matrix1[i]
        r2, c2, v2 = matrix2[j]

        if r1 == r2 and c1 == c2:
            # Same position, so we add the values
            result_matrix.append([r1, c1, v1 + v2])
            i += 1
            j += 1
        elif r1 < r2 or (r1 == r2 and c1 < c2):
            # Take element from matrix1
            result_matrix.append([r1, c1, v1])
            i += 1
        else:
            # Take element from matrix2
            result_matrix.append([r2, c2, v2])
            j += 1

    # Append remaining elements from matrix1 or matrix2
    while i < len(matrix1):
        result_matrix.append(matrix1[i])
        i += 1
    while j < len(matrix2):
        result_matrix.append(matrix2[j])
        j += 1

    return result_matrix

# Function to create a sparse matrix from user input
def create_sparse_matrix():
    rows = int(input("Enter number of rows in the matrix: "))
    cols = int(input("Enter number of columns in the matrix: "))
    num_non_zero = int(input("Enter the number of non-zero elements: "))
    
    elements = []
    for _ in range(num_non_zero):
        r = int(input("Enter row index (0-based): "))
        c = int(input("Enter column index (0-based): "))
        v = int(input("Enter value: "))
        elements.append([r, c, v])

    return elements, rows, cols

# Main function
def main():
    print("Input first sparse matrix:")
    matrix1, rows1, cols1 = create_sparse_matrix()
    print("\nOriginal Sparse Matrix 1:")
    display_sparse_matrix(matrix1)

    print("\nInput second sparse matrix:")
    matrix2, rows2, cols2 = create_sparse_matrix()
    print("\nOriginal Sparse Matrix 2:")
    display_sparse_matrix(matrix2)

    # Perform Simple Transpose of matrix1
    transposed_matrix1, transposed_rows1, transposed_cols1 = simple_transpose(matrix1, rows1, cols1)
    print("\nSimple Transpose of the first Sparse Matrix:")
    display_sparse_matrix(transposed_matrix1)

    # Perform Addition of matrix1 and matrix2
    if rows1 == rows2 and cols1 == cols2:
        added_matrix = add_sparse_matrices(matrix1, matrix2, rows1, cols1)
        print("\nAddition of the two Sparse Matrices:")
        display_sparse_matrix(added_matrix)
    else:
        print("Matrices cannot be added due to different dimensions.")

if __name__ == "__main__":
    main()



# the overall time complexity for the most significant operations in the code is:
# for transposing a matrix: O(k log k)
# For adding two matrices: O(k1 + k2) (where k1 and k2 are the number of non-zero elements in the two matrices)

# In general, the time complexity of the sparse matrix operations is dominated by the number of non-zero elements in the matrix,
# and for each operation, it's linear or logarithmic in the number of non-zero elements.