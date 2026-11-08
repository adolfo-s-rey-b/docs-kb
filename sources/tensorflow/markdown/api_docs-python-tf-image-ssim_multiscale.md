[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/image/ssim_multiscale#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/image/ssim_multiscale)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/image/ssim_multiscale?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fimage%2Fssim_multiscale&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/image/ssim_multiscale#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/image/ssim_multiscale#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.image.ssim\_multiscale Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/image/ssim_multiscale#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/image/ssim_multiscale#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/image_ops_impl.py#L4510-L4636)

Computes the MS-SSIM between img1 and img2.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.image.ssim_multiscale`](https://www.tensorflow.org/api_docs/python/tf/image/ssim_multiscale)

tf.image.ssim_multiscale(
        img1,
        img2,
        max_val,
        power_factors=_MSSSIM_WEIGHTS,
        filter_size=11,
        filter_sigma=1.5,
        k1=0.01,
        k2=0.03
    )

This function assumes that `img1` and `img2` are image batches, i.e. the last three dimensions are \[height, width, channels\].

Original paper: Wang, Zhou, Eero P. Simoncelli, and Alan C. Bovik. "Multiscale structural similarity for image quality assessment." Signals, Systems and Computers, 2004.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `img1` | First image batch with only Positive Pixel Values. |
| `img2` | Second image batch with only Positive Pixel Values. Must have the same rank as img1. |
| `max_val` | The dynamic range of the images (i.e., the difference between the maximum the and minimum allowed values). |
| `power_factors` | Iterable of weights for each of the scales. The number of scales used is the length of the list. Index 0 is the unscaled resolution's weight and each increasing scale corresponds to the image being downsampled by 2. Defaults to (0.0448, 0.2856, 0.3001, 0.2363, 0.1333), which are the values obtained in the original paper. |
| `filter_size` | Default value 11 (size of gaussian filter). |
| `filter_sigma` | Default value 1.5 (width of gaussian filter). |
| `k1` | Default value 0.01 |
| `k2` | Default value 0.03 (SSIM is less sensitivity to K2 for lower values, so it would be better if we took the values in the range of 0 < K2 < 0.4). |

|     |
| --- |
| Returns<br>------- |     |
| A tensor containing an MS-SSIM value for each image in batch. The values are in range \[0, 1\]. Returns a tensor with shape: broadcast(img1.shape\[:-3\], img2.shape\[:-3\]). |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.