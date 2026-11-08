[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/config/set_max_steps_per_epoch#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/config/set_max_steps_per_epoch)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/config/set_max_steps_per_epoch?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Fconfig%2Fset_max_steps_per_epoch&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/config/set_max_steps_per_epoch#args)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.config.set\_max\_steps\_per\_epoch Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/config/set_max_steps_per_epoch#args)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/config.py#L409-L423)

Limit the maximum number of steps for any call to fit/evaluate/predict.

tf.keras.config.set_max_steps_per_epoch(
        max_steps_per_epoch
    )

This will cap the number of steps for single epoch of a call to `fit()`, `evaluate()`, or `predict()`. This is purely for debugging, and can also be set via the `KERAS_MAX_STEPS_PER_EPOCH` environment variable to quickly run a scrip without modifying its source.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `max_epochs` | The integer limit on the number of epochs or `None`. If `None`, no limit is applied. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.