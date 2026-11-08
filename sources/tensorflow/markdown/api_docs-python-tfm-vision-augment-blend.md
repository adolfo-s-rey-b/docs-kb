[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/blend#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/blend)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/blend?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/blend#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/blend#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.augment.blend Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/blend#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/blend#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/augment.py#L537-L577)

Blend image1 and image2 using 'factor'.

tfm.vision.augment.blend(
        image1: tf.Tensor, image2: tf.Tensor, factor: float
    ) -> tf.Tensor

Factor can be above 0.0. A value of 0.0 means only image1 is used. A value of 1.0 means only image2 is used. A value between 0.0 and 1.0 means we linearly interpolate the pixel values between the two images. A value greater than 1.0 "extrapolates" the difference between the two pixel values, and we clip the results to values between 0 and 255.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `image1` | An image Tensor of type uint8. |
| `image2` | An image Tensor of type uint8. |
| `factor` | A floating point value above 0.0. |

|     |
| --- |
| Returns<br>------- |     |
| A blended image Tensor of type uint8. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.