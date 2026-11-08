[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/assert_greater_equal#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   English
*   中文 – 简体

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.assert\_greater\_equal Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/check_ops.py#L1005-L1013)

Assert the condition `x >= y` holds element-wise.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.debugging.assert_greater_equal`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/assert_greater_equal)

tf.compat.v1.assert_greater_equal(
        x, y, data=None, summarize=None, message=None, name=None
    )

Migrate to TF2
--------------

[`tf.compat.v1.assert_greater_equal`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/assert_greater_equal)
 is compatible with eager execution and [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
. Please use [`tf.debugging.assert_greater_equal`](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_greater_equal)
 instead when migrating to TF2. Apart from `data`, all arguments are supported with the same argument name.

If you want to ensure the assert statements run before the potentially-invalid computation, please use [`tf.control_dependencies`](https://www.tensorflow.org/api_docs/python/tf/control_dependencies)
, as tf.function auto-control dependencies are insufficient for assert statements.

#### Structural Mapping to Native TF2

Before:

tf.compat.v1.assert_greater_equal(
      x=x, y=y, data=data, summarize=summarize,
      message=message, name=name)

After:

tf.debugging.assert_greater_equal(
      x=x, y=y, message=message,
      summarize=summarize, name=name)

#### TF1 & TF2 Usage Example

TF1:

    g = tf.Graph()

TF2:

    a = tf.Variable([1, 2], dtype=tf.float32)

Description
-----------

This condition holds if for every pair of (possibly broadcast) elements `x[i]`, `y[i]`, we have `x[i] >= y[i]`. If both `x` and `y` are empty, this is trivially satisfied.

When running in graph mode, you should add a dependency on this operation to ensure that it runs. Example of adding a dependency to an operation:

with tf.control_dependencies([tf.compat.v1.assert_greater_equal(x, y)]):
      output = tf.reduce_sum(x)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | Numeric `Tensor`. |
| `y` | Numeric `Tensor`, same dtype as and broadcastable to `x`. |
| `data` | The tensors to print out if the condition is False. Defaults to error message and first few entries of `x`, `y`. |
| `summarize` | Print this many entries of each tensor. |
| `message` | A string to prefix to the default message. |
| `name` | A name for this operation (optional). Defaults to "assert\_greater\_equal". |

|     |
| --- |
| Returns<br>------- |     |
| Op that raises `InvalidArgumentError` if `x >= y` is False. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `InvalidArgumentError` | if the check can be performed immediately and `x >= y` is False. The check can be performed immediately during eager execution or if `x` and `y` are statically known. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.