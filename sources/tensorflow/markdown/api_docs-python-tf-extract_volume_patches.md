[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/extract_volume_patches#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/extract_volume_patches)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/extract_volume_patches?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/extract_volume_patches#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/extract_volume_patches#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.extract\_volume\_patches Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/extract_volume_patches#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/extract_volume_patches#returns)
    

Extract `patches` from `input` and put them in the `"depth"` output dimension. 3D extension of `extract_image_patches`.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.extract_volume_patches`](https://www.tensorflow.org/api_docs/python/tf/extract_volume_patches)

tf.extract_volume_patches(
        input: Annotated[Any, TV_ExtractVolumePatches_T],
        ksizes,
        strides,
        padding: str,
        name=None
    ) -> Annotated[Any, TV_ExtractVolumePatches_T]

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`. 5-D Tensor with shape `[batch, in_planes, in_rows, in_cols, depth]`. |
| `ksizes` | A list of `ints` that has length `>= 5`. The size of the sliding window for each dimension of `input`. |
| `strides` | A list of `ints` that has length `>= 5`. 1-D of length 5. How far the centers of two consecutive patches are in `input`. Must be: `[1, stride_planes, stride_rows, stride_cols, 1]`. |
| `padding` | A `string` from: `"SAME", "VALID"`. The type of padding algorithm to use.<br><br>The size-related attributes are specified as follows:<br><br>ksizes = [1, ksize_planes, ksize_rows, ksize_cols, 1]<br>    strides = [1, stride_planes, strides_rows, strides_cols, 1] |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor`. Has the same type as `input`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.