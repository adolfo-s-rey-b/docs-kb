[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/applications/resnet_v2/preprocess_input#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/applications/resnet_v2/preprocess_input)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/applications/resnet_v2/preprocess_input?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/applications/resnet_v2/preprocess_input#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/applications/resnet_v2/preprocess_input#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/keras/applications/resnet_v2/preprocess_input#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.applications.resnet\_v2.preprocess\_input Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/applications/resnet_v2/preprocess_input#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/applications/resnet_v2/preprocess_input#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/keras/applications/resnet_v2/preprocess_input#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/applications/resnet_v2.py#L132-L136)

Preprocesses a tensor or Numpy array encoding a batch of images.

tf.keras.applications.resnet_v2.preprocess_input(
        x, data_format=None
    )

Usage example with [`applications.MobileNet`](https://www.tensorflow.org/api_docs/python/tf/keras/applications/MobileNet)
:

i = keras.layers.Input([None, None, 3], dtype="uint8")
    x = ops.cast(i, "float32")
    x = keras.applications.mobilenet.preprocess_input(x)
    core = keras.applications.MobileNet()
    x = core(x)
    model = keras.Model(inputs=[i], outputs=[x])
    result = model(image)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | A floating point [`numpy.array`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/array)<br> or a backend-native tensor, 3D or 4D with 3 color channels, with values in the range \[0, 255\]. The preprocessed data are written over the input data if the data types are compatible. To avoid this behaviour, [`numpy.copy(x)`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/copy)<br> can be used. |
| `data_format` | Optional data format of the image tensor/array. None, means the global setting [`keras.backend.image_data_format()`](https://www.tensorflow.org/api_docs/python/tf/keras/backend/image_data_format)<br> is used (unless you changed it, it uses "channels\_last"). Defaults to `None`. |

|     |
| --- |
| Returns<br>------- |     |
| Preprocessed array with type `float32`.<br><br>The inputs pixel values are scaled between -1 and 1, sample-wise. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | In case of unknown `data_format` argument. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.