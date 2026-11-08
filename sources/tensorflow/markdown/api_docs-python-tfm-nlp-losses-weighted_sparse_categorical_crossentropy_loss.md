[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/nlp/losses/weighted_sparse_categorical_crossentropy_loss#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/nlp/losses/weighted_sparse_categorical_crossentropy_loss)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/nlp/losses/weighted_sparse_categorical_crossentropy_loss?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/nlp/losses/weighted_sparse_categorical_crossentropy_loss#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tfm/nlp/losses/weighted_sparse_categorical_crossentropy_loss#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.nlp.losses.weighted\_sparse\_categorical\_crossentropy\_loss Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================================================

*   On this page
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/nlp/losses/weighted_sparse_categorical_crossentropy_loss#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tfm/nlp/losses/weighted_sparse_categorical_crossentropy_loss#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/losses/weighted_sparse_categorical_crossentropy.py#L41-L71)

Calculate a per-batch sparse categorical crossentropy loss.

tfm.nlp.losses.weighted_sparse_categorical_crossentropy_loss(
        labels, predictions, weights=None, from_logits=False
    )

This loss function assumes that the predictions are post-softmax. Args: labels: The labels to evaluate against. Should be a set of integer indices ranging from 0 to (vocab\_size-1). predictions: The network predictions. Should have softmax already applied. weights: An optional weight array of the same shape as the 'labels' array. If None, all examples will be used. from\_logits: Whether the input predictions are logits.

|     |
| --- |
| Returns<br>------- |     |
| A loss scalar. |     |

|     |
| --- |
| Raises<br>------ |     |
| RuntimeError if the passed tensors do not have the same rank. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.