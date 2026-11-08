[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/ctc_loss#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/ctc_loss)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/ctc_loss?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/ctc_loss#args)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.ctc\_loss Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/ctc_loss#args)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/nn.py#L2513-L2541)

CTC (Connectionist Temporal Classification) loss.

#### View aliases

**Main aliases**

[`tf.keras.ops.nn.ctc_loss`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/ctc_loss)

tf.keras.ops.ctc_loss(
        target, output, target_length, output_length, mask_index=0
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `target` | A tensor of shape `(batch_size, max_length)` containing the true labels in integer format. |
| `output` | A tensor of shape `(batch_size, max_length, num_classes)` containing logits (the output of your model). |
| `target_length` | A tensor of shape `(batch_size,)` containing the true label lengths. |
| `output_length` | A tensor of shape `(batch_size,)` containing the output lengths. |
| `mask_index` | The index of the mask character in the vocabulary. Defaults to `0`. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.