[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/sparse/concat#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/sparse/concat)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/sparse/concat?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fsparse%2Fconcat&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/sparse/concat#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/sparse/concat#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/sparse/concat#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/sparse/concat#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

Was this helpful?

tf.sparse.concat Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/sparse/concat#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/sparse/concat#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/sparse/concat#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/sparse/concat#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/sparse_ops.py#L400-L451)

Concatenates a list of `SparseTensor` along the specified dimension. (deprecated arguments)

tf.sparse.concat(
        axis, sp_inputs, expand_nonconcat_dims=False, name=None
    )

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Ragged tensors](https://www.tensorflow.org/guide/ragged_tensor)<br>    <br>*   [Working with sparse tensors](https://www.tensorflow.org/guide/sparse_tensor) |

Concatenation is with respect to the dense versions of each sparse input. It is assumed that each inputs is a `SparseTensor` whose elements are ordered along increasing dimension number.

If expand\_nonconcat\_dim is False, all inputs' shapes must match, except for the concat dimension. If expand\_nonconcat\_dim is True, then inputs' shapes are allowed to vary among all inputs.

The `indices`, `values`, and `shapes` lists must have the same length.

If expand\_nonconcat\_dim is False, then the output shape is identical to the inputs', except along the concat dimension, where it is the sum of the inputs' sizes along that dimension.

If expand\_nonconcat\_dim is True, then the output shape along the non-concat dimensions will be expand to be the largest among all inputs, and it is the sum of the inputs sizes along the concat dimension.

The output elements will be resorted to preserve the sort order along increasing dimension number.

This op runs in `O(M log M)` time, where `M` is the total number of non-empty values across all inputs. This is due to the need for an internal sort in order to concatenate efficiently across an arbitrary dimension.

For example, if `axis = 1` and the inputs are

sp_inputs[0]: shape = [2, 3]
    [0, 2]: "a"
    [1, 0]: "b"
    [1, 1]: "c"
    
    sp_inputs[1]: shape = [2, 4]
    [0, 1]: "d"
    [0, 2]: "e"

then the output will be

shape = [2, 7]
    [0, 2]: "a"
    [0, 4]: "d"
    [0, 5]: "e"
    [1, 0]: "b"
    [1, 1]: "c"

Graphically this is equivalent to doing

[    a] concat [  d e  ] = [    a   d e  ]
    [b c  ]        [       ]   [b c          ]

Another example, if 'axis = 1' and the inputs are

sp_inputs[0]: shape = [3, 3]
    [0, 2]: "a"
    [1, 0]: "b"
    [2, 1]: "c"
    
    sp_inputs[1]: shape = [2, 4]
    [0, 1]: "d"
    [0, 2]: "e"

if expand\_nonconcat\_dim = False, this will result in an error. But if expand\_nonconcat\_dim = True, this will result in:

shape = [3, 7]
    [0, 2]: "a"
    [0, 4]: "d"
    [0, 5]: "e"
    [1, 0]: "b"
    [2, 1]: "c"

Graphically this is equivalent to doing

[    a] concat [  d e  ] = [    a   d e  ]
    [b    ]        [       ]   [b            ]
    [  c  ]                    [  c          ]

|     |     |
| --- | --- |
| Args<br>---- |     |
| `axis` | Dimension to concatenate along. Must be in range \[-rank, rank), where rank is the number of dimensions in each input `SparseTensor`. |\
| `sp_inputs` | List of `SparseTensor` to concatenate. |\
| `name` | A name prefix for the returned tensors (optional). |\
| `expand_nonconcat_dim` | Whether to allow the expansion in the non-concat dimensions. Defaulted to False. |\
| `concat_dim` | The old (deprecated) name for axis. |\
| `expand_nonconcat_dims` | alias for expand\_nonconcat\_dim |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| A `SparseTensor` with the concatenated output. |     |\
\
|     |     |\
| --- | --- |\
| Raises<br>------ |     |\
| `TypeError` | If `sp_inputs` is not a list of `SparseTensor`. |\
\
Was this helpful?\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.