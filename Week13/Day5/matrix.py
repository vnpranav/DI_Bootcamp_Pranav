matrix_str = """7ii
Tsx
h%?
i #
sM 
$a 
#t%
^r!"""

# Step 1: Convert the matrix string into a 2D list
matrix = [list(row) for row in matrix_str.splitlines()]

num_rows = len(matrix)
num_cols = len(matrix[0]) if matrix else 0

decoded_message = []

for col in range(num_cols):
    column_chars = []
    for row in range(num_rows):
        char = matrix[row][col]
        if char.isalnum():  
            column_chars.append(char)
    decoded_message.extend(column_chars)
    decoded_message.append(' ')  

decoded_message_str = ''.join(decoded_message).strip()

# Print the decoded message
print("Decoded message:")
print(decoded_message_str)