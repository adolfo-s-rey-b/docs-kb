[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/config/max_epochs#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/config/max_epochs)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/config/max_epochs?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/config/max_epochs#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.config.max\_epochs Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================

*   On this page
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/config/max_epochs#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/config.py#L426-L438)

Get the maximum number of epochs for any call to fit.

tf.keras.config.max_epochs()

Retrieves the limit on the number of epochs set by [`keras.config.set_max_epochs`](https://www.tensorflow.org/api_docs/python/tf/keras/config/set_max_epochs)
 or the `KERAS_MAX_EPOCHS` environment variable.

|     |
| --- |
| Returns<br>------- |     |
| The integer limit on the number of epochs or `None`, if no limit has been set. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.