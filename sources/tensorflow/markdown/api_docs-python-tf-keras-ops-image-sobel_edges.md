[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/sobel_edges#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/sobel_edges)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/sobel_edges?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/sobel_edges#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/sobel_edges#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.image.sobel\_edges Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/sobel_edges#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/sobel_edges#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/image.py#L2128-L2168)

Computes Sobel edge detection on images.

tf.keras.ops.image.sobel_edges(
        images, data_format=None
    )

The Sobel operator computes the gradient of the image intensity at each pixel, giving the direction of the largest increase from light to dark and the rate of change in that direction.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `images` | Input tensor of shape `(batch, height, width, channels)` if `data_format="channels_last"`, or `(batch, channels, height, width)` if `data_format="channels_first"`. |
| `data_format` | A string specifying the data format of the input tensor. It can be either `"channels_last"` or `"channels_first"`. If not specified, the value will default to [`keras.config.image_data_format`](https://www.tensorflow.org/api_docs/python/tf/keras/backend/image_data_format)<br>. |

|     |
| --- |
| Returns<br>------- |     |
| A tensor containing the Sobel edges. For `data_format="channels_last"`, the output shape is `(batch, height, width, channels, 2)` where the last dimension contains `[dy, dx]` representing the vertical and horizontal gradients. For `data_format="channels_first"`, the output shape is `(batch, channels, height, width, 2)`. |     |

#### Example:

    import numpy as np

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.