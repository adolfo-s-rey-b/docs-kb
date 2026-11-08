[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/quantized_relu_x#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/quantized_relu_x)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/quantized_relu_x?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/quantized_relu_x#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/quantized_relu_x#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.nn.quantized\_relu\_x Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/quantized_relu_x#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/nn/quantized_relu_x#returns)
    

Computes Quantized Rectified Linear X: `min(max(features, 0), max_value)`

tf.compat.v1.nn.quantized_relu_x(
        features: Annotated[Any, TV_QuantizedReluX_Tinput],
        max_value: Annotated[Any, _atypes.Float32],
        min_features: Annotated[Any, _atypes.Float32],
        max_features: Annotated[Any, _atypes.Float32],
        out_type: TV_QuantizedReluX_out_type = tf.dtypes.quint8,
        name=None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `features` | A `Tensor`. Must be one of the following types: `qint8`, `quint8`, `qint32`, `qint16`, `quint16`. |
| `max_value` | A `Tensor` of type `float32`. |
| `min_features` | A `Tensor` of type `float32`. The float value that the lowest quantized value represents. |
| `max_features` | A `Tensor` of type `float32`. The float value that the highest quantized value represents. |
| `out_type` | An optional [`tf.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br> from: `tf.qint8, tf.quint8, tf.qint32, tf.qint16, tf.quint16`. Defaults to [`tf.quint8`](https://www.tensorflow.org/api_docs/python/tf#quint8)<br>. |
| `name` | A name for the operation (optional). |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| A tuple of `Tensor` objects (activations, min\_activations, max\_activations). |     |
| `activations` | A `Tensor` of type `out_type`. |
| `min_activations` | A `Tensor` of type `float32`. |
| `max_activations` | A `Tensor` of type `float32`. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.