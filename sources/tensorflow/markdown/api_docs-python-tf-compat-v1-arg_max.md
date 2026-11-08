[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/arg_max#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/arg_max)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/arg_max?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Farg_max&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Usage](https://www.tensorflow.org/api_docs/python/tf/compat/v1/arg_max#usage)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/arg_max#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/arg_max#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.arg\_max Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================

*   On this page
*   [Usage](https://www.tensorflow.org/api_docs/python/tf/compat/v1/arg_max#usage)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/arg_max#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/arg_max#returns)
    

Returns the index with the largest value across dimensions of a tensor. (deprecated)

tf.compat.v1.arg_max(
        input: Annotated[Any, tf.raw_ops.Any],
        dimension: Annotated[Any, tf.raw_ops.Any],
        output_type: TV_ArgMax_output_type = tf.dtypes.int64,
        name=None
    ) -> Annotated[Any, tf.raw_ops.Any]

Note that in case of ties the identity of the return value is not guaranteed.

|     |
| --- |
| Usage<br>----- |     |
| import tensorflow as tf<br>    a = [1, 10, 26.9, 2.8, 166.32, 62.3]<br>    b = tf.math.argmax(input = a)<br>    c = tf.keras.backend.eval(b)<br>    # c = 4<br>    # here a[4] = 166.32 which is the largest element of a across axis 0 |     |

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`, `qint8`, `quint8`, `qint32`, `qint16`, `quint16`, `bool`. |
| `dimension` | A `Tensor`. Must be one of the following types: `int16`, `int32`, `int64`. int16, int32 or int64, must be in the range `[-rank(input), rank(input))`. Describes which dimension of the input Tensor to reduce across. For vectors, use dimension = 0. |\
| `output_type` | An optional [`tf.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br> from: `tf.int16, tf.uint16, tf.int32, tf.int64`. Defaults to [`tf.int64`](https://www.tensorflow.org/api_docs/python/tf#int64)<br>. |\
| `name` | A name for the operation (optional). |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| A `Tensor` of type `output_type`. |     |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2024-04-26 UTC.