[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/timestamp#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/timestamp)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/timestamp?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/timestamp#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/timestamp#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/timestamp#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.timestamp Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/timestamp#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/timestamp#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/timestamp#returns)
    

Provides the time since epoch in seconds.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.timestamp`](https://www.tensorflow.org/api_docs/python/tf/timestamp)

tf.timestamp(
        name=None
    ) -> Annotated[Any, _atypes.Float64]

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Random noise generation in TFF](https://www.tensorflow.org/federated/tutorials/random_noise_generation) |

Returns the timestamp as a `float64` for seconds since the Unix epoch.

#### Common usages include:

*   Logging
*   Providing a random number seed
*   Debugging graph execution
*   Generating timing information, mainly through comparison of timestamps

|     |     |
| --- | --- |
| Args<br>---- |     |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` of type `float64`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.