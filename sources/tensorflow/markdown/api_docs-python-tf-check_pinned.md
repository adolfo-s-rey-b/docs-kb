[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/check_pinned#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/check_pinned)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/check_pinned?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/check_pinned#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/check_pinned#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.check\_pinned Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/check_pinned#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/check_pinned#returns)
    

Checks whether a tensor is located in host memory pinned for GPU.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.check_pinned`](https://www.tensorflow.org/api_docs/python/tf/check_pinned)

tf.check_pinned(
        tensor: Annotated[Any, TV_CheckPinned_T], name=None
    ) -> Annotated[Any, TV_CheckPinned_T]

#### When run:

*   Reports an `InvalidArgument` error if `tensor` is not in pinned memory.
*   Reports a `FailedPrecondition` error if not built with CUDA.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `tensor` | A `Tensor`. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor`. Has the same type as `tensor`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.