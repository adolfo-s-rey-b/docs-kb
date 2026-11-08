[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/saturate_cast#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/saturate_cast)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/saturate_cast?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/saturate_cast#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/saturate_cast#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.saturate\_cast Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/saturate_cast#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/saturate_cast#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/core.py#L897-L947)

Performs a safe saturating cast to the desired dtype.

tf.keras.ops.saturate_cast(
        x, dtype
    )

Saturating cast prevents data type overflow when casting to `dtype` with smaller values range. E.g. `ops.cast(ops.cast([-1, 256], "float32"), "uint8")` returns `[255, 0]`, but `ops.saturate_cast(ops.cast([-1, 256], "float32"), "uint8")` returns `[0, 255]`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | A tensor or variable. |
| `dtype` | The target type. |

|     |
| --- |
| Returns<br>------- |     |
| A safely casted tensor of the specified `dtype`. |     |

#### Example:

Image resizing with bicubic interpolation may produce values outside original range.

>>> image2x2 = np.array([0, 1, 254, 255], dtype="uint8").reshape(1, 2, 2, 1)
    >>> image4x4 = tf.image.resize(image2x2, (4, 4), method="bicubic")
    >>> print(image4x4.numpy().squeeze())
    >>> # [[-22.500004 -22.204624 -21.618908 -21.32353 ]\
    >>> #  [ 52.526054  52.82143   53.407146  53.70253 ]\
    >>> #  [201.29752  201.59288  202.17859  202.47395 ]\
    >>> #  [276.32355  276.61893  277.20465  277.50006 ]]

Casting this resized image back to `uint8` will cause overflow.

>>> image4x4_casted = ops.cast(image4x4, "uint8")
    >>> print(image4x4_casted.numpy().squeeze())
    >>> # [[234 234 235 235]\
    >>> #  [ 52  52  53  53]\
    >>> #  [201 201 202 202]\
    >>> #  [ 20  20  21  21]]

Saturate casting to `uint8` will clip values to `uint8` range before casting and will not cause overflow.

>>> image4x4_saturate_casted = ops.saturate_cast(image4x4, "uint8")
    >>> print(image4x4_saturate_casted.numpy().squeeze())
    >>> # [[  0   0   0   0]\
    >>> #  [ 52  52  53  53]\
    >>> #  [201 201 202 202]\
    >>> #  [255 255 255 255]]

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.