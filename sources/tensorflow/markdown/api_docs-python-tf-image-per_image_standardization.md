[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/image/per_image_standardization#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/image/per_image_standardization)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/image/per_image_standardization?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/image/per_image_standardization#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/image/per_image_standardization#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/image/per_image_standardization#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/image/per_image_standardization#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.image.per\_image\_standardization Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/image/per_image_standardization#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/image/per_image_standardization#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/image/per_image_standardization#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/image/per_image_standardization#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/image_ops_impl.py#L1964-L2020)

Linearly scales each image in `image` to have mean 0 and variance 1.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.image.per_image_standardization`](https://www.tensorflow.org/api_docs/python/tf/image/per_image_standardization)

tf.image.per_image_standardization(
        image
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [TFF simulations with accelerators](https://www.tensorflow.org/federated/tutorials/simulations_with_accelerators) |

For each 3-D image `x` in `image`, computes `(x - mean) / adjusted_stddev`, where

*   `mean` is the average of all values in `x`
*   `adjusted_stddev = max(stddev, 1.0/sqrt(N))` is capped away from 0 to protect against division by 0 when handling uniform images
    *   `N` is the number of elements in `x`
    *   `stddev` is the standard deviation of all values in `x`

#### Example Usage:

    image = tf.constant(np.arange(1, 13, dtype=np.int32), shape=[2, 2, 3])

|     |     |
| --- | --- |
| Args<br>---- |     |
| `image` | An n-D `Tensor` with at least 3 dimensions, the last 3 of which are the dimensions of each image. |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` with the same shape as `image` and its dtype is `float32`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | The shape of `image` has fewer than 3 dimensions. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.