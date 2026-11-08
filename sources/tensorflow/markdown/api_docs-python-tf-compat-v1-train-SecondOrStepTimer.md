[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SecondOrStepTimer#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SecondOrStepTimer)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SecondOrStepTimer?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SecondOrStepTimer#methods)
    *   [last\_triggered\_step](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SecondOrStepTimer#last_triggered_step)
        
    *   [reset](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SecondOrStepTimer#reset)
        
    *   [should\_trigger\_for\_step](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SecondOrStepTimer#should_trigger_for_step)
        
    *   [update\_last\_triggered\_step](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SecondOrStepTimer#update_last_triggered_step)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.train.SecondOrStepTimer Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================================

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SecondOrStepTimer#methods)
    *   [last\_triggered\_step](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SecondOrStepTimer#last_triggered_step)
        
    *   [reset](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SecondOrStepTimer#reset)
        
    *   [should\_trigger\_for\_step](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SecondOrStepTimer#should_trigger_for_step)
        
    *   [update\_last\_triggered\_step](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SecondOrStepTimer#update_last_triggered_step)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/basic_session_run_hooks.py#L85-L150)

Timer that triggers at most once every N seconds or once every N steps.

tf.compat.v1.train.SecondOrStepTimer(
        every_secs=None, every_steps=None
    )

This symbol is also exported to v2 in tf.estimator namespace. See [https://github.com/tensorflow/estimator/blob/master/tensorflow\_estimator/python/estimator/hooks/basic\_session\_run\_hooks.py](https://github.com/tensorflow/estimator/blob/master/tensorflow_estimator/python/estimator/hooks/basic_session_run_hooks.py)

Methods
-------

### `last_triggered_step`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/basic_session_run_hooks.py#L149-L150)

last_triggered_step()

Returns the last triggered time step or None if never triggered.

### `reset`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/basic_session_run_hooks.py#L105-L107)

reset()

Resets the timer.

### `should_trigger_for_step`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/basic_session_run_hooks.py#L109-L134)

should_trigger_for_step(
        step
    )

Return true if the timer should trigger for the specified step.

|     |     |
| --- | --- |
| Args |     |
| `step` | Training step to trigger on. |

|     |
| --- |
| Returns |     |
| True if the difference between the current time and the time of the last trigger exceeds `every_secs`, or if the difference between the current step and the last triggered step exceeds `every_steps`. False otherwise. |     |

### `update_last_triggered_step`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/basic_session_run_hooks.py#L136-L147)

update_last_triggered_step(
        step
    )

Update the last triggered time and step number.

|     |     |
| --- | --- |
| Args |     |
| `step` | The current step. |

|     |
| --- |
| Returns |     |
| A pair `(elapsed_time, elapsed_steps)`, where `elapsed_time` is the number of seconds between the current trigger and the last one (a float), and `elapsed_steps` is the number of steps between the current trigger and the last one. Both values will be set to `None` on the first trigger. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.