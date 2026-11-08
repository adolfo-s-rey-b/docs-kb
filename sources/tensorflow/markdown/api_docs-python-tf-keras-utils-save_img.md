[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/utils/save_img#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/utils/save_img)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/utils/save_img?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/utils/save_img#args)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.utils.save\_img Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/utils/save_img#args)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/utils/image_utils.py#L162-L196)

Saves an image stored as a NumPy array to a path or file object.

#### View aliases

**Main aliases**

[`tf.keras.preprocessing.image.save_img`](https://www.tensorflow.org/api_docs/python/tf/keras/utils/save_img)

tf.keras.utils.save_img(
        path, x, data_format=None, file_format=None, scale=True, **kwargs
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `path` | Path or file object. |
| `x` | NumPy array. |
| `data_format` | Image data format, either `"channels_first"` or `"channels_last"`. |
| `file_format` | Optional file format override. If omitted, the format to use is determined from the filename extension. If a file object was used instead of a filename, this parameter should always be used. |
| `scale` | Whether to rescale image values to be within `[0, 255]`. |
| `**kwargs` | Additional keyword arguments passed to `PIL.Image.save()`. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.