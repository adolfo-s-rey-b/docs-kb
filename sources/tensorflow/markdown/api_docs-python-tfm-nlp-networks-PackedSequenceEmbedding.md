[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/PackedSequenceEmbedding#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/PackedSequenceEmbedding)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/PackedSequenceEmbedding?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/PackedSequenceEmbedding#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/PackedSequenceEmbedding#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/PackedSequenceEmbedding#call)
        
    *   [get\_embedding\_table](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/PackedSequenceEmbedding#get_embedding_table)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.nlp.networks.PackedSequenceEmbedding Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/PackedSequenceEmbedding#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/PackedSequenceEmbedding#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/PackedSequenceEmbedding#call)
        
    *   [get\_embedding\_table](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/PackedSequenceEmbedding#get_embedding_table)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/networks/packed_sequence_embedding.py#L24-L163)

An embedding network supporting packed sequences and position ids.

tfm.nlp.networks.PackedSequenceEmbedding(
        vocab_size,
        type_vocab_size,
        embedding_width,
        hidden_size,
        max_seq_length,
        initializer,
        dropout_rate,
        use_position_id=False,
        pack_multiple_sequences=False,
        **kwargs
    )

This network implements an embedding layer similar to the one described in "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding" ([https://arxiv.org/abs/1810.04805](https://arxiv.org/abs/1810.04805)
). On top of it, it supports to (1) pack multiple sequences into one sequence and (2) allow additional "position\_ids" as input.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `vocab_size` | The size of the token vocabulary. |
| `type_vocab_size` | The size of the type vocabulary. |
| `embedding_width` | Width of token embeddings. |
| `hidden_size` | The output size for this encoder. |
| `max_seq_length` | The maximum sequence length for this encoder. |
| `initializer` | The initializer for the embedding portion of this encoder. |
| `dropout_rate` | The dropout rate to apply before the encoding layers. |
| `pack_multiple_sequences` | If `True`, we can feed multiple sequences into one sequence for training and inference (they don't impact each other). |
| `use_position_id` | Whether to expect `position_ids` as an input to the network. If False, the `position_ids` will be inferred: (1) when pack\_multiple\_sequences is False, we assume the position ids are `0, 1, 2, ..., seq_length - 1`; (2) when `pack_multiple_sequences` is `True`, there may be multiple sub sequences, and for each sub sequence, its position ids start from 0, 1, 2, ... |

Methods
-------

### `call`

call(
        inputs, training=None, mask=None
    )

Calls the model on new inputs and returns the outputs as tensors.

In this case `call()` just reapplies all ops in the graph to the new inputs (e.g. build a new computational graph from the provided inputs).

|     |     |
| --- | --- |
| Args |     |
| `inputs` | Input tensor, or dict/list/tuple of input tensors. |
| `training` | Boolean or boolean scalar tensor, indicating whether to run the `Network` in training mode or inference mode. |
| `mask` | A mask or list of masks. A mask can be either a boolean tensor or None (no mask). For more details, check the guide [here](https://www.tensorflow.org/guide/keras/masking_and_padding)<br>. |

|     |
| --- |
| Returns |     |
| A tensor if there is a single output, or a list of tensors if there are more than one outputs. |     |

### `get_embedding_table`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/networks/packed_sequence_embedding.py#L155-L156)

get_embedding_table()

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.