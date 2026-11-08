[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/concordance_correlation#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/concordance_correlation)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/concordance_correlation?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/concordance_correlation#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/concordance_correlation#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.metrics.concordance\_correlation Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/concordance_correlation#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/concordance_correlation#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/metrics/correlation_metrics.py#L48-L92)

Computes the Concordance coefficient between labels and predictions.

tf.keras.metrics.concordance_correlation(
        y_true, y_pred, axis=-1
    )

#### Formula:

loss = mean(
        2 * (y_true - mean(y_true) * (y_pred - mean(y_pred)) / (
            var(y_true) + var(y_pred) + square(mean(y_true) - mean(y_pred))
        )
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `y_true` | Tensor of true targets. |
| `y_pred` | Tensor of predicted targets. |
| `axis` | Axis along which to determine similarity. Defaults to `-1`. |

|     |
| --- |
| Returns<br>------- |     |
| Concordance Correlation Coefficient tensor. |     |

#### Example:

    y_true = [[0, 1, 0.5], [1, 1, 0.2]]

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.