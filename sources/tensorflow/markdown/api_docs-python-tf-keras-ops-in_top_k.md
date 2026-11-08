[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/in_top_k#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/in_top_k)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/in_top_k?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/in_top_k#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/in_top_k#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.in\_top\_k Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/in_top_k#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/in_top_k#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/math.py#L293-L318)

Checks if the targets are in the top-k predictions.

tf.keras.ops.in_top_k(
        targets, predictions, k
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `targets` | A tensor of true labels. |
| `predictions` | A tensor of predicted labels. |
| `k` | An integer representing the number of predictions to consider. |

|     |
| --- |
| Returns<br>------- |     |
| A boolean tensor of the same shape as `targets`, where each element indicates whether the corresponding target is in the top-k predictions. |     |

#### Example:

    targets = keras.ops.convert_to_tensor([2, 5, 3])

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.