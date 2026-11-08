[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/scale_and_translate#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/scale_and_translate)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/scale_and_translate?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/scale_and_translate#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/scale_and_translate#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.image.scale\_and\_translate Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/scale_and_translate#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/scale_and_translate#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/image.py#L2021-L2105)

Apply a scale and translation to the images.

tf.keras.ops.image.scale_and_translate(
        images,
        output_shape,
        scale,
        translation,
        spatial_dims,
        method,
        antialias=True
    )

Generates a new image of `output_shape` by resampling from the input image using the sampling method corresponding to method. For 2D images, this operation transforms a location in the input images, (x, y), to a location in the output image according to:

`(x * scale[1] + translation[1], y * scale[0] + translation[0])`.

(Note the inverse warp is used to generate the sample locations.) Assumes half-centered pixels, i.e the pixel at integer location row, col has coordinates y, x = row + 0.5, col + 0.5, and similarly for other input image dimensions.

If an output location(pixel) maps to an input sample location that is outside the input boundaries then the value for the output location will be set to zero.

The `method` argument expects one of the following resize methods:

*   `"linear"`, `"bilinear"`, `"trilinear"`, `"triangle"`: Linear interpolation. If `antialias` is True, uses a triangular filter when downsampling.
*   `"cubic"`, `"bicubic"`, `"tricubic"`: Cubic interpolation, using the Keys cubic kernel.
*   `"lanczos3"`: Lanczos resampling, using a kernel of radius 3.
*   `"lanczos5"`: Lanczos resampling, using a kernel of radius 5.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `images` | The input array. |
| `output_shape` | The output shape, as a sequence of integers with length equal to the number of dimensions of image. |
| `scale` | A \[K\] array with the same number of dimensions as `images`, containing the scale to apply in each dimension. |
| `translation` | A \[K\] array with the same number of dimensions as `images`, containing the translation to apply in each dimension. |
| `spatial_dims` | A length K tuple specifying the spatial dimensions that the passed `scale` and `translation` should be applied to. |
| `method` | A string specifying the resizing method to use. Available methods are `"linear"`, `"bilinear"`, `"trilinear"`, `"triangle"`, `"cubic"`, `"bicubic"`, `"tricubic"`, `"lanczos3"` and `"lanczos5"`. |
| `antialias` | Whether an antialiasing filter should be applied when downsampling. Has no effect when upsampling. Defaults to `True`. |

|     |
| --- |
| Returns<br>------- |     |
| The scale and translated images. |     |

#### Example:

    images = np.arange(9, dtype="float32").reshape((3, 3))

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.