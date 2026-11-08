[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/nn/selu#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/nn/selu)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/nn/selu?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/selu#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/selu#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.nn.selu Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/selu#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/selu#returns)
    

Computes scaled exponential linear: `scale * alpha * (exp(features) - 1)`

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.nn.selu`](https://www.tensorflow.org/api_docs/python/tf/nn/selu)

tf.nn.selu(
        features: Annotated[Any, TV_Selu_T], name=None
    ) -> Annotated[Any, TV_Selu_T]

if < 0, `scale * features` otherwise.

To be used together with `initializer = tf.variance_scaling_initializer(factor=1.0, mode='FAN_IN')`. For correct dropout, use `tf.contrib.nn.alpha_dropout`.

See [Self-Normalizing Neural Networks](https://arxiv.org/abs/1706.02515)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `features` | A `Tensor`. Must be one of the following types: `half`, `bfloat16`, `float32`, `float64`. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor`. Has the same type as `features`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.