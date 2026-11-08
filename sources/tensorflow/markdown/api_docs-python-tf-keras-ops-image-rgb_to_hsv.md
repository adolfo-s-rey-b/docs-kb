[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/rgb_to_hsv#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/rgb_to_hsv)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/rgb_to_hsv?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/rgb_to_hsv#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/rgb_to_hsv#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.image.rgb\_to\_hsv Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/rgb_to_hsv#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/rgb_to_hsv#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/image.py#L115-L159)

Convert RGB images to HSV.

tf.keras.ops.image.rgb_to_hsv(
        images, data_format=None
    )

`images` must be of float dtype, and the output is only well defined if the values in `images` are in `[0, 1]`.

All HSV values are in `[0, 1]`. A hue of `0` corresponds to pure red, `1/3` is pure green, and `2/3` is pure blue.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `images` | Input image or batch of images. Must be 3D or 4D. |
| `data_format` | A string specifying the data format of the input tensor. It can be either `"channels_last"` or `"channels_first"`. `"channels_last"` corresponds to inputs with shape `(batch, height, width, channels)`, while `"channels_first"` corresponds to inputs with shape `(batch, channels, height, width)`. If not specified, the value will default to [`keras.config.image_data_format`](https://www.tensorflow.org/api_docs/python/tf/keras/backend/image_data_format)<br>. |

|     |
| --- |
| Returns<br>------- |     |
| HSV image or batch of HSV images. |     |

#### Examples:

    import numpy as np

    x = np.random.random((4, 4, 3)) # Single RGB image

    x = np.random.random((2, 3, 4, 4))

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.