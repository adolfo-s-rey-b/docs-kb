[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/resize#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/resize)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/resize?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Fops%2Fimage%2Fresize&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/resize#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/resize#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.image.resize Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/resize#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/resize#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/image.py#L292-L399)

Resize images to size using the specified interpolation method.

tf.keras.ops.image.resize(
        images,
        size,
        interpolation='bilinear',
        antialias=False,
        crop_to_aspect_ratio=False,
        pad_to_aspect_ratio=False,
        fill_mode='constant',
        fill_value=0.0,
        data_format=None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `images` | Input image or batch of images. Must be 3D or 4D. |
| `size` | Size of output image in `(height, width)` format. |
| `interpolation` | Interpolation method. Available methods are `"nearest"`, `"bilinear"`, and `"bicubic"`. Defaults to `"bilinear"`. |
| `antialias` | Whether to use an antialiasing filter when downsampling an image. Defaults to `False`. |
| `crop_to_aspect_ratio` | If `True`, resize the images without aspect ratio distortion. When the original aspect ratio differs from the target aspect ratio, the output image will be cropped so as to return the largest possible window in the image (of size `(height, width)`) that matches the target aspect ratio. By default (`crop_to_aspect_ratio=False`), aspect ratio may not be preserved. |
| `pad_to_aspect_ratio` | If `True`, pad the images without aspect ratio distortion. When the original aspect ratio differs from the target aspect ratio, the output image will be evenly padded on the short side. |
| `fill_mode` | When using `pad_to_aspect_ratio=True`, padded areas are filled according to the given mode. Only `"constant"` is supported at this time (fill with constant value, equal to `fill_value`). |
| `fill_value` | Float. Padding value to use when `pad_to_aspect_ratio=True`. |
| `data_format` | A string specifying the data format of the input tensor. It can be either `"channels_last"` or `"channels_first"`. `"channels_last"` corresponds to inputs with shape `(batch, height, width, channels)`, while `"channels_first"` corresponds to inputs with shape `(batch, channels, height, width)`. If not specified, the value will default to [`keras.config.image_data_format`](https://www.tensorflow.org/api_docs/python/tf/keras/backend/image_data_format)<br>. |

|     |
| --- |
| Returns<br>------- |     |
| Resized image or batch of images. |     |

#### Examples:

    x = np.random.random((2, 4, 4, 3)) # batch of 2 RGB images

    x = np.random.random((4, 4, 3)) # single RGB image

    x = np.random.random((2, 3, 4, 4)) # batch of 2 RGB images

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.