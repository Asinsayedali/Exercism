def saddle_points(matrix):

    if not matrix:
        return []

    row_count = len(matrix[0])
    for i in range(0, len(matrix)):
        if len(matrix[i]) != row_count:
            raise ValueError("irregular matrix")

    column_min = [min(c) for c in zip(*matrix)]
    final_result = []
    for index, row_max in enumerate(max(r) for r in matrix):
        for index_column, column_value in enumerate(column_min):
            if row_max == column_value:
                final_result.append({"row": index + 1, "column": index_column + 1})

    return final_result
