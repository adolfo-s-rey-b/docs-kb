[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/nn/l2_loss#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/nn/l2_loss)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/nn/l2_loss?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fnn%2Fl2_loss&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/l2_loss#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/l2_loss#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

Was this helpful?

tf.nn.l2\_loss Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/l2_loss#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/l2_loss#returns)
    

L2 Loss.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.nn.l2_loss`](https://www.tensorflow.org/api_docs/python/tf/nn/l2_loss)

tf.nn.l2_loss(
        t: Annotated[Any, TV_L2Loss_T], name=None
    ) -> Annotated[Any, TV_L2Loss_T]

Computes half the L2 norm of a tensor without the `sqrt`:

output = sum(t ** 2) / 2

|     |     |
| --- | --- |
| Args<br>---- |     |
| `t` | A `Tensor`. Must be one of the following types: `half`, `bfloat16`, `float32`, `float64`. Typically 2-D, but may have any dimensions. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor`. Has the same type as `t`. |     |

Was this helpful?

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.