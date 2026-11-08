[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/ragged/cross#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/ragged/cross)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/ragged/cross?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/ragged/cross#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/ragged/cross#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.ragged.cross Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/ragged/cross#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/ragged/cross#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/ragged_array_ops.py#L741-L765)

Generates feature cross from a list of tensors.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.ragged.cross`](https://www.tensorflow.org/api_docs/python/tf/ragged/cross)

tf.ragged.cross(
        inputs, name=None
    )

The input tensors must have `rank=2`, and must all have the same number of rows. The result is a `RaggedTensor` with the same number of rows as the inputs, where `result[row]` contains a list of all combinations of values formed by taking a single value from each input's corresponding row (`inputs[i][row]`). Values are combined by joining their strings with '_X_'. E.g.:

    tf.ragged.cross([tf.ragged.constant([['a'], ['b', 'c']]),\
\
|     |     |\
| --- | --- |\
| Args<br>---- |     |\
| `inputs` | A list of `RaggedTensor` or `Tensor` or `SparseTensor`. |\
| `name` | Optional name for the op. |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| A 2D `RaggedTensor` of type `string`. |     |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.