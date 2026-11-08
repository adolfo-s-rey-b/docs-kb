[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/debugging/Assert#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/debugging/Assert)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/debugging/Assert?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fdebugging%2FAssert&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/debugging/Assert#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/debugging/Assert#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/debugging/Assert#raises)
    
*   [TF1 compatibility](https://www.tensorflow.org/api_docs/python/tf/debugging/Assert#tf1-compatibility)
    
*   [eager compatibility](https://www.tensorflow.org/api_docs/python/tf/debugging/Assert#eager-compatibility)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.debugging.Assert Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/debugging/Assert#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/debugging/Assert#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/debugging/Assert#raises)
    
*   [TF1 compatibility](https://www.tensorflow.org/api_docs/python/tf/debugging/Assert#tf1-compatibility)
    
*   [eager compatibility](https://www.tensorflow.org/api_docs/python/tf/debugging/Assert#eager-compatibility)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/control_flow_assert.py#L62-L130)

Asserts that the given condition is true.

#### View aliases

**Main aliases**

[`tf.Assert`](https://www.tensorflow.org/api_docs/python/tf/debugging/Assert)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.Assert`](https://www.tensorflow.org/api_docs/python/tf/debugging/Assert)
, [`tf.compat.v1.debugging.Assert`](https://www.tensorflow.org/api_docs/python/tf/debugging/Assert)

tf.debugging.Assert(
        condition, data, summarize=None, name=None
    )

If `condition` evaluates to false, print the list of tensors in `data`. `summarize` determines how many entries of the tensors to print.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `condition` | The condition to evaluate. |
| `data` | The tensors to print out when condition is false. |
| `summarize` | Print this many entries of each tensor. |
| `name` | A name for this operation (optional). |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `assert_op` | An `Operation` that, when executed, raises a [`tf.errors.InvalidArgumentError`](https://www.tensorflow.org/api_docs/python/tf/errors/InvalidArgumentError)<br> if `condition` is not true. |

Raises
------

TF1 compatibility
-----------------

When in TF V1 mode (that is, outside [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
) Assert needs a control dependency on the output to ensure the assertion executes:

# Ensure maximum element of x is smaller or equal to 1
    assert_op = tf.Assert(tf.less_equal(tf.reduce_max(x), 1.), [x])
    with tf.control_dependencies([assert_op]):
      ... code using x ...

eager compatibility
-------------------

returns None

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.