[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/argmax#main-content)

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
    

tf.compat.v1.argmax Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L251-L268)

Returns the index with the largest value across axes of a tensor. (deprecated arguments)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.math.argmax`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/argmax)

tf.compat.v1.argmax(
        input,
        axis=None,
        name=None,
        dimension=None,
        output_type=tf.dtypes.int64
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Fitting Dirichlet Process Mixture Model Using Preconditioned Stochastic Gradient Langevin Dynamics](https://www.tensorflow.org/probability/examples/Fitting_DPMM_Using_pSGLD)<br>    <br>*   [Exploring the TF-Hub CORD-19 Swivel Embeddings](https://www.tensorflow.org/hub/tutorials/cord_19_embeddings) |

Note that in case of ties the identity of the return value is not guaranteed.

|     |
| --- |
| Usage<br>----- |     |
| import tensorflow as tf<br>    a = [1, 10, 26.9, 2.8, 166.32, 62.3]<br>    b = tf.math.argmax(input = a)<br>    c = tf.keras.backend.eval(b)<br>    # c = 4<br>    # here a[4] = 166.32 which is the largest element of a across axis 0 |     |

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`, `qint8`, `quint8`, `qint32`, `qint16`, `quint16`, `bool`. |
| `axis` | A `Tensor`. Must be one of the following types: `int16`, `int32`, `int64`. int16, int32 or int64, must be in the range `[-rank(input), rank(input))`. Describes which axis of the input Tensor to reduce across. For vectors, use axis = 0. |\
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
Last updated 2026-11-06 UTC.