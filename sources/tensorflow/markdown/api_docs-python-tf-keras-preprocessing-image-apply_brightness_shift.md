[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/apply_brightness_shift#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/apply_brightness_shift)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/apply_brightness_shift?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Fpreprocessing%2Fimage%2Fapply_brightness_shift&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/apply_brightness_shift#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/apply_brightness_shift#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/apply_brightness_shift#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.preprocessing.image.apply\_brightness\_shift Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/apply_brightness_shift#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/apply_brightness_shift#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/apply_brightness_shift#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/legacy/preprocessing/image.py#L1703-L1731)

Performs a brightness shift.

tf.keras.preprocessing.image.apply_brightness_shift(
        x, brightness, scale=True
    )

DEPRECATED.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | Input tensor. Must be 3D. |
| `brightness` | Float. The new brightness value. |
| `scale` | Whether to rescale the image such that minimum and maximum values are 0 and 255 respectively. Default: True. |

|     |
| --- |
| Returns<br>------- |     |
| Numpy image tensor. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ImportError` | if PIL is not available. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.