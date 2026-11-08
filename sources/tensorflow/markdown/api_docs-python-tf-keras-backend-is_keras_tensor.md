[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/backend/is_keras_tensor#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/backend/is_keras_tensor)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/backend/is_keras_tensor?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Fbackend%2Fis_keras_tensor&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.backend.is\_keras\_tensor Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/common/keras_tensor.py#L414-L425)

Returns whether `x` is a Keras tensor.

#### View aliases

**Main aliases**

[`tf.keras.utils.is_keras_tensor`](https://www.tensorflow.org/api_docs/python/tf/keras/backend/is_keras_tensor)

tf.keras.backend.is_keras_tensor(
        x
    )

A "Keras tensor" is a _symbolic tensor_, such as a tensor that was created via `Input()`. A "symbolic tensor" can be understood as a placeholder -- it does not contain any actual numerical data, only a shape and dtype. It can be used for building Functional models, but it cannot be used in actual computations.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.