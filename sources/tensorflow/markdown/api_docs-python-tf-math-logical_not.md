[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/math/logical_not#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/math/logical_not)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/math/logical_not?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/math/logical_not#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/logical_not#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/logical_not#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.math.logical\_not Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/math/logical_not#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/logical_not#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/logical_not#returns)
    

Returns the truth value of `NOT x` element-wise.

#### View aliases

**Main aliases**

[`tf.logical_not`](https://www.tensorflow.org/api_docs/python/tf/math/logical_not)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.logical_not`](https://www.tensorflow.org/api_docs/python/tf/math/logical_not)
, [`tf.compat.v1.math.logical_not`](https://www.tensorflow.org/api_docs/python/tf/math/logical_not)

tf.math.logical_not(
        x: Annotated[Any, tf.raw_ops.Any],
        name=None
    ) -> Annotated[Any, tf.raw_ops.Any]

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Private Heavy Hitters](https://www.tensorflow.org/federated/tutorials/private_heavy_hitters) |

#### Example:

    tf.math.logical_not(tf.constant([True, False]))

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | A `Tensor` of type `bool`. A `Tensor` of type `bool`. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` of type `bool`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.