[Skip to main content](https://www.tensorflow.org/api_docs/python/tfc/ops/lower_bound#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfc/ops/lower_bound)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfc/ops/lower_bound?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftfc%2Fops%2Flower_bound&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfc/ops/lower_bound#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfc/ops/lower_bound#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tfc/ops/lower_bound#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfc.ops.lower\_bound Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfc/ops/lower_bound#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfc/ops/lower_bound#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tfc/ops/lower_bound#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/python/ops/math_ops.py#L92-L154)

Same as [`tf.maximum`](https://www.tensorflow.org/api_docs/python/tf/math/maximum)
, but with helpful gradient for `inputs < bound`.

#### View aliases

**Main aliases**

[`tfc.lower_bound`](https://www.tensorflow.org/api_docs/python/tfc/ops/lower_bound)

tfc.ops.lower_bound(
        inputs,
        bound,
        gradient='identity_if_towards',
        name='lower_bound'
    )

This function behaves just like [`tf.maximum`](https://www.tensorflow.org/api_docs/python/tf/math/maximum)
, but the behavior of the gradient with respect to `inputs` for input values that hit the bound depends on `gradient`:

If set to `'disconnected'`, the returned gradient is zero for values that hit the bound. This is identical to the behavior of [`tf.maximum`](https://www.tensorflow.org/api_docs/python/tf/math/maximum)
.

If set to `'identity'`, the gradient is unconditionally replaced with the identity function (i.e., pretending this function does not exist).

If set to `'identity_if_towards'`, the gradient is replaced with the identity function, but only if applying gradient descent would push the values of `inputs` towards the bound. For gradient values that push away from the bound, the returned gradient is still zero.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `inputs` | Input tensor. |
| `bound` | Lower bound for the input tensor. |
| `gradient` | 'disconnected', 'identity', or 'identity\_if\_towards' (default). |
| `name` | Name for this op. |

|     |
| --- |
| Returns<br>------- |     |
| [`tf.maximum(inputs, bound)`](https://www.tensorflow.org/api_docs/python/tf/math/maximum) |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | for invalid value of `gradient`. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.