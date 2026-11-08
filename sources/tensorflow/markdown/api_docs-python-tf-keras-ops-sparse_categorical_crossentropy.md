[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/sparse_categorical_crossentropy#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/sparse_categorical_crossentropy)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/sparse_categorical_crossentropy?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/sparse_categorical_crossentropy#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/sparse_categorical_crossentropy#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.sparse\_categorical\_crossentropy Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/sparse_categorical_crossentropy#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/sparse_categorical_crossentropy#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/nn.py#L2166-L2218)

Computes sparse categorical cross-entropy loss.

#### View aliases

**Main aliases**

[`tf.keras.ops.nn.sparse_categorical_crossentropy`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/sparse_categorical_crossentropy)

tf.keras.ops.sparse_categorical_crossentropy(
        target, output, from_logits=False, axis=-1
    )

The sparse categorical cross-entropy loss is similar to categorical cross-entropy, but it is used when the target tensor contains integer class labels instead of one-hot encoded vectors. It measures the dissimilarity between the target and output probabilities or logits.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `target` | The target tensor representing the true class labels as integers. Its shape should match the shape of the `output` tensor except for the last dimension. |
| `output` | The output tensor representing the predicted probabilities or logits. Its shape should match the shape of the `target` tensor except for the last dimension. |
| `from_logits` | (optional) Whether `output` is a tensor of logits or probabilities. Set it to `True` if `output` represents logits; otherwise, set it to `False` if `output` represents probabilities. Defaults to `False`. |
| `axis` | (optional) The axis along which the sparse categorical cross-entropy is computed. Defaults to `-1`, which corresponds to the last dimension of the tensors. |

|     |
| --- |
| Returns<br>------- |     |
| Integer tensor: The computed sparse categorical cross-entropy loss between `target` and `output`. |     |

#### Example:

    target = keras.ops.convert_to_tensor([0, 1, 2], dtype=int32)

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.