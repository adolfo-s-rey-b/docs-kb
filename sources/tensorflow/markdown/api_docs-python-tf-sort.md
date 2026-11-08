[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/sort#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/sort)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/sort?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/sort#used-in-the-notebooks)
    
*   [See also](https://www.tensorflow.org/api_docs/python/tf/sort#see-also)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/sort#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/sort#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/sort#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.sort Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/sort#used-in-the-notebooks)
    
*   [See also](https://www.tensorflow.org/api_docs/python/tf/sort#see-also)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/sort#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/sort#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/sort#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/sort_ops.py#L29-L83)

Sorts a tensor.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.sort`](https://www.tensorflow.org/api_docs/python/tf/sort)

tf.sort(
        values, axis=-1, direction='ASCENDING', name=None
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [TFP Release Notes notebook (0.11.0)](https://www.tensorflow.org/probability/examples/TFP_Release_Notebook_0_11_0) |

#### Usage:

    a = [1, 10, 26.9, 2.8, 166.32, 62.3]

    tf.sort(a, direction='DESCENDING').numpy()

For multidimensional inputs you can control which axis the sort is applied along. The default `axis=-1` sorts the innermost axis.

    mat = [[3,2,1],\
\
|     |\
| --- |\
| See also<br>-------- |     |\
| *   [`tf.argsort`](https://www.tensorflow.org/api_docs/python/tf/argsort)<br>    : Like sort, but it returns the sort indices.<br>*   [`tf.math.top_k`](https://www.tensorflow.org/api_docs/python/tf/math/top_k)<br>    : A partial sort that returns a fixed number of top values and corresponding indices. |     |\
\
|     |     |\
| --- | --- |\
| Args<br>---- |     |\
| `values` | 1-D or higher **numeric** `Tensor`. |\
| `axis` | The axis along which to sort. The default is -1, which sorts the last axis. |\
| `direction` | The direction in which to sort the values (`'ASCENDING'` or `'DESCENDING'`). |\
| `name` | Optional name for the operation. |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| A `Tensor` with the same dtype and shape as `values`, with the elements sorted along the given `axis`. |     |\
\
|     |     |\
| --- | --- |\
| Raises<br>------ |     |\
| [`tf.errors.InvalidArgumentError`](https://www.tensorflow.org/api_docs/python/tf/errors/InvalidArgumentError) | If the `values.dtype` is not a `float` or `int` type. |\
| `ValueError` | If axis is not a constant scalar, or the direction is invalid. |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.