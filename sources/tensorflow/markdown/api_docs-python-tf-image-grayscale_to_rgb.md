[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/image/grayscale_to_rgb#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/image/grayscale_to_rgb)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/image/grayscale_to_rgb?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/image/grayscale_to_rgb#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/image/grayscale_to_rgb#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.image.grayscale\_to\_rgb Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/image/grayscale_to_rgb#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/image/grayscale_to_rgb#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/image_ops_impl.py#L2606-L2639)

Converts one or more images from Grayscale to RGB.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.image.grayscale_to_rgb`](https://www.tensorflow.org/api_docs/python/tf/image/grayscale_to_rgb)

tf.image.grayscale_to_rgb(
        images, name=None
    )

Outputs a tensor of the same `DType` and rank as `images`. The size of the last dimension of the output is 3, containing the RGB value of the pixels. The input images' last dimension must be size 1.

    original = tf.constant([[[1.0], [2.0], [3.0]]])

|     |     |
| --- | --- |
| Args<br>---- |     |
| `images` | The Grayscale tensor to convert. The last dimension must be size 1. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| The converted grayscale image(s). |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.