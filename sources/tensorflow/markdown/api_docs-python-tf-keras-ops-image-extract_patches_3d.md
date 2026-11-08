[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/extract_patches_3d#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/extract_patches_3d)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/extract_patches_3d?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/extract_patches_3d#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/extract_patches_3d#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.image.extract\_patches\_3d Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/extract_patches_3d#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/extract_patches_3d#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/image.py#L865-L928)

Extracts patches from the volume(s).

tf.keras.ops.image.extract_patches_3d(
        volumes,
        size,
        strides=None,
        dilation_rate=1,
        padding='valid',
        data_format=None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `volumes` | Input volume or batch of volumes. Must be 4D or 5D. |
| `size` | Patch size int or tuple (patch\_depth, patch\_height, patch\_width) |
| `strides` | strides along depth, height, and width. If not specified, or if `None`, it defaults to the same value as `size`. |
| `dilation_rate` | This is the input stride, specifying how far two consecutive patch samples are in the input. Note that using `dilation_rate > 1` is not supported in conjunction with `strides > 1` on the TensorFlow backend. |
| `padding` | The type of padding algorithm to use: `"same"` or `"valid"`. |
| `data_format` | A string specifying the data format of the input tensor. It can be either `"channels_last"` or `"channels_first"`. `"channels_last"` corresponds to inputs with shape `(batch, depth, height, width, channels)`, while `"channels_first"` corresponds to inputs with shape `(batch, channels, depth, height, width)`. If not specified, the value will default to [`keras.config.image_data_format()`](https://www.tensorflow.org/api_docs/python/tf/keras/backend/image_data_format)<br>. |

|     |
| --- |
| Returns<br>------- |     |
| Extracted patches 4D (if not batched) or 5D (if batched) |     |

#### Examples:

    import numpy as np

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.