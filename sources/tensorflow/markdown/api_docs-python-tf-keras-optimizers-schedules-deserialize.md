[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/deserialize#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/deserialize)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/deserialize?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/deserialize#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/deserialize#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.optimizers.schedules.deserialize Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/deserialize#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/deserialize#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/optimizers/schedules/learning_rate_schedule.py#L943-L978)

Instantiates a `LearningRateSchedule` object from a serialized form.

tf.keras.optimizers.schedules.deserialize(
        config, custom_objects=None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `config` | The serialized form of the `LearningRateSchedule`. Dictionary of the form {'class\_name': str, 'config': dict}. |
| `custom_objects` | A dictionary mapping class names (or function names) of custom (non-Keras) objects to class/functions. |

|     |
| --- |
| Returns<br>------- |     |
| A `LearningRateSchedule` object. |     |

#### Example:

# Configuration for PolynomialDecay
    config = {
        'class_name': 'PolynomialDecay',
        'config': {'cycle': False,
            'decay_steps': 10000,
            'end_learning_rate': 0.01,
            'initial_learning_rate': 0.1,
            'name': None,
            'power': 0.5
        }
    }
    lr_schedule = keras.optimizers.schedules.deserialize(config)

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.