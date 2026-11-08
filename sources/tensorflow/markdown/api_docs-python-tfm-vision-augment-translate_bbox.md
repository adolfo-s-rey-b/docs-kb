[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/translate_bbox#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/translate_bbox)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/translate_bbox?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftfm%2Fvision%2Faugment%2Ftranslate_bbox&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/translate_bbox#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/translate_bbox#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/translate_bbox#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.augment.translate\_bbox Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/translate_bbox#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/translate_bbox#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/translate_bbox#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/augment.py#L1598-L1635)

Equivalent of PIL Translate in X/Y dimension that shifts image and bbox.

tfm.vision.augment.translate_bbox(
        image, bboxes, pixels, replace, shift_horizontal
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `image` | 3D uint8 Tensor. |
| `bboxes` | 2D Tensor that is a list of the bboxes in the image. Each bbox has 4 elements (min\_y, min\_x, max\_y, max\_x) of type float with values between \[0, 1\]. |
| `pixels` | An int. How many pixels to shift the image and bboxes |
| `replace` | A one or three value 1D tensor to fill empty pixels. |
| `shift_horizontal` | Boolean. If true then shift in X dimension else shift in Y dimension. |

|     |
| --- |
| Returns<br>------- |     |
| A tuple containing a 3D uint8 Tensor that will be the result of translating image by pixels. The second element of the tuple is bboxes, where now the coordinates will be shifted to reflect the shifted image. |     |

|     |
| --- |
| Raises<br>------ |     |
| ValueError if applied to video. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.