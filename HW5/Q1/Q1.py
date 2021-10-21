def transpose(input_list):
    # iterate over columns
    num_rows = len(input_list)
    num_cols = len(input_list[0])
    result = []
    for col_i in range(num_cols):
        row =[]
        for row_i in range(num_rows):
            input_row = input_list[row_i]
            row.append(input_row[col_i])
        result.append(row)
    return result
# test the output
input_list = [[10, 8], [2, 4], [1, 7]]
print(transpose(input_list))
 