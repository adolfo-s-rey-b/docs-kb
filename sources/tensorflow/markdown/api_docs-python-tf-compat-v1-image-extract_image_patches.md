[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/image/extract_image_patches#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/image/extract_image_patches)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/image/extract_image_patches?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/image/extract_image_patches#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/image/extract_image_patches#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.image.extract\_image\_patches Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/image/extract_image_patches#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/image/extract_image_patches#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/array_ops.py#L6361-L6409)

Extract `patches` from `images` and put them in the "depth" output dimension.

tf.compat.v1.image.extract_image_patches(
        images,
        ksizes=None,
        strides=None,
        rates=None,
        padding=None,
        name=None,
        sizes=None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `images` | A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `int8`, `int16`, `int32`, `int64`, `uint8`, `uint16`, `uint32`, `uint64`, `complex64`, `complex128`, `bool`. 4-D Tensor with shape `[batch, in_rows, in_cols, depth]`. |
| `ksizes` | A list of `ints` that has length `>= 4`. The size of the sliding window for each dimension of `images`. |
| `strides` | A list of `ints` that has length `>= 4`. How far the centers of two consecutive patches are in the images. Must be: `[1, stride_rows, stride_cols, 1]`. |
| `rates` | A list of `ints` that has length `>= 4`. Must be: `[1, rate_rows, rate_cols, 1]`. This is the input stride, specifying how far two consecutive patch samples are in the input. Equivalent to extracting patches with `patch_sizes_eff = patch_sizes + (patch_sizes - 1) * (rates - 1)`, followed by subsampling them spatially by a factor of `rates`. This is equivalent to `rate` in dilated (a.k.a. Atrous) convolutions. |
| `padding` | A `string` from: `"SAME", "VALID"`. The type of padding algorithm to use. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor`. Has the same type as `images`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.