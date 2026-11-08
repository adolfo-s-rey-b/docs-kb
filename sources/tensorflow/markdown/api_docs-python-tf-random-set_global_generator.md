[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/random/set_global_generator#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/random/set_global_generator)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/random/set_global_generator?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/random/set_global_generator#args)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.random.set\_global\_generator Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/random/set_global_generator#args)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/stateful_random_ops.py#L1000-L1031)

Replaces the global generator with another `Generator` object.

#### View aliases

**Main aliases**

[`tf.random.experimental.set_global_generator`](https://www.tensorflow.org/api_docs/python/tf/random/set_global_generator)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.random.experimental.set_global_generator`](https://www.tensorflow.org/api_docs/python/tf/random/set_global_generator)
, [`tf.compat.v1.random.set_global_generator`](https://www.tensorflow.org/api_docs/python/tf/random/set_global_generator)

tf.random.set_global_generator(
        generator
    )

This function replaces the global generator with the provided `generator` object. A random number generator utilizes a [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable)
 object to store its state. The user shall be aware of caveats how `set_global_generator` interacts with [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
:

*   tf.function puts restrictions on Variable creation thus one cannot freely create a new random generator instance inside [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
    . To call `set_global_generator` inside [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
    , the generator instance must have already been created eagerly.
*   tf.function captures the Variable during trace-compilation, thus a compiled f.function will not be affected `set_global_generator` as demonstrated by random\_test.py/RandomTest.testResetGlobalGeneratorBadWithDefun .

For most use cases, avoid calling `set_global_generator` after program initialization, and prefer to reset the state of the existing global generator instead, such as,

    rng = tf.random.get_global_generator()

|     |     |
| --- | --- |
| Args<br>---- |     |
| `generator` | the new `Generator` object. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.