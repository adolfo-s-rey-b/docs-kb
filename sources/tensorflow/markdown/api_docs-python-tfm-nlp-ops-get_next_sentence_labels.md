[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/nlp/ops/get_next_sentence_labels#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/nlp/ops/get_next_sentence_labels)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/nlp/ops/get_next_sentence_labels?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/ops/get_next_sentence_labels#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/nlp/ops/get_next_sentence_labels#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.nlp.ops.get\_next\_sentence\_labels Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/ops/get_next_sentence_labels#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/nlp/ops/get_next_sentence_labels#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/ops/segment_extractor.py#L164-L210)

Extracts the next sentence label from sentences.

tfm.nlp.ops.get_next_sentence_labels(
        sentences, random_threshold=0.5, random_fn=tf.random.uniform
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `sentences` | A `RaggedTensor` of strings w/ shape \[batch, (num\_sentences)\]. |
| `random_threshold` | (optional) A float threshold between 0 and 1, used to determine whether to extract a random sentence or the immediate next sentence. Higher value favors next sentence. |
| `random_fn` | (optional) An op used to generate random float values. |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| A tuple of (next\_sentence\_or\_random, is\_next\_sentence) where: |     |
| `next_sentence_or_random` | A `Tensor` with shape \[num\_sentences\] that contains either the subsequent sentence of `segment_a` or a randomly injected sentence. |
| `is_next_sentence` | A `Tensor` of bool w/ shape \[num\_sentences\] that contains whether or not `next_sentence_or_random` is truly a subsequent sentence or not. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.