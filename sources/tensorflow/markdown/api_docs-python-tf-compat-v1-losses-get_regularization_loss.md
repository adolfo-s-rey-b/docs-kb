[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/get_regularization_loss#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/get_regularization_loss)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/get_regularization_loss?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Flosses%2Fget_regularization_loss&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/get_regularization_loss#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/get_regularization_loss#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.losses.get\_regularization\_loss Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/get_regularization_loss#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/get_regularization_loss#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/losses/util.py#L216-L231)

Gets the total regularization loss.

tf.compat.v1.losses.get_regularization_loss(
        scope=None, name='total_regularization_loss'
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `scope` | An optional scope name for filtering the losses to return. |
| `name` | The name of the returned tensor. |

|     |
| --- |
| Returns<br>------- |     |
| A scalar regularization loss. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.