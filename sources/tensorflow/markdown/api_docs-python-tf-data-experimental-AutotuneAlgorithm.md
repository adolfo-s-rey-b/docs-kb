[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutotuneAlgorithm#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutotuneAlgorithm)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutotuneAlgorithm?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutotuneAlgorithm#class-variables)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.data.experimental.AutotuneAlgorithm Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================================

*   On this page
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutotuneAlgorithm#class-variables)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/options.py#L30-L85)

Represents the type of autotuning algorithm to use.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.data.experimental.AutotuneAlgorithm`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutotuneAlgorithm)

DEFAULT: The default behavior is implementation specific and may change over time.

HILL\_CLIMB: In each optimization step, this algorithm chooses the optimal parameter and increases its value by 1.

GRADIENT\_DESCENT: In each optimization step, this algorithm updates the parameter values in the optimal direction.

MAX\_PARALLELISM: Similar to HILL\_CLIMB but uses a relaxed stopping condition, allowing the optimization to oversubscribe the CPU.

STAGE\_BASED: In each optimization step, this algorithm chooses the worst bottleneck parameter and increases its value by 1.

|     |     |
| --- | --- |
| Class Variables<br>--------------- |     |
| DEFAULT | `<AutotuneAlgorithm.DEFAULT: 0>` |
| GRADIENT\_DESCENT | `<AutotuneAlgorithm.GRADIENT_DESCENT: 2>` |
| HILL\_CLIMB | `<AutotuneAlgorithm.HILL_CLIMB: 1>` |
| MAX\_PARALLELISM | `<AutotuneAlgorithm.MAX_PARALLELISM: 3>` |
| STAGE\_BASED | `<AutotuneAlgorithm.STAGE_BASED: 4>` |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.