[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/AlbertEncoder#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/AlbertEncoder)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/AlbertEncoder?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/AlbertEncoder#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/AlbertEncoder#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/AlbertEncoder#call)
        
    *   [get\_embedding\_table](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/AlbertEncoder#get_embedding_table)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.nlp.networks.AlbertEncoder Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/AlbertEncoder#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/AlbertEncoder#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/AlbertEncoder#call)
        
    *   [get\_embedding\_table](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/AlbertEncoder#get_embedding_table)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/networks/albert_encoder.py#L25-L211)

ALBERT ([https://arxiv.org/abs/1810.04805](https://arxiv.org/abs/1810.04805)
) text encoder network.

tfm.nlp.networks.AlbertEncoder(
        vocab_size,
        embedding_width=128,
        hidden_size=768,
        num_layers=12,
        num_attention_heads=12,
        max_sequence_length=512,
        type_vocab_size=16,
        intermediate_size=3072,
        activation=tfm.utils.activations.gelu,
        dropout_rate=0.1,
        attention_dropout_rate=0.1,
        initializer=tf_keras.initializers.TruncatedNormal(stddev=0.02),
        dict_outputs=False,
        **kwargs
    )

This network implements the encoder described in the paper "ALBERT: A Lite BERT for Self-supervised Learning of Language Representations" ([https://arxiv.org/abs/1909.11942](https://arxiv.org/abs/1909.11942)
).

Compared with BERT ([https://arxiv.org/abs/1810.04805](https://arxiv.org/abs/1810.04805)
), ALBERT refactorizes embedding parameters into two smaller matrices and shares parameters across layers.

The default values for this object are taken from the ALBERT-Base implementation described in the paper.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `vocab_size` | The size of the token vocabulary. |
| `embedding_width` | The width of the word embeddings. If the embedding width is not equal to hidden size, embedding parameters will be factorized into two matrices in the shape of `(vocab_size, embedding_width)` and `(embedding_width, hidden_size)`, where `embedding_width` is usually much smaller than `hidden_size`. |
| `hidden_size` | The size of the transformer hidden layers. |
| `num_layers` | The number of transformer layers. |
| `num_attention_heads` | The number of attention heads for each transformer. The hidden size must be divisible by the number of attention heads. |
| `max_sequence_length` | The maximum sequence length that this encoder can consume. If None, max\_sequence\_length uses the value from sequence length. This determines the variable shape for positional embeddings. |
| `type_vocab_size` | The number of types that the 'type\_ids' input can take. |
| `intermediate_size` | The intermediate size for the transformer layers. |
| `activation` | The activation to use for the transformer layers. |
| `dropout_rate` | The dropout rate to use for the transformer layers. |
| `attention_dropout_rate` | The dropout rate to use for the attention layers within the transformer layers. |
| `initializer` | The initialzer to use for all weights in this encoder. |
| `dict_outputs` | Whether to use a dictionary as the model outputs. |

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

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/networks/albert_encoder.py#L203-L204)

get_embedding_table()

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.