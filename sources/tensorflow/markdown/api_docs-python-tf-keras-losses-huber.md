[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/losses/huber#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/losses/huber)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/losses/huber?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/losses/huber#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/losses/huber#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.losses.huber Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/losses/huber#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/losses/huber#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/losses/losses.py#L1961-L2008)

Computes Huber loss value.

#### View aliases

**Main aliases**

[`tf.keras.metrics.huber`](https://www.tensorflow.org/api_docs/python/tf/keras/losses/huber)

tf.keras.losses.huber(
        y_true, y_pred, delta=1.0
    )

#### Formula:

for x in error:
        if abs(x) <= delta:
            loss.append(0.5 * x^2)
        elif abs(x) > delta:
            loss.append(delta * abs(x) - 0.5 * delta^2)
    
    loss = mean(loss, axis=-1)

See: [Huber loss](https://en.wikipedia.org/wiki/Huber_loss)
.

#### Example:

    y_true = [[0, 1], [0, 0]]

|     |     |
| --- | --- |
| Args<br>---- |     |
| `y_true` | tensor of true targets. |
| `y_pred` | tensor of predicted targets. |
| `delta` | A float, the point where the Huber loss function changes from a quadratic to linear. Defaults to `1.0`. |

|     |
| --- |
| Returns<br>------- |     |
| Tensor with one scalar loss entry per sample. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.