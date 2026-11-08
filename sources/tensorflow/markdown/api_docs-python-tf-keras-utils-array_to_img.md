[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/utils/array_to_img#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/utils/array_to_img)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/utils/array_to_img?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/utils/array_to_img#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/utils/array_to_img#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/utils/array_to_img#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.utils.array\_to\_img Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/utils/array_to_img#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/utils/array_to_img#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/utils/array_to_img#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/utils/image_utils.py#L35-L107)

Converts a 3D NumPy array to a PIL Image instance.

#### View aliases

**Main aliases**

[`tf.keras.preprocessing.image.array_to_img`](https://www.tensorflow.org/api_docs/python/tf/keras/utils/array_to_img)

tf.keras.utils.array_to_img(
        x, data_format=None, scale=True, dtype=None
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Image segmentation](https://www.tensorflow.org/tutorials/images/segmentation)<br>    <br>*   [Semantic Segmentation with Model Garden](https://www.tensorflow.org/tfmodels/vision/semantic_segmentation)<br>    <br>*   [Adversarial regularization for image classification](https://www.tensorflow.org/neural_structured_learning/tutorials/adversarial_keras_cnn_mnist) |

#### Example:

from PIL import Image
    img = np.random.random(size=(100, 100, 3))
    pil_img = keras.utils.array_to_img(img)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | Input data, in any form that can be converted to a NumPy array. |
| `data_format` | Image data format, can be either `"channels_first"` or `"channels_last"`. Defaults to `None`, in which case the global setting [`keras.backend.image_data_format()`](https://www.tensorflow.org/api_docs/python/tf/keras/backend/image_data_format)<br> is used (unless you changed it, it defaults to `"channels_last"`). |
| `scale` | Whether to rescale the image such that minimum and maximum values are 0 and 255 respectively. Defaults to `True`. |
| `dtype` | Dtype to use. `None` means the global setting [`keras.backend.floatx()`](https://www.tensorflow.org/api_docs/python/tf/keras/backend/floatx)<br> is used (unless you changed it, it defaults to `"float32"`). Defaults to `None`. |

|     |
| --- |
| Returns<br>------- |     |
| A PIL Image instance. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.