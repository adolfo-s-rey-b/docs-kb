[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/cov#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/cov)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/cov?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Fops%2Fcov&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/cov#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/cov#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.cov Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/cov#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/cov#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/master/keras/src/ops/numpy.py#L10820-L10836)

Estimate the covariance matrix of the variables in `x`.

#### View aliases

**Main aliases**

[`tf.keras.ops.numpy.cov`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/cov)

tf.keras.ops.cov(
        x
    )

The covariance is normalized by `D - 1`, where `D` is the number of observations.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | A 2D tensor of shape `(N, D)`, where N is the number of variables and D is the number of observations. |

|     |
| --- |
| Returns<br>------- |     |
| A tensor of shape `(N, N)` representing the covariance matrix. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-04 UTC.