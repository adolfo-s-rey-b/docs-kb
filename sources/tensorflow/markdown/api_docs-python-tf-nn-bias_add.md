[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/nn/bias_add#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/nn/bias_add)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/nn/bias_add?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fnn%2Fbias_add&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/nn/bias_add#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/bias_add#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/bias_add#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/nn/bias_add#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.nn.bias\_add Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/nn/bias_add#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/bias_add#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/bias_add#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/nn/bias_add#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/nn_ops.py#L3516-L3560)

Adds `bias` to `value`.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.nn.bias_add`](https://www.tensorflow.org/api_docs/python/tf/nn/bias_add)

tf.nn.bias_add(
        value, bias, data_format=None, name=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Use TF1.x models in TF2 workflows](https://www.tensorflow.org/guide/migrate/model_mapping) | *   [Scalable model compression](https://www.tensorflow.org/tutorials/optimization/compression) |

This is (mostly) a special case of [`tf.add`](https://www.tensorflow.org/api_docs/python/tf/math/add)
 where `bias` is restricted to 1-D. Broadcasting is supported, so `value` may have any number of dimensions. Unlike [`tf.add`](https://www.tensorflow.org/api_docs/python/tf/math/add)
, the type of `bias` is allowed to differ from `value` in the case where both types are quantized.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `value` | A `Tensor` with type `float`, `double`, `int64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, or `complex128`. |
| `bias` | A 1-D `Tensor` with size matching the channel dimension of `value`. Must be the same type as `value` unless `value` is a quantized type, in which case a different quantized type may be used. |
| `data_format` | A string. 'N...C' and 'NC...' are supported. If `None` (the default) is specified then 'N..C' is assumed. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` with the same type as `value`. |     |

|     |
| --- |
| Raises<br>------ |     |
| ValueError if data format is unrecognized, if `value` has less than two dimensions when `data_format` is 'N..C'/`None` or `value` has less then three dimensions when `data_format` is `NC..`, if `bias` does not have exactly one dimension (is a vector), or if the size of `bias` does not match the size of the channel dimension of `value`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.