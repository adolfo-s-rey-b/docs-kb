[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/extract_patches#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/extract_patches)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/extract_patches?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/extract_patches#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/extract_patches#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.image.extract\_patches Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/extract_patches#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/extract_patches#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/image.py#L657-L749)

Extracts patches from the image(s) or volume(s).

tf.keras.ops.image.extract_patches(
        images,
        size,
        strides=None,
        dilation_rate=1,
        padding='valid',
        data_format=None
    )

This function supports both 2D and 3D patch extraction based on the `size` argument length, similar to how [`keras.ops.conv`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/conv)
 handles different dimensions.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `images` | Input image/volume or batch of images/volumes. For 2D patches: 3D `(H, W, C)` or 4D `(N, H, W, C)`. For 3D patches: 4D `(D, H, W, C)` or 5D `(N, D, H, W, C)`. |
| `size` | Patch size as int or tuple. Length 2 tuple `(patch_height, patch_width)` or int for 2D patches. Length 3 tuple `(patch_depth, patch_height, patch_width)` for 3D patches. |
| `strides` | Strides for patch extraction. If not specified, defaults to `size` (non-overlapping patches). |
| `dilation_rate` | Dilation rate for patch extraction. Note that `dilation_rate > 1` is not supported with `strides > 1`. |
| `padding` | The type of padding algorithm to use: `"same"` or `"valid"`. |
| `data_format` | A string specifying the data format of the input tensor. It can be either `"channels_last"` or `"channels_first"`. If not specified, defaults to [`keras.config.image_data_format`](https://www.tensorflow.org/api_docs/python/tf/keras/backend/image_data_format)<br>. |

|     |
| --- |
| Returns<br>------- |     |
| Extracted patches with shape depending on input and `size`:<br><br>*   2D patches: 3D (unbatched) or 4D (batched)<br>*   3D patches: 4D (unbatched) or 5D (batched) |     |

#### Examples:

    # 2D patches from batch of images

    # 2D patches from single image

    # 3D patches from batch of volumes

    # 3D patches from single volume

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.