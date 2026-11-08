[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/config/set_backend#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/config/set_backend)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/config/set_backend?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.config.set\_backend Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/utils/backend_utils.py#L122-L188)

Reload the backend (and the Keras package).

tf.keras.config.set_backend(
        backend
    )

#### Example:

    import os

⚠️ WARNING ⚠️: Using this function is dangerous and should be done carefully. Changing the backend will **NOT** convert the type of any already-instantiated objects. Thus, any layers / tensors / etc. already created will no longer be usable without errors. It is strongly recommended **not** to keep around **any** Keras-originated objects instances created before calling `set_backend()`.

This includes any function or class instance that uses any Keras functionality. All such code needs to be re-executed after calling `set_backend()` and re-importing all imported `keras` modules.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.