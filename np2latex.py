def np2latex(arr, column=True):
    if len(arr.shape) == 2:
        return _make_matrix(arr)
    elif len(arr.shape) == 1:
        if column:
            return _make_matrix(arr.reshape(-1, 1))
        else:
            return _make_matrix(arr.reshape(1, -1))
    else:
        raise ValueError("Array must be 1 or 2 dimensional.")
    
def _make_matrix(arr):
    n_cols = arr.shape[1]
    left = "\\left( \\begin{{array}}{{{}}} ".format('c'*arr.shape[1])
    right = " \\end{array} \\right)"
    rows = [_make_row_format_string(n_cols).format(*row)
            for row in arr]
    return left + ' '.join(rows) + right

def _make_row_format_string(n_columns, format_str=":2.2f", join_str=" & "):
    return join_str.join(["{" + format_str + "}"]*n_columns) + r" \\"
