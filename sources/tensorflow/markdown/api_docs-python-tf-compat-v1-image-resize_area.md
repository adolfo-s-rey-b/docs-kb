[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/image/resize_area#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/image/resize_area)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/image/resize_area?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/image/resize_area#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/image/resize_area#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.image.resize\_area Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/image/resize_area#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/image/resize_area#returns)
    

Resize `images` to `size` using area interpolation. (deprecated)

tf.compat.v1.image.resize_area(
        images: Annotated[Any, TV_ResizeArea_T],
        size: Annotated[Any, _atypes.Int32],
        align_corners: bool = False,
        name=None
    ) -> Annotated[Any, _atypes.Float32]

Input images can be of different types but output images are always float.

The range of pixel values for the output image might be slightly different from the range for the input image because of limited numerical precision. To guarantee an output range, for example `[0.0, 1.0]`, apply [`tf.clip_by_value`](https://www.tensorflow.org/api_docs/python/tf/clip_by_value)
 to the output.

Each output pixel is computed by first transforming the pixel's footprint into the input tensor and then averaging the pixels that intersect the footprint. An input pixel's contribution to the average is weighted by the fraction of its area that intersects the footprint. This is the same as OpenCV's INTER\_AREA.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `images` | A `Tensor`. Must be one of the following types: `int8`, `uint8`, `int16`, `uint16`, `int32`, `int64`, `half`, `float32`, `float64`, `bfloat16`. 4-D with shape `[batch, height, width, channels]`. |
| `size` | A 1-D int32 Tensor of 2 elements: `new_height, new_width`. The new size for the images. |
| `align_corners` | An optional `bool`. Defaults to `False`. If true, the centers of the 4 corner pixels of the input and output tensors are aligned, preserving the values at the corner pixels. Defaults to false. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` of type `float32`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.