[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/sparse/slice#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/sparse/slice)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/sparse/slice?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/sparse/slice#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/sparse/slice#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/sparse/slice#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/sparse/slice#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.sparse.slice Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/sparse/slice#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/sparse/slice#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/sparse/slice#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/sparse/slice#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/sparse_ops.py#L1136-L1183)

Slice a `SparseTensor` based on the `start` and `size`.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.sparse.slice`](https://www.tensorflow.org/api_docs/python/tf/sparse/slice)
, [`tf.compat.v1.sparse_slice`](https://www.tensorflow.org/api_docs/python/tf/sparse/slice)

tf.sparse.slice(
        sp_input, start, size, name=None
    )

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Working with sparse tensors](https://www.tensorflow.org/guide/sparse_tensor) |

For example, if the input is

input_tensor = shape = [2, 7]
    [    a   d e  ]
    [b c          ]

Graphically the output tensors are:

sparse.slice([0, 0], [2, 4]) = shape = [2, 4]
    [    a  ]
    [b c    ]
    
    sparse.slice([0, 4], [2, 3]) = shape = [2, 3]
    [ d e  ]
    [      ]

|     |     |
| --- | --- |
| Args<br>---- |     |
| `sp_input` | The `SparseTensor` to split. |
| `start` | 1-D. tensor represents the start of the slice. |
| `size` | 1-D. tensor represents the size of the slice. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `SparseTensor` objects resulting from splicing. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | If `sp_input` is not a `SparseTensor`. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.