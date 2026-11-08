[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/shear_with_bboxes#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/shear_with_bboxes)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/shear_with_bboxes?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/shear_with_bboxes#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/shear_with_bboxes#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/shear_with_bboxes#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.augment.shear\_with\_bboxes Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/shear_with_bboxes#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/shear_with_bboxes#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/shear_with_bboxes#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/augment.py#L1516-L1554)

Applies Shear Transformation to the image and shifts the bboxes.

tfm.vision.augment.shear_with_bboxes(
        image, bboxes, level, replace, shear_horizontal
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `image` | 3D uint8 Tensor. |
| `bboxes` | 2D Tensor that is a list of the bboxes in the image. Each bbox has 4 elements (min\_y, min\_x, max\_y, max\_x) of type float with values between \[0, 1\]. |
| `level` | Float. How much to shear the image. This value will be between -0.3 to 0.3. |
| `replace` | A one or three value 1D tensor to fill empty pixels. |
| `shear_horizontal` | Boolean. If true then shear in X dimension else shear in the Y dimension. |

|     |
| --- |
| Returns<br>------- |     |
| A tuple containing a 3D uint8 Tensor that will be the result of shearing image by level. The second element of the tuple is bboxes, where now the coordinates will be shifted to reflect the sheared image. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If applied to video. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.