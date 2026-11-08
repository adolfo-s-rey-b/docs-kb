[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/sparse/split#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   English
*   中文 – 简体

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.sparse.split Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/sparse_ops.py#L1067-L1133)

Split a `SparseTensor` into `num_split` tensors along `axis`.

tf.sparse.split(
        sp_input=None, num_split=None, axis=None, name=None
    )

If the `sp_input.dense_shape[axis]` is not an integer multiple of `num_split` each slice starting from 0:`shape[axis] % num_split` gets extra one dimension. For example:

    indices = [[0, 2], [0, 4], [0, 5], [1, 0], [1, 1]]

    output = tf.sparse.split(sp_input=t, num_split=2, axis=1)

    output = tf.sparse.split(sp_input=t, num_split=2, axis=0)

    output = tf.sparse.split(sp_input=t, num_split=2, axis=-1)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `sp_input` | The `SparseTensor` to split. |
| `num_split` | A Python integer. The number of ways to split. |
| `axis` | A 0-D `int32` `Tensor`. The dimension along which to split. Must be in range \[-rank, rank), where rank is the number of dimensions in the input `SparseTensor`. |\
| `name` | A name for the operation (optional). |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| `num_split` `SparseTensor` objects resulting from splitting `value`. |     |\
\
|     |     |\
| --- | --- |\
| Raises<br>------ |     |\
| `TypeError` | If `sp_input` is not a `SparseTensor`. |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.