[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/serialize#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/serialize)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/serialize?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/serialize#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/serialize#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.optimizers.schedules.serialize Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/serialize#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/serialize#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/optimizers/schedules/learning_rate_schedule.py#L921-L940)

Serializes a `LearningRateSchedule` into a JSON-compatible dict.

tf.keras.optimizers.schedules.serialize(
        learning_rate_schedule
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `learning_rate_schedule` | The `LearningRateSchedule` object to serialize. |

|     |
| --- |
| Returns<br>------- |     |
| A JSON-serializable dict representing the object's config. |     |

#### Example:

    lr_schedule = keras.optimizers.schedules.ExponentialDecay(

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.