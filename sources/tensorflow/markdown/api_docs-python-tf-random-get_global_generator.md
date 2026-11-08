[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/random/get_global_generator#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/random/get_global_generator)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/random/get_global_generator?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/random/get_global_generator#used-in-the-notebooks)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/random/get_global_generator#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.random.get\_global\_generator Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/random/get_global_generator#used-in-the-notebooks)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/random/get_global_generator#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/stateful_random_ops.py#L975-L997)

Retrieves the global generator.

#### View aliases

**Main aliases**

[`tf.random.experimental.get_global_generator`](https://www.tensorflow.org/api_docs/python/tf/random/get_global_generator)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.random.experimental.get_global_generator`](https://www.tensorflow.org/api_docs/python/tf/random/get_global_generator)
, [`tf.compat.v1.random.get_global_generator`](https://www.tensorflow.org/api_docs/python/tf/random/get_global_generator)

tf.random.get_global_generator()

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Random number generation](https://www.tensorflow.org/guide/random_numbers) |

This function will create the global generator the first time it is called, and the generator will be placed at the default device at that time, so one needs to be careful when this function is first called. Using a generator placed on a less-ideal device will incur performance regression.

|     |
| --- |
| Returns<br>------- |     |
| The global [`tf.random.Generator`](https://www.tensorflow.org/api_docs/python/tf/random/Generator)<br> object. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.