[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/losses/KLD#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/losses/KLD)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/losses/KLD?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/losses/KLD#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/losses/KLD#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.losses.KLD Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/losses/KLD#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/losses/KLD#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/losses/losses.py#L2058-L2106)

Computes Kullback-Leibler divergence loss between `y_true` & `y_pred`.

#### View aliases

**Main aliases**

[`tf.keras.losses.kld`](https://www.tensorflow.org/api_docs/python/tf/keras/losses/KLD)
, [`tf.keras.losses.kullback_leibler_divergence`](https://www.tensorflow.org/api_docs/python/tf/keras/losses/KLD)
, [`tf.keras.metrics.KLD`](https://www.tensorflow.org/api_docs/python/tf/keras/losses/KLD)
, [`tf.keras.metrics.kld`](https://www.tensorflow.org/api_docs/python/tf/keras/losses/KLD)
, [`tf.keras.metrics.kullback_leibler_divergence`](https://www.tensorflow.org/api_docs/python/tf/keras/losses/KLD)

tf.keras.losses.KLD(
        y_true, y_pred
    )

#### Formula:

loss = y_true * log(y_true / y_pred)

`y_true` and `y_pred` are expected to be probability distributions, with values between 0 and 1. They will get clipped to the `[0, 1]` range.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `y_true` | Tensor of true targets. |
| `y_pred` | Tensor of predicted targets. |

|     |
| --- |
| Returns<br>------- |     |
| KL Divergence loss values with shape = `[batch_size, d0, .. dN-1]`. |     |

#### Example:

    y_true = np.random.randint(0, 2, size=(2, 3)).astype(np.float32)

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.