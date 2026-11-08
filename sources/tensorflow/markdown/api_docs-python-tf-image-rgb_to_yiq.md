[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/image/rgb_to_yiq#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/image/rgb_to_yiq)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/image/rgb_to_yiq?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fimage%2Frgb_to_yiq&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/image/rgb_to_yiq#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/image/rgb_to_yiq#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.image.rgb\_to\_yiq Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/image/rgb_to_yiq#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/image/rgb_to_yiq#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/image_ops_impl.py#L4007-L4034)

Converts one or more images from RGB to YIQ.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.image.rgb_to_yiq`](https://www.tensorflow.org/api_docs/python/tf/image/rgb_to_yiq)

tf.image.rgb_to_yiq(
        images
    )

Outputs a tensor of the same shape as the `images` tensor, containing the YIQ value of the pixels. The output is only well defined if the value in images are in \[0,1\].

#### Usage Example:

    x = tf.constant([[[1.0, 2.0, 3.0]]])

|     |     |
| --- | --- |
| Args<br>---- |     |
| `images` | 2-D or higher rank. Image data to convert. Last dimension must be size 3. |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `images` | tensor with the same shape as `images`. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.