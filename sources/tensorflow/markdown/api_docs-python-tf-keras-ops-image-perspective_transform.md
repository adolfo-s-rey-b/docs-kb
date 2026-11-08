[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/perspective_transform#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/perspective_transform)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/perspective_transform?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/perspective_transform#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/perspective_transform#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.image.perspective\_transform Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/perspective_transform#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/perspective_transform#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/image.py#L1686-L1778)

Applies a perspective transformation to the image(s).

tf.keras.ops.image.perspective_transform(
        images,
        start_points,
        end_points,
        interpolation='bilinear',
        fill_value=0,
        data_format=None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `images` | Input image or batch of images. Must be 3D or 4D. |
| `start_points` | A tensor of shape `(N, 4, 2)` or `(4, 2)`, representing the source points in the original image that define the transformation. |
| `end_points` | A tensor of shape `(N, 4, 2)` or `(4, 2)`, representing the target points in the output image after transformation. |
| `interpolation` | Interpolation method. Available methods are `"nearest"`, and `"bilinear"`. Defaults to `"bilinear"`. |
| `fill_value` | Value used for points outside the boundaries of the input if extrapolation is needed. Defaults to `0`. |
| `data_format` | A string specifying the data format of the input tensor. It can be either `"channels_last"` or `"channels_first"`. `"channels_last"` corresponds to inputs with shape `(batch, height, width, channels)`, while `"channels_first"` corresponds to inputs with shape `(batch, channels, height, width)`. If not specified, the value will default to [`keras.config.image_data_format`](https://www.tensorflow.org/api_docs/python/tf/keras/backend/image_data_format)<br>. |

|     |
| --- |
| Returns<br>------- |     |
| Applied perspective transform image or batch of images. |     |

#### Examples:

    x = np.random.random((2, 64, 80, 3))  # batch of 2 RGB images

    x = np.random.random((64, 80, 3))  # single RGB image

    x = np.random.random((2, 3, 64, 80))  # batch of 2 RGB images

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.