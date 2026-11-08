[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/sparse/add#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/sparse/add)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/sparse/add?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fsparse%2Fadd&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/sparse/add#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/sparse/add#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/sparse/add#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/sparse/add#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.sparse.add Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/sparse/add#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/sparse/add#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/sparse/add#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/sparse/add#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/sparse_ops.py#L524-L605)

Adds two tensors, at least one of each is a `SparseTensor`.

tf.sparse.add(
        a, b, threshold=0
    )

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Working with sparse tensors](https://www.tensorflow.org/guide/sparse_tensor) |

If one `SparseTensor` and one `Tensor` are passed in, returns a `Tensor`. If both arguments are `SparseTensor`s, this returns a `SparseTensor`. The order of arguments does not matter. Use vanilla [`tf.add()`](https://www.tensorflow.org/api_docs/python/tf/math/add)
 for adding two dense `Tensor`s.

The shapes of the two operands must match: broadcasting is not supported.

The indices of any input `SparseTensor` are assumed ordered in standard lexicographic order. If this is not the case, before this step run `SparseReorder` to restore index ordering.

If both arguments are sparse, we perform "clipping" as follows. By default, if two values sum to zero at some index, the output `SparseTensor` would still include that particular location in its index, storing a zero in the corresponding value slot. To override this, callers can specify `threshold`, indicating that if the sum has a magnitude strictly smaller than `threshold`, its corresponding value and index would then not be included. In particular, `threshold == 0.0` (default) means everything is kept and actual thresholding happens only for a positive value.

For example, suppose the logical sum of two sparse operands is (densified):

[       2]
    [.1     0]
    [ 6   -.2]

Then,

*   `threshold == 0` (the default): all 5 index/value pairs will be returned.
*   `threshold == 0.11`: only .1 and 0 will vanish, and the remaining three index/value pairs will be returned.
*   `threshold == 0.21`: .1, 0, and -.2 will vanish.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `a` | The first operand; `SparseTensor` or `Tensor`. |
| `b` | The second operand; `SparseTensor` or `Tensor`. At least one operand must be sparse. |
| `threshold` | A 0-D `Tensor`. The magnitude threshold that determines if an output value/index pair takes space. Its dtype should match that of the values if they are real; if the latter are complex64/complex128, then the dtype should be float32/float64, correspondingly. |

|     |
| --- |
| Returns<br>------- |     |
| A `SparseTensor` or a `Tensor`, representing the sum. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | If both `a` and `b` are `Tensor`s. Use [`tf.add()`](https://www.tensorflow.org/api_docs/python/tf/math/add)<br> instead. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.