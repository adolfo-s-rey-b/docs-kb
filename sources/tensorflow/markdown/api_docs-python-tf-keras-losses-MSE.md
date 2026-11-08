[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/losses/MSE#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/losses/MSE)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/losses/MSE?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/losses/MSE#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/losses/MSE#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.losses.MSE Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/losses/MSE#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/losses/MSE#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/losses/losses.py#L1752-L1788)

Computes the mean squared error between labels and predictions.

#### View aliases

**Main aliases**

[`tf.keras.losses.mse`](https://www.tensorflow.org/api_docs/python/tf/keras/losses/MSE)
, [`tf.keras.metrics.MSE`](https://www.tensorflow.org/api_docs/python/tf/keras/losses/MSE)
, [`tf.keras.metrics.mse`](https://www.tensorflow.org/api_docs/python/tf/keras/losses/MSE)

tf.keras.losses.MSE(
        y_true, y_pred
    )

#### Formula:

loss = mean(square(y_true - y_pred), axis=-1)

#### Example:

    y_true = np.random.randint(0, 2, size=(2, 3))

|     |     |
| --- | --- |
| Args<br>---- |     |
| `y_true` | Ground truth values with shape = `[batch_size, d0, .. dN]`. |
| `y_pred` | The predicted values with shape = `[batch_size, d0, .. dN]`. |

|     |
| --- |
| Returns<br>------- |     |
| Mean squared error values with shape = `[batch_size, d0, .. dN-1]`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.