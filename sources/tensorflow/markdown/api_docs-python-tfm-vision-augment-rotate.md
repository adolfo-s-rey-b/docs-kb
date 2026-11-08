[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/rotate#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/rotate)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/rotate?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/rotate#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/rotate#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.augment.rotate Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/rotate#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/rotate#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/augment.py#L506-L534)

Rotates the image by degrees either clockwise or counterclockwise.

tfm.vision.augment.rotate(
        image: tf.Tensor, degrees: float
    ) -> tf.Tensor

|     |     |
| --- | --- |
| Args<br>---- |     |
| `image` | An image Tensor of type uint8. |
| `degrees` | Float, a scalar angle in degrees to rotate all images by. If degrees is positive the image will be rotated clockwise otherwise it will be rotated counterclockwise. |

|     |
| --- |
| Returns<br>------- |     |
| The rotated version of image. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.