[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/reconstruct_patches#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/reconstruct_patches)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/reconstruct_patches?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/reconstruct_patches#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/reconstruct_patches#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.image.reconstruct\_patches Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/reconstruct_patches#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/reconstruct_patches#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/master/keras/src/ops/image.py#L1086-L1191)

Reconstructs image(s) or volume(s) from non-overlapping patches.

tf.keras.ops.image.reconstruct_patches(
        patches,
        size,
        output_size=None,
        strides=None,
        padding='valid',
        data_format=None
    )

Inverse of [`keras.ops.image.extract_patches`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/extract_patches)
 for the non-overlapping case (`strides == size`).

|     |     |
| --- | --- |
| Args<br>---- |     |
| `patches` | Patches tensor as produced by `extract_patches`. For 2D patches: 3D `(gH, gW, pH*pW*C)` or 4D `(N, gH, gW, pH*pW*C)`. For 3D patches: 4D `(gD, gH, gW, pD*pH*pW*C)` or 5D `(N, gD, gH, gW, pD*pH*pW*C)`. With `data_format="channels_first"` the flat patch dim comes first instead: `(pH*pW*C, gH, gW)` / `(N, pH*pW*C, gH, gW)` for 2D patches, `(pD*pH*pW*C, gD, gH, gW)` / `(N, pD*pH*pW*C, gD, gH, gW)` for 3D patches. |
| `size` | Patch size, matching the `size` used for extraction. Length 2 tuple for 2D, length 3 tuple for 3D, or int. |
| `output_size` | Target spatial shape of the reconstruction. Length 2 tuple `(H, W)` for 2D, length 3 tuple `(D, H, W)` for 3D. With `padding="valid"` this may be omitted (`None`) and is then inferred from the patch grid; if given, it must equal `(grid - 1) * stride + size` per dim — the region covered by the extracted patches, i.e. the original size cropped down to a multiple of `size` in the non-overlapping case. With `padding="same"` it is required: pass the original spatial shape so the padding added during extraction can be unambiguously removed. |
| `strides` | Currently must equal `size` (non-overlapping). Defaults to `size`. |
| `padding` | `"same"` or `"valid"`, matching the extraction. |
| `data_format` | A string specifying the data format of the input tensor. Either `"channels_last"` or `"channels_first"`. With `"channels_first"` the reconstruction is returned in `(C, H, W)` / `(N, C, H, W)` layout. If not specified, defaults to [`keras.config.image_data_format`](https://www.tensorflow.org/api_docs/python/tf/keras/backend/image_data_format)<br>. |

|     |
| --- |
| Returns<br>------- |     |
| Reconstructed image/volume: 2D: 3D (unbatched) or 4D (batched). 3D: 4D (unbatched) or 5D (batched). |     |

#### Examples:

    image = np.random.random((2, 20, 20, 3)).astype("float32")

    # 3D patches: pass a length-3 `size`

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.