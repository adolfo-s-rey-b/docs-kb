[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/nlp/ops/get_sentence_order_labels#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/nlp/ops/get_sentence_order_labels)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/nlp/ops/get_sentence_order_labels?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/ops/get_sentence_order_labels#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/nlp/ops/get_sentence_order_labels#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.nlp.ops.get\_sentence\_order\_labels Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/ops/get_sentence_order_labels#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/nlp/ops/get_sentence_order_labels#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/ops/segment_extractor.py#L75-L161)

Extract segments and labels for sentence order prediction (SOP) task.

tfm.nlp.ops.get_sentence_order_labels(
        sentences,
        random_threshold=0.5,
        random_next_threshold=0.5,
        random_fn=tf.random.uniform
    )

Extracts the segment and labels for the sentence order prediction task defined in "ALBERT: A Lite BERT for Self-Supervised Learning of Language Representations" ([https://arxiv.org/pdf/1909.11942.pdf](https://arxiv.org/pdf/1909.11942.pdf)
)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `sentences` | a `RaggedTensor` of shape \[batch, (num\_sentences)\] with string dtype. |
| `random_threshold` | (optional) A float threshold between 0 and 1, used to determine whether to extract a random, out-of-batch sentence or a succeeding sentence. Higher value favors succeeding sentence. |
| `random_next_threshold` | (optional) A float threshold between 0 and 1, used to determine whether to extract either a random, out-of-batch, or succeeding sentence or a preceding sentence. Higher value favors preceding sentences. |
| `random_fn` | (optional) An op used to generate random float values. |

|     |
| --- |
| Returns<br>------- |     |
| a tuple of (preceding\_or\_random\_next, is\_succeeding\_or\_random) where: preceding\_or\_random\_next: a `RaggedTensor` of strings with the same shape as `sentences` and contains either a preceding, succeeding, or random out-of-batch sentence respective to its counterpart in `sentences` and dependent on its label in `is_preceding_or_random_next`. is\_succeeding\_or\_random: a `RaggedTensor` of bool values with the same shape as `sentences` and is True if it's corresponding sentence in `preceding_or_random_next` is a random or succeeding sentence, False otherwise. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.