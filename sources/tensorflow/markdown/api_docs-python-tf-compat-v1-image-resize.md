[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/image/resize#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/image/resize)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/image/resize?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/image/resize#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/image/resize#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/image/resize#raises)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/image/resize#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.image.resize Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/image/resize#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/image/resize#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/image/resize#raises)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/image/resize#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/image_ops_impl.py#L1534-L1617)

Resize `images` to `size` using the specified `method`.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.image.resize_images`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/image/resize)

tf.compat.v1.image.resize(
        images,
        size,
        method=ResizeMethodV1.BILINEAR,
        align_corners=False,
        preserve_aspect_ratio=False,
        name=None
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Classify Flowers with Transfer Learning](https://www.tensorflow.org/hub/tutorials/image_feature_vector) |

Resized images will be distorted if their original aspect ratio is not the same as `size`. To avoid distortions see [`tf.image.resize_with_pad`](https://www.tensorflow.org/api_docs/python/tf/image/resize_with_pad)
 or [`tf.image.resize_with_crop_or_pad`](https://www.tensorflow.org/api_docs/python/tf/image/resize_with_crop_or_pad)
.

The `method` can be one of:

*   **[`tf.image.ResizeMethod.BILINEAR`](https://www.tensorflow.org/api_docs/python/tf/image/ResizeMethod#BILINEAR)
    **: [Bilinear interpolation.](https://en.wikipedia.org/wiki/Bilinear_interpolation)
    
*   **[`tf.image.ResizeMethod.NEAREST_NEIGHBOR`](https://www.tensorflow.org/api_docs/python/tf/image/ResizeMethod#NEAREST_NEIGHBOR)
    **: [Nearest neighbor interpolation.](https://en.wikipedia.org/wiki/Nearest-neighbor_interpolation)
    
*   **[`tf.image.ResizeMethod.BICUBIC`](https://www.tensorflow.org/api_docs/python/tf/image/ResizeMethod#BICUBIC)
    **: [Bicubic interpolation.](https://en.wikipedia.org/wiki/Bicubic_interpolation)
    
*   **[`tf.image.ResizeMethod.AREA`](https://www.tensorflow.org/api_docs/python/tf/image/ResizeMethod#AREA)
    **: Area interpolation.

The return value has the same type as `images` if `method` is [`tf.image.ResizeMethod.NEAREST_NEIGHBOR`](https://www.tensorflow.org/api_docs/python/tf/image/ResizeMethod#NEAREST_NEIGHBOR)
. It will also have the same type as `images` if the size of `images` can be statically determined to be the same as `size`, because `images` is returned in this case. Otherwise, the return value has type `float32`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `images` | 4-D Tensor of shape `[batch, height, width, channels]` or 3-D Tensor of shape `[height, width, channels]`. |
| `size` | A 1-D int32 Tensor of 2 elements: `new_height, new_width`. The new size for the images. |
| `method` | ResizeMethod. Defaults to [`tf.image.ResizeMethod.BILINEAR`](https://www.tensorflow.org/api_docs/python/tf/image/ResizeMethod#BILINEAR)<br>. |
| `align_corners` | bool. If True, the centers of the 4 corner pixels of the input and output tensors are aligned, preserving the values at the corner pixels. Defaults to `False`. |
| `preserve_aspect_ratio` | Whether to preserve the aspect ratio. If this is set, then `images` will be resized to a size that fits in `size` while preserving the aspect ratio of the original image. Scales up the image if `size` is bigger than the current size of the `image`. Defaults to False. |
| `name` | A name for this operation (optional). |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | if the shape of `images` is incompatible with the shape arguments to this function |
| `ValueError` | if `size` has invalid shape or type. |
| `ValueError` | if an unsupported resize method is specified. |

|     |
| --- |
| Returns<br>------- |     |
| If `images` was 4-D, a 4-D float Tensor of shape `[batch, new_height, new_width, channels]`. If `images` was 3-D, a 3-D float Tensor of shape `[new_height, new_width, channels]`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.