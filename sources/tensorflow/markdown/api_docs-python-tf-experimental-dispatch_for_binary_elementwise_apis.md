[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/experimental/dispatch_for_binary_elementwise_apis#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/experimental/dispatch_for_binary_elementwise_apis)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/experimental/dispatch_for_binary_elementwise_apis?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/experimental/dispatch_for_binary_elementwise_apis#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/experimental/dispatch_for_binary_elementwise_apis#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/experimental/dispatch_for_binary_elementwise_apis#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.experimental.dispatch\_for\_binary\_elementwise\_apis Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/experimental/dispatch_for_binary_elementwise_apis#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/experimental/dispatch_for_binary_elementwise_apis#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/experimental/dispatch_for_binary_elementwise_apis#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/util/dispatch.py#L878-L933)

Decorator to override default implementation for binary elementwise APIs.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.experimental.dispatch_for_binary_elementwise_apis`](https://www.tensorflow.org/api_docs/python/tf/experimental/dispatch_for_binary_elementwise_apis)

tf.experimental.dispatch_for_binary_elementwise_apis(
        x_type, y_type
    )

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Extension types](https://www.tensorflow.org/guide/extension_type) |

The decorated function (known as the "elementwise api handler") overrides the default implementation for any binary elementwise API whenever the value for the first two arguments (typically named `x` and `y`) match the specified type annotations. The elementwise api handler is called with two arguments:

`elementwise_api_handler(api_func, x, y)`

Where `x` and `y` are the first two arguments to the elementwise api, and `api_func` is a TensorFlow function that takes two parameters and performs the elementwise operation (e.g., [`tf.add`](https://www.tensorflow.org/api_docs/python/tf/math/add)
).

The following example shows how this decorator can be used to update all binary elementwise operations to handle a `MaskedTensor` type:

    class MaskedTensor(tf.experimental.ExtensionType):

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

The binary elementwise APIs are:

<\>

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.