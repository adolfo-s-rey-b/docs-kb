[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/random/create_rng_state#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/random/create_rng_state)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/random/create_rng_state?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/random/create_rng_state#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/random/create_rng_state#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.random.create\_rng\_state Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/random/create_rng_state#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/random/create_rng_state#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/stateful_random_ops.py#L174-L195)

Creates a RNG state from an integer or a vector.

#### View aliases

**Main aliases**

[`tf.random.experimental.create_rng_state`](https://www.tensorflow.org/api_docs/python/tf/random/create_rng_state)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.random.create_rng_state`](https://www.tensorflow.org/api_docs/python/tf/random/create_rng_state)
, [`tf.compat.v1.random.experimental.create_rng_state`](https://www.tensorflow.org/api_docs/python/tf/random/create_rng_state)

tf.random.create_rng_state(
        seed, alg
    )

#### Example:

    tf.random.create_rng_state(

|     |     |
| --- | --- |
| Args<br>---- |     |
| `seed` | an integer or 1-D numpy array. |
| `alg` | the RNG algorithm. Can be a string, an `Algorithm` or an integer. |

|     |
| --- |
| Returns<br>------- |     |
| a 1-D numpy array whose size depends on the algorithm. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.