[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/image/hsv_to_rgb#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/image/hsv_to_rgb)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/image/hsv_to_rgb?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fimage%2Fhsv_to_rgb&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/image/hsv_to_rgb#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/image/hsv_to_rgb#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.image.hsv\_to\_rgb Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/image/hsv_to_rgb#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/image/hsv_to_rgb#returns)
    

Convert one or more images from HSV to RGB.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.image.hsv_to_rgb`](https://www.tensorflow.org/api_docs/python/tf/image/hsv_to_rgb)

tf.image.hsv_to_rgb(
        images: Annotated[Any, TV_HSVToRGB_T], name=None
    ) -> Annotated[Any, TV_HSVToRGB_T]

Outputs a tensor of the same shape as the `images` tensor, containing the RGB value of the pixels. The output is only well defined if the value in `images` are in `[0,1]`.

See `rgb_to_hsv` for a description of the HSV encoding.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `images` | A `Tensor`. Must be one of the following types: `half`, `bfloat16`, `float32`, `float64`. 1-D or higher rank. HSV data to convert. Last dimension must be size 3. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor`. Has the same type as `images`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.