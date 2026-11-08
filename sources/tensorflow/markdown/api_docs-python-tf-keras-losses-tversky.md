[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/losses/tversky#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/losses/tversky)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/losses/tversky?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/losses/tversky#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/losses/tversky#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.losses.tversky Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/losses/tversky#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/losses/tversky#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/losses/losses.py#L2615-L2654)

Computes the Tversky loss value between `y_true` and `y_pred`.

tf.keras.losses.tversky(
        y_true, y_pred, alpha=0.5, beta=0.5, axis=None
    )

This loss function is weighted by the alpha and beta coefficients that penalize false positives and false negatives.

With `alpha=0.5` and `beta=0.5`, the loss value becomes equivalent to Dice Loss.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `y_true` | tensor of true targets. |
| `y_pred` | tensor of predicted targets. |
| `alpha` | coefficient controlling incidence of false positives. |
| `beta` | coefficient controlling incidence of false negatives. |
| `axis` | tuple for which dimensions the loss is calculated. |

|     |
| --- |
| Returns<br>------- |     |
| Tversky loss value. |     |

#### Reference:

*   [Salehi et al., 2017](https://arxiv.org/abs/1706.05721)
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.