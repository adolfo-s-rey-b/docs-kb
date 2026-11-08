[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/linalg/set_diag#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/linalg/set_diag)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/linalg/set_diag?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Flinalg%2Fset_diag&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/linalg/set_diag#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/linalg/set_diag#args)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.linalg.set\_diag Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/linalg/set_diag#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/linalg/set_diag#args)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/array_ops.py#L2433-L2567)

Returns a batched matrix tensor with new batched diagonal values.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.linalg.set_diag`](https://www.tensorflow.org/api_docs/python/tf/linalg/set_diag)
, [`tf.compat.v1.matrix_set_diag`](https://www.tensorflow.org/api_docs/python/tf/linalg/set_diag)

tf.linalg.set_diag(
        input,
        diagonal,
        name='set_diag',
        k=0,
        align='RIGHT_LEFT'
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Multiple changepoint detection and Bayesian model selection](https://www.tensorflow.org/probability/examples/Multiple_changepoint_detection_and_Bayesian_model_selection) |

Given `input` and `diagonal`, this operation returns a tensor with the same shape and values as `input`, except for the specified diagonals of the innermost matrices. These will be overwritten by the values in `diagonal`.

`input` has `r+1` dimensions `[I, J, ..., L, M, N]`. When `k` is scalar or `k[0] == k[1]`, `diagonal` has `r` dimensions `[I, J, ..., L, max_diag_len]`. Otherwise, it has `r+1` dimensions `[I, J, ..., L, num_diags, max_diag_len]`. `num_diags` is the number of diagonals, `num_diags = k[1] - k[0] + 1`. `max_diag_len` is the longest diagonal in the range `[k[0], k[1]]`, `max_diag_len = min(M + min(k[1], 0), N + min(-k[0], 0))`

The output is a tensor of rank `k+1` with dimensions `[I, J, ..., L, M, N]`. If `k` is scalar or `k[0] == k[1]`:

output[i, j, ..., l, m, n]
      = diagonal[i, j, ..., l, n-max(k[1], 0)] ; if n - m == k[1]
        input[i, j, ..., l, m, n]              ; otherwise

Otherwise,

output[i, j, ..., l, m, n]
      = diagonal[i, j, ..., l, diag_index, index_in_diag] ; if k[0] <= d <= k[1]
        input[i, j, ..., l, m, n]                         ; otherwise

where `d = n - m`, `diag_index = k[1] - d`, and `index_in_diag = n - max(d, 0) + offset`.

`offset` is zero except when the alignment of the diagonal is to the right.

offset = max_diag_len - diag_len(d) ; if (`align` in {RIGHT_LEFT, RIGHT_RIGHT}
                                               and `d >= 0`) or
                                             (`align` in {LEFT_RIGHT, RIGHT_RIGHT}
                                               and `d <= 0`)
             0                          ; otherwise

where `diag_len(d) = min(cols - max(d, 0), rows + min(d, 0))`.

#### For example:

# The main diagonal.
    input = np.array([[[7, 7, 7, 7],              # Input shape: (2, 3, 4)\
                       [7, 7, 7, 7],\
                       [7, 7, 7, 7]],\
                      [[7, 7, 7, 7],\
                       [7, 7, 7, 7],\
                       [7, 7, 7, 7]]])
    diagonal = np.array([[1, 2, 3],               # Diagonal shape: (2, 3)\
                         [4, 5, 6]])
    tf.matrix_set_diag(input, diagonal)
      ==> [[[1, 7, 7, 7],  # Output shape: (2, 3, 4)\
            [7, 2, 7, 7],\
            [7, 7, 3, 7]],\
           [[4, 7, 7, 7],\
            [7, 5, 7, 7],\
            [7, 7, 6, 7]]]
    
    # A superdiagonal (per batch).
    tf.matrix_set_diag(input, diagonal, k = 1)
      ==> [[[7, 1, 7, 7],  # Output shape: (2, 3, 4)\
            [7, 7, 2, 7],\
            [7, 7, 7, 3]],\
           [[7, 4, 7, 7],\
            [7, 7, 5, 7],\
            [7, 7, 7, 6]]]
    
    # A band of diagonals.
    diagonals = np.array([[[9, 1, 0],  # Diagonal shape: (2, 4, 3)\
                           [6, 5, 8],\
                           [1, 2, 3],\
                           [0, 4, 5]],\
                          [[1, 2, 0],\
                           [5, 6, 4],\
                           [6, 1, 2],\
                           [0, 3, 4]]])
    tf.matrix_set_diag(input, diagonals, k = (-1, 2))
      ==> [[[1, 6, 9, 7],  # Output shape: (2, 3, 4)\
            [4, 2, 5, 1],\
            [7, 5, 3, 8]],\
           [[6, 5, 1, 7],\
            [3, 1, 6, 2],\
            [7, 4, 2, 4]]]
    
    # RIGHT_LEFT alignment.
    diagonals = np.array([[[0, 9, 1],  # Diagonal shape: (2, 4, 3)\
                           [6, 5, 8],\
                           [1, 2, 3],\
                           [4, 5, 0]],\
                          [[0, 1, 2],\
                           [5, 6, 4],\
                           [6, 1, 2],\
                           [3, 4, 0]]])
    tf.matrix_set_diag(input, diagonals, k = (-1, 2), align="RIGHT_LEFT")
      ==> [[[1, 6, 9, 7],  # Output shape: (2, 3, 4)\
            [4, 2, 5, 1],\
            [7, 5, 3, 8]],\
           [[6, 5, 1, 7],\
            [3, 1, 6, 2],\
            [7, 4, 2, 4]]]

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A `Tensor` with rank `k + 1`, where `k >= 1`. |
| `diagonal` | A `Tensor` with rank `k`, when `d_lower == d_upper`, or `k + 1`, otherwise. `k >= 1`. |
| `name` | A name for the operation (optional). |
| `k` | Diagonal offset(s). Positive value means superdiagonal, 0 refers to the main diagonal, and negative value means subdiagonals. `k` can be a single integer (for a single diagonal) or a pair of integers specifying the low and high ends of a matrix band. `k[0]` must not be larger than `k[1]`. |
| `align` | Some diagonals are shorter than `max_diag_len` and need to be padded. `align` is a string specifying how superdiagonals and subdiagonals should be aligned, respectively. There are four possible alignments: "RIGHT\_LEFT" (default), "LEFT\_RIGHT", "LEFT\_LEFT", and "RIGHT\_RIGHT". "RIGHT\_LEFT" aligns superdiagonals to the right (left-pads the row) and subdiagonals to the left (right-pads the row). It is the packing format LAPACK uses. cuSPARSE uses "LEFT\_RIGHT", which is the opposite alignment. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.