[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/image/ssim#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/image/ssim)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/image/ssim?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fimage%2Fssim&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Details](https://www.tensorflow.org/api_docs/python/tf/image/ssim#details)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/image/ssim#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/image/ssim#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.image.ssim Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================

*   On this page
*   [Details](https://www.tensorflow.org/api_docs/python/tf/image/ssim#details)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/image/ssim#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/image/ssim#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/image_ops_impl.py#L4412-L4503)

Computes SSIM index between img1 and img2.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.image.ssim`](https://www.tensorflow.org/api_docs/python/tf/image/ssim)

tf.image.ssim(
        img1,
        img2,
        max_val,
        filter_size=11,
        filter_sigma=1.5,
        k1=0.01,
        k2=0.03,
        return_index_map=False
    )

This function is based on the standard SSIM implementation from: Wang, Z., Bovik, A. C., Sheikh, H. R., & Simoncelli, E. P. (2004). Image quality assessment: from error visibility to structural similarity. IEEE transactions on image processing.

|     |
| --- |
| Details<br>------- |     |
| *   11x11 Gaussian filter of width 1.5 is used.<br>*   k1 = 0.01, k2 = 0.03 as in the original paper. |     |

The image sizes must be at least 11x11 because of the filter size.

#### Example:

    # Read images (of size 255 x 255) from file.
        im1 = tf.image.decode_image(tf.io.read_file('path/to/im1.png'))
        im2 = tf.image.decode_image(tf.io.read_file('path/to/im2.png'))
        tf.shape(im1)  # `img1.png` has 3 channels; shape is `(255, 255, 3)`
        tf.shape(im2)  # `img2.png` has 3 channels; shape is `(255, 255, 3)`
        # Add an outer batch for each image.
        im1 = tf.expand_dims(im1, axis=0)
        im2 = tf.expand_dims(im2, axis=0)
        # Compute SSIM over tf.uint8 Tensors.
        ssim1 = tf.image.ssim(im1, im2, max_val=255, filter_size=11,
                              filter_sigma=1.5, k1=0.01, k2=0.03)
    
        # Compute SSIM over tf.float32 Tensors.
        im1 = tf.image.convert_image_dtype(im1, tf.float32)
        im2 = tf.image.convert_image_dtype(im2, tf.float32)
        ssim2 = tf.image.ssim(im1, im2, max_val=1.0, filter_size=11,
                              filter_sigma=1.5, k1=0.01, k2=0.03)
        # ssim1 and ssim2 both have type tf.float32 and are almost equal.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `img1` | First image batch. 4-D Tensor of shape `[batch, height, width, channels]` with only Positive Pixel Values. |
| `img2` | Second image batch. 4-D Tensor of shape `[batch, height, width, channels]` with only Positive Pixel Values. |
| `max_val` | The dynamic range of the images (i.e., the difference between the maximum the and minimum allowed values). |
| `filter_size` | Default value 11 (size of gaussian filter). |
| `filter_sigma` | Default value 1.5 (width of gaussian filter). |
| `k1` | Default value 0.01 |
| `k2` | Default value 0.03 (SSIM is less sensitivity to K2 for lower values, so it would be better if we took the values in the range of 0 < K2 < 0.4). |
| `return_index_map` | If True returns local SSIM map instead of the global mean. |

|     |
| --- |
| Returns<br>------- |     |
| A tensor containing an SSIM value for each image in batch or a tensor containing an SSIM value for each pixel for each image in batch if return\_index\_map is True. Returned SSIM values are in range (-1, 1\], when pixel values are non-negative. Returns a tensor with shape: broadcast(img1.shape\[:-3\], img2.shape\[:-3\]) or broadcast(img1.shape\[:-1\], img2.shape\[:-1\]). |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.