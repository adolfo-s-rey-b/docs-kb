[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/utils/img_to_array#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/utils/img_to_array)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/utils/img_to_array?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Futils%2Fimg_to_array&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/utils/img_to_array#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/utils/img_to_array#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/utils/img_to_array#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.utils.img\_to\_array Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/utils/img_to_array#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/utils/img_to_array#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/utils/img_to_array#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/utils/image_utils.py#L110-L159)

Converts a PIL Image instance to a NumPy array.

#### View aliases

**Main aliases**

[`tf.keras.preprocessing.image.img_to_array`](https://www.tensorflow.org/api_docs/python/tf/keras/utils/img_to_array)

tf.keras.utils.img_to_array(
        img, data_format=None, dtype=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Using the SavedModel format](https://www.tensorflow.org/guide/saved_model) | *   [DeepDream](https://www.tensorflow.org/tutorials/generative/deepdream)<br>    <br>*   [Image classification](https://www.tensorflow.org/tutorials/images/classification) |

#### Example:

from PIL import Image
    img_data = np.random.random(size=(100, 100, 3))
    img = keras.utils.array_to_img(img_data)
    array = keras.utils.image.img_to_array(img)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `img` | Input PIL Image instance. |
| `data_format` | Image data format, can be either `"channels_first"` or `"channels_last"`. Defaults to `None`, in which case the global setting [`keras.backend.image_data_format()`](https://www.tensorflow.org/api_docs/python/tf/keras/backend/image_data_format)<br> is used (unless you changed it, it defaults to `"channels_last"`). |
| `dtype` | Dtype to use. `None` means the global setting [`keras.backend.floatx()`](https://www.tensorflow.org/api_docs/python/tf/keras/backend/floatx)<br> is used (unless you changed it, it defaults to `"float32"`). |

|     |
| --- |
| Returns<br>------- |     |
| A 3D NumPy array. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.