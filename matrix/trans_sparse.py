# Function to display the sparse matrix
def display_sparse_matrix(rows, cols, elements):
    print(f"Sparse Matrix Representation: [row, col, value]")
    for element in elements:
        print(f"[{element[0]}, {element[1]}, {element[2]}]")

# Function for simple transpose of a sparse matrix
def simple_transpose_sparse_matrix(rows, cols, elements):
    transposed_elements = []
    for element in elements:
        transposed_elements.append([element[1], element[0], element[2]])  # Swap row and col
    # Sort the transposed elements by row and column
    transposed_elements.sort(key=lambda x: (x[0], x[1]))
    return cols, rows, transposed_elements  # New rows and cols swapped

# Function for fast transpose of a sparse matrix
def fast_transpose_sparse_matrix(rows, cols, elements):
    row_terms = [0] * cols
    starting_pos = [0] * cols
    transposed_elements = [[0, 0, 0]] * len(elements)

    # Step 1: Count the number of elements in each column (row in transposed matrix)
    for element in elements:
        row_terms[element[1]] += 1

    # Step 2: Calculate starting position for each column in transposed matrix
    starting_pos[0] = 0
    for i in range(1, cols):
        starting_pos[i] = starting_pos[i - 1] + row_terms[i - 1]

    # Step 3: Place elements in correct position in transposed matrix
    for element in elements:
        col = element[1]
        pos = starting_pos[col]
        transposed_elements[pos] = [element[1], element[0], element[2]]  # Swap row and col
        starting_pos[col] += 1

    return cols, rows, transposed_elements  # Return swapped dimensions with transposed elements

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

    return rows, cols, elements

# Main function
def main():
    rows, cols, sparse_matrix = create_sparse_matrix()
    print("\nOriginal Sparse Matrix:")
    display_sparse_matrix(rows, cols, sparse_matrix)

    # Perform Simple Transpose
    new_rows, new_cols, simple_transposed = simple_transpose_sparse_matrix(rows, cols, sparse_matrix)
    print("\nSimple Transpose of the Sparse Matrix:")
    display_sparse_matrix(new_rows, new_cols, simple_transposed)

    # Perform Fast Transpose
    new_rows, new_cols, fast_transposed = fast_transpose_sparse_matrix(rows, cols, sparse_matrix)
    print("\nFast Transpose of the Sparse Matrix:")
    display_sparse_matrix(new_rows, new_cols, fast_transposed)

if __name__ == "__main__":
    main()

    
    
    
    
    
    # Time complexity of simple transpose=O(nlogn)
    # Time complexity of fast transpose=O(n+m)
    # Display: O(n)
    # In the worst case, for large matrices with many non-zero elements, the fast transpose will likely be more efficient than the simple transpose