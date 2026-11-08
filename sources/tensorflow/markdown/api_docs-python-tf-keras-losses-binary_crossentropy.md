[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/losses/binary_crossentropy#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/losses/binary_crossentropy)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/losses/binary_crossentropy?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/losses/binary_crossentropy#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/losses/binary_crossentropy#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/losses/binary_crossentropy#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.losses.binary\_crossentropy Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/losses/binary_crossentropy#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/losses/binary_crossentropy#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/losses/binary_crossentropy#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/losses/losses.py#L2374-L2417)

Computes the binary crossentropy loss.

#### View aliases

**Main aliases**

[`tf.keras.metrics.binary_crossentropy`](https://www.tensorflow.org/api_docs/python/tf/keras/losses/binary_crossentropy)

tf.keras.losses.binary_crossentropy(
        y_true, y_pred, from_logits=False, label_smoothing=0.0, axis=-1
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Wiki Talk Comments Toxicity Prediction](https://www.tensorflow.org/responsible_ai/fairness_indicators/tutorials/Fairness_Indicators_TFCO_Wiki_Case_Study) |

|     |     |
| --- | --- |
| Args<br>---- |     |
| `y_true` | Ground truth values. shape = `[batch_size, d0, .. dN]`. |
| `y_pred` | The predicted values. shape = `[batch_size, d0, .. dN]`. |
| `from_logits` | Whether `y_pred` is expected to be a logits tensor. By default, we assume that `y_pred` encodes a probability distribution. |
| `label_smoothing` | Float in `[0, 1]`. If > `0` then smooth the labels by squeezing them towards 0.5, that is, using `1. - 0.5 * label_smoothing` for the target class and `0.5 * label_smoothing` for the non-target class. |
| `axis` | The axis along which the mean is computed. Defaults to `-1`. |

|     |
| --- |
| Returns<br>------- |     |
| Binary crossentropy loss value. shape = `[batch_size, d0, .. dN-1]`. |     |

#### Example:

    y_true = [[0, 1], [0, 0]]

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.