[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/searchsorted#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/searchsorted)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/searchsorted?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fsearchsorted&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/searchsorted#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/searchsorted#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/searchsorted#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.searchsorted Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/searchsorted#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/searchsorted#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/searchsorted#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/array_ops.py#L6111-L6191)

Searches for where a value would go in a sorted sequence.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.searchsorted`](https://www.tensorflow.org/api_docs/python/tf/searchsorted)

tf.searchsorted(
        sorted_sequence,
        values,
        side='left',
        out_type=tf.dtypes.int32,
        name=None
    )

This is not a method for checking containment (like python `in`).

The typical use case for this operation is "binning", "bucketing", or "discretizing". The `values` are assigned to bucket-indices based on the **edges** listed in `sorted_sequence`. This operation returns the bucket-index for each value.

    edges = [-1, 3.3, 9.1, 10.0]

The `side` argument controls which index is returned if a value lands exactly on an edge:

    seq = [0, 3, 9, 10, 10]

The `axis` is not settable for this operation. It always operates on the innermost dimension (`axis=-1`). The operation will accept any number of outer dimensions. Here it is applied to the rows of a matrix:

    sorted_sequence = [[0., 3., 8., 9., 10.],\
\
|     |     |\
| --- | --- |\
| Args<br>---- |     |\
| `sorted_sequence` | N-D `Tensor` containing a sorted sequence. |\
| `values` | N-D `Tensor` containing the search values. |\
| `side` | 'left' or 'right'; 'left' corresponds to lower\_bound and 'right' to upper\_bound. |\
| `out_type` | The output type (`int32` or `int64`). Default is [`tf.int32`](https://www.tensorflow.org/api_docs/python/tf#int32)<br>. |\
| `name` | Optional name for the operation. |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| An N-D `Tensor` the size of `values` containing the result of applying either lower\_bound or upper\_bound (depending on side) to each value. The result is not a global index to the entire `Tensor`, but the index in the last dimension. |     |\
\
|     |     |\
| --- | --- |\
| Raises<br>------ |     |\
| `ValueError` | If the last dimension of `sorted_sequence >= 2^31-1` elements. If the total size of `values` exceeds `2^31 - 1` elements. If the first `N-1` dimensions of the two tensors don't match. |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.