[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/losses/get#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   English
*   中文 – 简体

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.losses.get Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/losses/__init__.py#L162-L207)

Retrieves a Keras loss as a `function`/`Loss` class instance.

tf.keras.losses.get(
        identifier
    )

The `identifier` may be the string name of a loss function or `Loss` class.

    loss = losses.get("categorical_crossentropy")

You can also specify `config` of the loss to this function by passing dict containing `class_name` and `config` as an identifier. Also note that the `class_name` must map to a `Loss` class

    identifier = {"class_name": "CategoricalCrossentropy",

|     |     |
| --- | --- |
| Args<br>---- |     |
| `identifier` | A loss identifier. One of None or string name of a loss function/class or loss configuration dictionary or a loss function or a loss class instance. |

|     |
| --- |
| Returns<br>------- |     |
| A Keras loss as a `function`/ `Loss` class instance. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.