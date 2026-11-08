[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/debugging/is_numeric_tensor#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/debugging/is_numeric_tensor)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/debugging/is_numeric_tensor?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fdebugging%2Fis_numeric_tensor&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.debugging.is\_numeric\_tensor Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/check_ops.py#L1961-L1993)

Returns `True` if the elements of `tensor` are numbers.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.debugging.is_numeric_tensor`](https://www.tensorflow.org/api_docs/python/tf/debugging/is_numeric_tensor)
, [`tf.compat.v1.is_numeric_tensor`](https://www.tensorflow.org/api_docs/python/tf/debugging/is_numeric_tensor)

tf.debugging.is_numeric_tensor(
        tensor
    )

Specifically, returns `True` if the dtype of `tensor` is one of the following:

*   [`tf.float16`](https://www.tensorflow.org/api_docs/python/tf#float16)
    
*   [`tf.float32`](https://www.tensorflow.org/api_docs/python/tf#float32)
    
*   [`tf.float64`](https://www.tensorflow.org/api_docs/python/tf#float64)
    
*   [`tf.int8`](https://www.tensorflow.org/api_docs/python/tf#int8)
    
*   [`tf.int16`](https://www.tensorflow.org/api_docs/python/tf#int16)
    
*   [`tf.int32`](https://www.tensorflow.org/api_docs/python/tf#int32)
    
*   [`tf.int64`](https://www.tensorflow.org/api_docs/python/tf#int64)
    
*   [`tf.uint8`](https://www.tensorflow.org/api_docs/python/tf#uint8)
    
*   [`tf.uint16`](https://www.tensorflow.org/api_docs/python/tf#uint16)
    
*   [`tf.uint32`](https://www.tensorflow.org/api_docs/python/tf#uint32)
    
*   [`tf.uint64`](https://www.tensorflow.org/api_docs/python/tf#uint64)
    
*   [`tf.qint8`](https://www.tensorflow.org/api_docs/python/tf#qint8)
    
*   [`tf.qint16`](https://www.tensorflow.org/api_docs/python/tf#qint16)
    
*   [`tf.qint32`](https://www.tensorflow.org/api_docs/python/tf#qint32)
    
*   [`tf.quint8`](https://www.tensorflow.org/api_docs/python/tf#quint8)
    
*   [`tf.quint16`](https://www.tensorflow.org/api_docs/python/tf#quint16)
    
*   [`tf.complex64`](https://www.tensorflow.org/api_docs/python/tf#complex64)
    
*   [`tf.complex128`](https://www.tensorflow.org/api_docs/python/tf#complex128)
    
*   [`tf.bfloat16`](https://www.tensorflow.org/api_docs/python/tf#bfloat16)
    

Returns `False` if `tensor` is of a non-numeric type or if `tensor` is not a [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
 object.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.