[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/to_4d#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/to_4d)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/to_4d?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftfm%2Fvision%2Faugment%2Fto_4d&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/to_4d#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/to_4d#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/to_4d#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.augment.to\_4d Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/to_4d#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/to_4d#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/to_4d#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/augment.py#L51-L80)

Converts an input Tensor to 4 dimensions.

tfm.vision.augment.to_4d(
        image: tf.Tensor
    ) -> tf.Tensor

4D image => \[N, H, W, C\] or \[N, C, H, W\] 3D image => \[1, H, W, C\] or \[1, C, H, W\] 2D image => \[1, H, W, 1\]

|     |     |
| --- | --- |
| Args<br>---- |     |
| `image` | The 2/3/4D input tensor. |

|     |
| --- |
| Returns<br>------- |     |
| A 4D image tensor. |     |

|     |
| --- |
| Raises<br>------ |     |
| `TypeError` if `image` is not a 2/3/4D tensor. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.