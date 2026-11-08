[Skip to main content](https://www.tensorflow.org/api_docs/python/tfc/ops/entropy_decode_finalize#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfc/ops/entropy_decode_finalize)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfc/ops/entropy_decode_finalize?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfc/ops/entropy_decode_finalize#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfc/ops/entropy_decode_finalize#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfc.ops.entropy\_decode\_finalize Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfc/ops/entropy_decode_finalize#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfc/ops/entropy_decode_finalize#returns)
    

Finalizes the decoding process.

#### View aliases

**Main aliases**

[`tfc.entropy_decode_finalize`](https://www.tensorflow.org/api_docs/python/tfc/ops/entropy_decode_finalize)

tfc.ops.entropy_decode_finalize(
        handle, name=None
    )

This op performs a _weak_ sanity check, and the

return value may be false if some catastrophic error has happened. This is a quite weak safety device, and one should not rely on this for error detection.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `handle` | A `Tensor` of type `variant`. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` of type `bool`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.