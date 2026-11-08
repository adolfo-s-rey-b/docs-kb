[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/abs_max_quantize#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/abs_max_quantize)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/abs_max_quantize?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Fquantizers%2Fabs_max_quantize&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/abs_max_quantize#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/abs_max_quantize#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.quantizers.abs\_max\_quantize Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/abs_max_quantize#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/quantizers/abs_max_quantize#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/quantizers/quantizers.py#L69-L120)

Quantizes the input tensor using the absolute maximum quantization scheme.

tf.keras.quantizers.abs_max_quantize(
        inputs,
        axis,
        value_range=(-127, 127),
        dtype='int8',
        epsilon=backend.epsilon(),
        to_numpy=False
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `inputs` | Input tensor to quantize. |
| `axis` | Axis along which to compute the quantization range. |
| `value_range` | Tuple of the minimum and maximum values of the quantization range. |
| `dtype` | Data type of the quantized output. |
| `epsilon` | Small value to avoid division by zero. |
| `to_numpy` | Whether to perform the quantization in numpy. This performs the computation on the host CPU and can be useful for saving memory on the device. If False, the computation is performed on the device. |

|     |
| --- |
| Returns<br>------- |     |
| A tuple of the quantized tensor and the scale. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.