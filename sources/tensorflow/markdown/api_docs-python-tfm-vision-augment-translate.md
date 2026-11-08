[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/translate#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/translate)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/translate?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftfm%2Fvision%2Faugment%2Ftranslate&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/translate#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/translate#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.augment.translate Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/translate#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/translate#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/augment.py#L474-L503)

Translates image(s) by provided vectors.

tfm.vision.augment.translate(
        image: tf.Tensor,
        translations,
        fill_value: float = 0.0,
        fill_mode: str = 'reflect',
        interpolation: str = 'nearest'
    ) -> tf.Tensor

|     |     |
| --- | --- |
| Args<br>---- |     |
| `image` | An image Tensor of type uint8. |
| `translations` | A vector or matrix representing \[dx dy\]. |
| `fill_value` | a float represents the value to be filled outside the boundaries when `fill_mode="constant"`. |
| `fill_mode` | Points outside the boundaries of the input are filled according to the given mode (one of `{"constant", "reflect", "wrap", "nearest"}`). |
| `interpolation` | Interpolation mode. Supported values: `"nearest"`, `"bilinear"`. |

|     |
| --- |
| Returns<br>------- |     |
| The translated version of the image. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.