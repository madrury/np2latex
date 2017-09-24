import numpy as np


def np2latex(arr, column=True):
    """Return latex markdown representing a numpy array.

    Parameters
    ----------
    arr: array, shape (n, p), (n,) or (1, n)
        A numpy array.

    column: boolean
        When the arr argument is one dimensional, this controls whether to
        return latex for a column or row vector. Defaults to True (indicating a
        column vector).

    Returns
    -------
    latex: string
        A latex string.
    """
    if len(arr.shape) == 2:
        return _make_matrix(arr)
    elif len(arr.shape) == 1:
        if column:
            return _make_matrix(arr.reshape(-1, 1))
        else:
            return _make_matrix(arr.reshape(1, -1), end_str="")
    else:
        raise ValueError("Array must be 1 or 2 dimensional.")
    
def _make_matrix(arr, **kwargs):
    n_cols = arr.shape[1]
    left = "\\left( \\begin{{array}}{{{}}} ".format('c'*arr.shape[1])
    right = " \\end{array} \\right)"
    rows = [_make_row_format_string(n_cols, **kwargs).format(*row)
            for row in arr]
    return left + ' '.join(rows) + right

def _make_row_format_string(n_columns, format_str=":2.2f", end_str=r" \\"):
    return " & ".join(["{" + format_str + "}"]*n_columns) + end_str
