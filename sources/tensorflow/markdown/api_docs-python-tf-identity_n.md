[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/identity_n#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/identity_n)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/identity_n?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/identity_n#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/identity_n#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.identity\_n Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/identity_n#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/identity_n#returns)
    

Returns a list of tensors with the same shapes and contents as the input

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.identity_n`](https://www.tensorflow.org/api_docs/python/tf/identity_n)

tf.identity_n(
        input, name=None
    )

tensors.

This op can be used to override the gradient for complicated functions. For example, suppose y = f(x) and we wish to apply a custom function g for backprop such that dx = g(dy). In Python,

with tf.get_default_graph().gradient_override_map(
        {'IdentityN': 'OverrideGradientWithG'}):
      y, _ = identity_n([f(x), x])
    
    @tf.RegisterGradient('OverrideGradientWithG')
    def ApplyG(op, dy, _):
      return [None, g(dy)]  # Do not backprop to f(x).

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A list of `Tensor` objects. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A list of `Tensor` objects. Has the same type as `input`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.