[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/ctc_decode#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/ctc_decode)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/ctc_decode?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/ctc_decode#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/ctc_decode#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.ctc\_decode Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/ctc_decode#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/ctc_decode#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/nn.py#L2588-L2652)

Decodes the output of a CTC model.

#### View aliases

**Main aliases**

[`tf.keras.ops.nn.ctc_decode`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/ctc_decode)

tf.keras.ops.ctc_decode(
        inputs,
        sequence_lengths,
        strategy='greedy',
        beam_width=100,
        top_paths=1,
        merge_repeated=True,
        mask_index=0
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `inputs` | A tensor of shape `(batch_size, max_length, num_classes)` containing the logits (the output of the model). They should _not_ be normalized via softmax. |
| `sequence_lengths` | A tensor of shape `(batch_size,)` containing the sequence lengths for the batch. |
| `strategy` | A string for the decoding strategy. Supported values are `"greedy"` and `"beam_search"`. |
| `beam_width` | An integer scalar beam width used in beam search. Defaults to 100. |
| `top_paths` | An integer scalar, the number of top paths to return. Defaults to 1. |
| `merge_repeated` | A boolean scalar, whether to merge repeated labels in the output. Defaults to `True`. |
| `mask_index` | An integer scalar, the index of the mask character in the vocabulary. Defaults to `0`. |

|     |
| --- |
| Returns<br>------- |     |
| A tuple containing:<br><br>*   The tensor representing the list of decoded sequences. If `strategy="greedy"`, the shape is `(1, batch_size, max_length)`. If `strategy="beam_search"`, the shape is `(top_paths, batch_size, max_length)`. Note that: `-1` indicates the blank label.<br>*   If `strategy="greedy"`, a tensor of shape `(batch_size, 1)` representing the negative of the sum of the probability logits for each sequence. If `strategy="beam_seatch"`, a tensor of shape `(batch_size, top_paths)` representing the log probability for each sequence. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.