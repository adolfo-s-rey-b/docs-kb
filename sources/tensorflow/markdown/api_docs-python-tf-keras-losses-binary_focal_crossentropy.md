[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/losses/binary_focal_crossentropy#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/losses/binary_focal_crossentropy)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/losses/binary_focal_crossentropy?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/losses/binary_focal_crossentropy#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/losses/binary_focal_crossentropy#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.losses.binary\_focal\_crossentropy Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/losses/binary_focal_crossentropy#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/losses/binary_focal_crossentropy#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/losses/losses.py#L2420-L2522)

Computes the binary focal crossentropy loss.

#### View aliases

**Main aliases**

[`tf.keras.metrics.binary_focal_crossentropy`](https://www.tensorflow.org/api_docs/python/tf/keras/losses/binary_focal_crossentropy)

tf.keras.losses.binary_focal_crossentropy(
        y_true,
        y_pred,
        apply_class_balancing=False,
        alpha=0.25,
        gamma=2.0,
        from_logits=False,
        label_smoothing=0.0,
        axis=-1
    )

According to [Lin et al., 2018](https://arxiv.org/pdf/1708.02002.pdf)
, it helps to apply a focal factor to down-weight easy examples and focus more on hard examples. By default, the focal tensor is computed as follows:

`focal_factor = (1 - output) ** gamma` for class 1 `focal_factor = output ** gamma` for class 0 where `gamma` is a focusing parameter. When `gamma` = 0, there is no focal effect on the binary crossentropy loss.

If `apply_class_balancing == True`, this function also takes into account a weight balancing factor for the binary classes 0 and 1 as follows:

`weight = alpha` for class 1 (`target == 1`) `weight = 1 - alpha` for class 0 where `alpha` is a float in the range of `[0, 1]`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `y_true` | Ground truth values, of shape `(batch_size, d0, .. dN)`. |
| `y_pred` | The predicted values, of shape `(batch_size, d0, .. dN)`. |
| `apply_class_balancing` | A bool, whether to apply weight balancing on the binary classes 0 and 1. |
| `alpha` | A weight balancing factor for class 1, default is `0.25` as mentioned in the reference. The weight for class 0 is `1.0 - alpha`. |
| `gamma` | A focusing parameter, default is `2.0` as mentioned in the reference. |
| `from_logits` | Whether `y_pred` is expected to be a logits tensor. By default, we assume that `y_pred` encodes a probability distribution. |
| `label_smoothing` | Float in `[0, 1]`. If > `0` then smooth the labels by squeezing them towards 0.5, that is, using `1. - 0.5 * label_smoothing` for the target class and `0.5 * label_smoothing` for the non-target class. |
| `axis` | The axis along which the mean is computed. Defaults to `-1`. |

|     |
| --- |
| Returns<br>------- |     |
| Binary focal crossentropy loss value with shape = `[batch_size, d0, .. dN-1]`. |     |

#### Example:

    y_true = [[0, 1], [0, 0]]

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.