[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/MobileBERTEncoder#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/MobileBERTEncoder)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/MobileBERTEncoder?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/MobileBERTEncoder#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/MobileBERTEncoder#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/MobileBERTEncoder#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/MobileBERTEncoder#call)
        
    *   [get\_embedding\_layer](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/MobileBERTEncoder#get_embedding_layer)
        
    *   [get\_embedding\_table](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/MobileBERTEncoder#get_embedding_table)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.nlp.networks.MobileBERTEncoder Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/MobileBERTEncoder#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/MobileBERTEncoder#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/MobileBERTEncoder#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/MobileBERTEncoder#call)
        
    *   [get\_embedding\_layer](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/MobileBERTEncoder#get_embedding_layer)
        
    *   [get\_embedding\_table](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/MobileBERTEncoder#get_embedding_table)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/networks/mobile_bert_encoder.py#L22-L213)

A Keras functional API implementation for MobileBERT encoder.

tfm.nlp.networks.MobileBERTEncoder(
        word_vocab_size=30522,
        word_embed_size=128,
        type_vocab_size=2,
        max_sequence_length=512,
        num_blocks=24,
        hidden_size=512,
        num_attention_heads=4,
        intermediate_size=512,
        intermediate_act_fn='relu',
        hidden_dropout_prob=0.1,
        attention_probs_dropout_prob=0.1,
        intra_bottleneck_size=128,
        initializer_range=0.02,
        use_bottleneck_attention=False,
        key_query_shared_bottleneck=True,
        num_feedforward_networks=4,
        normalization_type='no_norm',
        classifier_activation=False,
        input_mask_dtype='int32',
        **kwargs
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `word_vocab_size` | Number of words in the vocabulary. |
| `word_embed_size` | Word embedding size. |
| `type_vocab_size` | Number of word types. |
| `max_sequence_length` | Maximum length of input sequence. |
| `num_blocks` | Number of transformer block in the encoder model. |
| `hidden_size` | Hidden size for the transformer block. |
| `num_attention_heads` | Number of attention heads in the transformer block. |
| `intermediate_size` | The size of the "intermediate" (a.k.a., feed forward) layer. |
| `intermediate_act_fn` | The non-linear activation function to apply to the output of the intermediate/feed-forward layer. |
| `hidden_dropout_prob` | Dropout probability for the hidden layers. |
| `attention_probs_dropout_prob` | Dropout probability of the attention probabilities. |
| `intra_bottleneck_size` | Size of bottleneck. |
| `initializer_range` | The stddev of the `truncated_normal_initializer` for initializing all weight matrices. |
| `use_bottleneck_attention` | Use attention inputs from the bottleneck transformation. If true, the following `key_query_shared_bottleneck` will be ignored. |
| `key_query_shared_bottleneck` | Whether to share linear transformation for keys and queries. |
| `num_feedforward_networks` | Number of stacked feed-forward networks. |
| `normalization_type` | The type of normalization\_type, only `no_norm` and `layer_norm` are supported. `no_norm` represents the element-wise linear transformation for the student model, as suggested by the original MobileBERT paper. `layer_norm` is used for the teacher model. |
| `classifier_activation` | If using the tanh activation for the final representation of the `[CLS]` token in fine-tuning. |
| `input_mask_dtype` | The dtype of `input_mask` tensor, which is one of the input tensors of this encoder. Defaults to `int32`. If you want to use [`tf.lite`](https://ai.google.dev/edge/api/tflite/python/edge/api/tflite/python/tf/lite)<br> quantization, which does not support `Cast` op, please set this argument to [`tf.float32`](https://www.tensorflow.org/api_docs/python/tf#float32)<br> and feed `input_mask` tensor with values in `float32` to avoid [`tf.cast`](https://www.tensorflow.org/api_docs/python/tf/cast)<br> in the computation. |
| `**kwargs` | Other keyworded and arguments. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `pooler_layer` | The pooler dense layer after the transformer layers. |
| `transformer_layers` | List of Transformer layers in the encoder. |

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

### `get_embedding_layer`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/networks/mobile_bert_encoder.py#L202-L203)

get_embedding_layer()

### `get_embedding_table`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/networks/mobile_bert_encoder.py#L199-L200)

get_embedding_table()

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.