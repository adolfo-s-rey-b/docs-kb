[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/errors/UnimplementedError#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/errors/UnimplementedError)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/errors/UnimplementedError?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Ferrors%2FUnimplementedError&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/errors/UnimplementedError#attributes)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

Was this helpful?

tf.errors.UnimplementedError Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/errors/UnimplementedError#attributes)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/errors_impl.py#L437-L451)

Raised when an operation has not been implemented.

Inherits From: [`OpError`](https://www.tensorflow.org/api_docs/python/tf/errors/OpError)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.errors.UnimplementedError`](https://www.tensorflow.org/api_docs/python/tf/errors/UnimplementedError)

tf.errors.UnimplementedError(
        node_def, op, message, *args
    )

Some operations may raise this error when passed otherwise-valid arguments that it does not currently support. For example, running the [`tf.nn.max_pool2d`](https://www.tensorflow.org/api_docs/python/tf/nn/max_pool2d)
 operation would raise this error if pooling was requested on the batch dimension, because this is not yet supported.

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `error_code` | The integer error code that describes the error. |
| `experimental_payloads` | A dictionary describing the details of the error. |
| `message` | The error message that describes the error. |
| `node_def` | The `NodeDef` proto representing the op that failed. |
| `op` | The operation that failed, if known. |

Was this helpful?

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.