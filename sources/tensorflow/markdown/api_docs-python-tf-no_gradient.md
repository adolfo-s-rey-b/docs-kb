[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/no_gradient#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/no_gradient)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/no_gradient?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/no_gradient#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/no_gradient#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.no\_gradient Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/no_gradient#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/no_gradient#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/ops.py#L1747-L1779)

Specifies that ops of type `op_type` is not differentiable.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.NoGradient`](https://www.tensorflow.org/api_docs/python/tf/no_gradient)
, [`tf.compat.v1.NotDifferentiable`](https://www.tensorflow.org/api_docs/python/tf/no_gradient)
, [`tf.compat.v1.no_gradient`](https://www.tensorflow.org/api_docs/python/tf/no_gradient)

tf.no_gradient(
        op_type: str
    ) -> None

This function should _not_ be used for operations that have a well-defined gradient that is not yet implemented.

This function is only used when defining a new op type. It may be used for ops such as [`tf.size()`](https://www.tensorflow.org/api_docs/python/tf/size)
 that are not differentiable. For example:

tf.no_gradient("Size")

The gradient computed for 'op\_type' will then propagate zeros.

For ops that have a well-defined gradient but are not yet implemented, no declaration should be made, and an error _must_ be thrown if an attempt to request its gradient is made.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `op_type` | The string type of an operation. This corresponds to the `OpDef.name` field for the proto that defines the operation. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | If `op_type` is not a string. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.