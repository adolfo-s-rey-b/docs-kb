[Skip to main content](https://www.tensorflow.org/api_docs/python/orbit/utils/create_global_step#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/orbit/utils/create_global_step)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/orbit/utils/create_global_step?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Returns](https://www.tensorflow.org/api_docs/python/orbit/utils/create_global_step#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

orbit.utils.create\_global\_step Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================

*   On this page
*   [Returns](https://www.tensorflow.org/api_docs/python/orbit/utils/create_global_step#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/orbit/utils/common.py#L22-L44)

Creates a [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable)
 suitable for use as a global step counter.

orbit.utils.create_global_step() -> tf.Variable

Creating and managing a global step variable may be necessary for `AbstractTrainer` subclasses that perform multiple parameter updates per `Controller` "step", or use different optimizers on different steps.

In these cases, an `optimizer.iterations` property generally can't be used directly, since it would correspond to parameter updates instead of iterations in the `Controller`'s training loop. Such use cases should simply call `step.assign_add(1)` at the end of each step.

|     |
| --- |
| Returns<br>------- |     |
| A non-trainable scalar [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable)<br> of dtype [`tf.int64`](https://www.tensorflow.org/api_docs/python/tf#int64)<br>, with only the first replica's value retained when synchronizing across replicas in a distributed setting. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-02-13 UTC.