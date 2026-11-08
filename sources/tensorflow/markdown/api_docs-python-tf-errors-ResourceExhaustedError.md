[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/errors/ResourceExhaustedError#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/errors/ResourceExhaustedError)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/errors/ResourceExhaustedError?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/errors/ResourceExhaustedError#attributes)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.errors.ResourceExhaustedError Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/errors/ResourceExhaustedError#attributes)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/errors_impl.py#L367-L380)

Raised when some resource has been exhausted while running operation.

Inherits From: [`OpError`](https://www.tensorflow.org/api_docs/python/tf/errors/OpError)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.errors.ResourceExhaustedError`](https://www.tensorflow.org/api_docs/python/tf/errors/ResourceExhaustedError)

tf.errors.ResourceExhaustedError(
        node_def, op, message, *args
    )

For example, this error might be raised if a per-user quota is exhausted, or perhaps the entire file system is out of space. If running into `ResourceExhaustedError` due to out of memory (OOM), try to use smaller batch size or reduce dimension size of model weights.

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `error_code` | The integer error code that describes the error. |
| `experimental_payloads` | A dictionary describing the details of the error. |
| `message` | The error message that describes the error. |
| `node_def` | The `NodeDef` proto representing the op that failed. |
| `op` | The operation that failed, if known. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.