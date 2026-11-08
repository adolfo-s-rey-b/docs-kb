[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/experimental/dispatch_for_binary_elementwise_assert_apis#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/experimental/dispatch_for_binary_elementwise_assert_apis)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/experimental/dispatch_for_binary_elementwise_assert_apis?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fexperimental%2Fdispatch_for_binary_elementwise_assert_apis&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/experimental/dispatch_for_binary_elementwise_assert_apis#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/experimental/dispatch_for_binary_elementwise_assert_apis#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.experimental.dispatch\_for\_binary\_elementwise\_assert\_apis Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/experimental/dispatch_for_binary_elementwise_assert_apis#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/experimental/dispatch_for_binary_elementwise_assert_apis#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/util/dispatch.py#L936-L1002)

Decorator to override default implementation for binary elementwise assert APIs.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.experimental.dispatch_for_binary_elementwise_assert_apis`](https://www.tensorflow.org/api_docs/python/tf/experimental/dispatch_for_binary_elementwise_assert_apis)

tf.experimental.dispatch_for_binary_elementwise_assert_apis(
        x_type, y_type
    )

The decorated function (known as the "elementwise assert handler") overrides the default implementation for any binary elementwise assert API whenever the value for the first two arguments (typically named `x` and `y`) match the specified type annotations. The handler is called with two arguments:

`elementwise_assert_handler(assert_func, x, y)`

Where `x` and `y` are the first two arguments to the binary elementwise assert operation, and `assert_func` is a TensorFlow function that takes two parameters and performs the elementwise assert operation (e.g., [`tf.debugging.assert_equal`](https://www.tensorflow.org/api_docs/python/tf/debugging/assert_equal)
).

The following example shows how this decorator can be used to update all binary elementwise assert operations to handle a `MaskedTensor` type:

    class MaskedTensor(tf.experimental.ExtensionType):

    a = MaskedTensor([1, 1, 1, 1, 1], [True, True, True, True, True])

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x_type` | A type annotation indicating when the api handler should be called. |
| `y_type` | A type annotation indicating when the api handler should be called. |

|     |
| --- |
| Returns<br>------- |     |
| A decorator. |     |

#### Registered APIs

The binary elementwise assert APIs are:

<\>

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.