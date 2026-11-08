[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/losses/dice#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/losses/dice)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/losses/dice?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Flosses%2Fdice&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/losses/dice#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/losses/dice#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.losses.dice Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/losses/dice#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/losses/dice#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/losses/losses.py#L2563-L2612)

Computes the Dice loss value between `y_true` and `y_pred`.

tf.keras.losses.dice(
        y_true, y_pred, axis=None
    )

#### Formula:

loss = 1 - (2 * sum(y_true * y_pred)) / (sum(y_true) + sum(y_pred))

|     |     |
| --- | --- |
| Args<br>---- |     |
| `y_true` | tensor of true targets. |
| `y_pred` | tensor of predicted targets. |
| `axis` | tuple for which dimensions the loss is calculated |

|     |
| --- |
| Returns<br>------- |     |
| Dice loss value. |     |

#### Example:

    y_true = [[[[1.0], [1.0]], [[0.0], [0.0]]],\
\
    loss = keras.losses.dice(y_true, y_pred)\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.