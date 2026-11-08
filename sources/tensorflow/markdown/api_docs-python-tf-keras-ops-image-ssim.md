[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/ssim#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/ssim)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/ssim?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Fops%2Fimage%2Fssim&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/ssim#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/ssim#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.image.ssim Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/ssim#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/image/ssim#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/image.py#L2224-L2308)

Computes the Structural Similarity Index (SSIM) between two images.

tf.keras.ops.image.ssim(
        image1,
        image2,
        max_val=1.0,
        filter_size=11,
        filter_sigma=1.5,
        k1=0.01,
        k2=0.03,
        data_format=None
    )

The SSIM index is a method for measuring the similarity between two images. It is based on the comparison of luminance, contrast, and structure between the images. The resulting SSIM index is a value between -1 and 1, where 1 indicates identical images.

This implementation is based on the original SSIM paper: Wang, Z., Bovik, A. C., Sheikh, H. R., & Simoncelli, E. P. (2004). "Image quality assessment: from error visibility to structural similarity." IEEE Transactions on Image Processing.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `image1` | First image or batch of images. Must be 3D or 4D. |
| `image2` | Second image or batch of images. Must have the same shape as `image1`. |
| `max_val` | The maximum possible pixel value of the images. Defaults to `1.0` (for normalized images). Use `255.0` for images with pixel values in `[0, 255]`. |
| `filter_size` | Size of the Gaussian filter used for computing SSIM. Defaults to `11`. Must be an odd integer >= 1. |
| `filter_sigma` | Standard deviation of the Gaussian filter. Defaults to `1.5`. |
| `k1` | First stabilization constant. Defaults to `0.01`. |
| `k2` | Second stabilization constant. Defaults to `0.03`. |
| `data_format` | A string specifying the data format of the input tensor. It can be either `"channels_last"` or `"channels_first"`. `"channels_last"` corresponds to inputs with shape `(batch, height, width, channels)`, while `"channels_first"` corresponds to inputs with shape `(batch, channels, height, width)`. If not specified, the value will default to [`keras.config.image_data_format`](https://www.tensorflow.org/api_docs/python/tf/keras/backend/image_data_format)<br>. |

|     |
| --- |
| Returns<br>------- |     |
| A tensor of SSIM values. For batched inputs, returns a 1D tensor with one SSIM value per image pair. For unbatched inputs, returns a scalar tensor. |     |

#### Examples:

    import numpy as np

    # Batched images

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.