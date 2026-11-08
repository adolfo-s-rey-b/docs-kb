[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/losses/categorical_generalized_cross_entropy#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/losses/categorical_generalized_cross_entropy)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/losses/categorical_generalized_cross_entropy?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Flosses%2Fcategorical_generalized_cross_entropy&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/losses/categorical_generalized_cross_entropy#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/losses/categorical_generalized_cross_entropy#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.losses.categorical\_generalized\_cross\_entropy Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/losses/categorical_generalized_cross_entropy#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/losses/categorical_generalized_cross_entropy#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/losses/losses.py#L2745-L2793)

Computes the Generalized Cross Entropy loss.

tf.keras.losses.categorical_generalized_cross_entropy(
        y_true, y_pred, q
    )

Generalized Cross Entropy (GCE) is a noise-robust loss function that provides better robustness against noisy labels than standard cross entropy. It generalizes both cross entropy and mean absolute error through the parameter q, where values closer to 1 make the loss more robust to noisy labels.

#### Formula:

loss = (1 - p**q) / q

where `p` is the predicted probability for the true class and `q` is the noise parameter.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `y_true` | Ground truth labels. Expected to contain _integer class indices_ with shape `[batch_size]` or `[batch_size, 1]`. |
| `y_pred` | The predicted class probabilities, with shape `[batch_size, num_classes]`. |
| `q` | Float in range `(0, 1)`. It is the noise parameter. Controls the behavior of the loss:<br><br>*   As `q` approaches 0: Behaves more like cross entropy<br>*   As `q` approaches 1: Behaves more like mean absolute error |

|     |
| --- |
| Returns<br>------- |     |
| GCE loss values with shape `[batch_size]`. |     |

<!-- Tabular view -->
     <table class="responsive fixed orange">
    <colgroup><col width="214px"><col></colgroup>
    <tr><th colspan="2"><h2 class="add-link">References</h2></th></tr>
    <tr class="alt">
    <td colspan="2">
    - [Zhang, Sabuncu, 2018](https://arxiv.org/abs/1805.07836)
    ("Generalized Cross Entropy Loss for Training
      Deep Neural Networks with Noisy Labels")
    </td>
    </tr>
    
    </table>

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.