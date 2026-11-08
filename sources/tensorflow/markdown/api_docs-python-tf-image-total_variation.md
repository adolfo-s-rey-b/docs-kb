[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/image/total_variation#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   English
*   中文 – 简体

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.image.total\_variation Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/image_ops_impl.py#L3364-L3433)

Calculate and return the total variation for one or more images.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.image.total_variation`](https://www.tensorflow.org/api_docs/python/tf/image/total_variation)

tf.image.total_variation(
        images, name=None
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Neural style transfer](https://www.tensorflow.org/tutorials/generative/style_transfer) |

The total variation is the sum of the absolute differences for neighboring pixel-values in the input images. This measures how much noise is in the images.

This can be used as a loss-function during optimization so as to suppress noise in images. If you have a batch of images, then you should calculate the scalar loss-value as the sum: `loss = tf.reduce_sum(tf.image.total_variation(images))`

This implements the anisotropic 2-D version of the formula described here:

[https://en.wikipedia.org/wiki/Total\_variation\_denoising](https://en.wikipedia.org/wiki/Total_variation_denoising)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `images` | 4-D Tensor of shape `[batch, height, width, channels]` or 3-D Tensor of shape `[height, width, channels]`. |
| `name` | A name for the operation (optional). |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | if images.shape is not a 3-D or 4-D vector. |

|     |
| --- |
| Returns<br>------- |     |
| The total variation of `images`.<br><br>If `images` was 4-D, return a 1-D float Tensor of shape `[batch]` with the total variation for each image in the batch. If `images` was 3-D, return a scalar float with the total variation for that image. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.