[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/RegisterGradient#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/RegisterGradient)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/RegisterGradient?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2FRegisterGradient&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/RegisterGradient#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/RegisterGradient#raises)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/RegisterGradient#methods)
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/RegisterGradient#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.RegisterGradient Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/RegisterGradient#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/RegisterGradient#raises)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/RegisterGradient#methods)
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/RegisterGradient#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/ops.py#L1699-L1744)

A decorator for registering the gradient function for an op type.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.RegisterGradient`](https://www.tensorflow.org/api_docs/python/tf/RegisterGradient)

tf.RegisterGradient(
        op_type
    )

This decorator is only used when defining a new op type. For an op with `m` inputs and `n` outputs, the gradient function is a function that takes the original `Operation` and `n` `Tensor` objects (representing the gradients with respect to each output of the op), and returns `m` `Tensor` objects (representing the partial gradients with respect to each input of the op).

For example, assuming that operations of type `"Sub"` take two inputs `x` and `y`, and return a single output `x - y`, the following gradient function would be registered:

@tf.RegisterGradient("Sub")
    def _sub_grad(unused_op, grad):
      return grad, tf.negative(grad)

The decorator argument `op_type` is the string type of an operation. This corresponds to the `OpDef.name` field for the proto that defines the operation.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `op_type` | The string type of an operation. This corresponds to the `OpDef.name` field for the proto that defines the operation. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | If `op_type` is not string. |

Methods
-------

### `__call__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/ops.py#L1741-L1744)

__call__(
        f: _T
    ) -> _T

Registers the function `f` as gradient function for `op_type`.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.