[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/smart_resize#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/smart_resize)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/smart_resize?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/smart_resize#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/smart_resize#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.preprocessing.image.smart\_resize Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/smart_resize#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/smart_resize#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/utils/image_utils.py#L308-L472)

Resize images to a target size without aspect ratio distortion.

tf.keras.preprocessing.image.smart_resize(
        x,
        size,
        interpolation='bilinear',
        data_format='channels_last',
        **kwargs
    )

Image datasets typically yield images that have each a different size. However, these images need to be batched before they can be processed by Keras layers. To be batched, images need to share the same height and width.

You could simply do, in TF (or JAX equivalent):

size = (200, 200)
    ds = ds.map(lambda img: resize(img, size))

However, if you do this, you distort the aspect ratio of your images, since in general they do not all have the same aspect ratio as `size`. This is fine in many cases, but not always (e.g. for image generation models this can be a problem).

Note that passing the argument `preserve_aspect_ratio=True` to `resize` will preserve the aspect ratio, but at the cost of no longer respecting the provided target size.

#### This calls for:

size = (200, 200)
    ds = ds.map(lambda img: smart_resize(img, size))

Your output images will actually be `(200, 200)`, and will not be distorted. Instead, the parts of the image that do not fit within the target size get cropped out.

The resizing process is:

1.  Take the largest centered crop of the image that has the same aspect ratio as the target size. For instance, if `size=(200, 200)` and the input image has size `(340, 500)`, we take a crop of `(340, 340)` centered along the width.
2.  Resize the cropped image to the target size. In the example above, we resize the `(340, 340)` crop to `(200, 200)`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | Input image or batch of images (as a tensor or NumPy array). Must be in format `(height, width, channels)` or `(batch_size, height, width, channels)`. |
| `size` | Tuple of `(height, width)` integer. Target size. |
| `interpolation` | String, interpolation to use for resizing. Supports `"bilinear"`, `"nearest"`, `"bicubic"`, `"lanczos3"`, `"lanczos5"`. Defaults to `"bilinear"`. |
| `data_format` | `"channels_last"` or `"channels_first"`. |

|     |
| --- |
| Returns<br>------- |     |
| Array with shape `(size[0], size[1], channels)`. If the input image was a NumPy array, the output is a NumPy array, and if it was a backend-native tensor, the output is a backend-native tensor. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.