[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/MobileBertTransformer#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/MobileBertTransformer)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/MobileBertTransformer?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/MobileBertTransformer#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/MobileBertTransformer#raises)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/MobileBertTransformer#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/MobileBertTransformer#call)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.nlp.layers.MobileBertTransformer Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/MobileBertTransformer#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/MobileBertTransformer#raises)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/MobileBertTransformer#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/MobileBertTransformer#call)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/layers/mobile_bert_layers.py#L170-L431)

Transformer block for MobileBERT.

tfm.nlp.layers.MobileBertTransformer(
        hidden_size=512,
        num_attention_heads=4,
        intermediate_size=512,
        intermediate_act_fn='relu',
        hidden_dropout_prob=0.1,
        attention_probs_dropout_prob=0.1,
        intra_bottleneck_size=128,
        use_bottleneck_attention=False,
        key_query_shared_bottleneck=True,
        num_feedforward_networks=4,
        normalization_type='no_norm',
        initializer=tf_keras.initializers.TruncatedNormal(stddev=0.02),
        **kwargs
    )

An implementation of one layer (block) of Transformer with bottleneck and inverted-bottleneck for MobilerBERT.

Original paper for MobileBERT: [https://arxiv.org/pdf/2004.02984.pdf](https://arxiv.org/pdf/2004.02984.pdf)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `hidden_size` | Hidden size for the Transformer input and output tensor. |
| `num_attention_heads` | Number of attention heads in the Transformer. |
| `intermediate_size` | The size of the "intermediate" (a.k.a., feed forward) layer. |
| `intermediate_act_fn` | The non-linear activation function to apply to the output of the intermediate/feed-forward layer. |
| `hidden_dropout_prob` | Dropout probability for the hidden layers. |
| `attention_probs_dropout_prob` | Dropout probability of the attention probabilities. |
| `intra_bottleneck_size` | Size of bottleneck. |
| `use_bottleneck_attention` | Use attention inputs from the bottleneck transformation. If true, the following `key_query_shared_bottleneck` will be ignored. |
| `key_query_shared_bottleneck` | Whether to share linear transformation for keys and queries. |
| `num_feedforward_networks` | Number of stacked feed-forward networks. |
| `normalization_type` | The type of normalization\_type, only `no_norm` and `layer_norm` are supported. `no_norm` represents the element-wise linear transformation for the student model, as suggested by the original MobileBERT paper. `layer_norm` is used for the teacher model. |
| `initializer` | The initializer to use for the embedding weights and linear projection weights. |
| `**kwargs` | keyword arguments. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | A Tensor shape or parameter is invalid. |

Methods
-------

### `call`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/layers/mobile_bert_layers.py#L345-L431)

call(
        input_tensor, attention_mask=None, return_attention_scores=False
    )

Implementes the forward pass.

|     |     |
| --- | --- |
| Args |     |
| `input_tensor` | Float tensor of shape `(batch_size, seq_length, hidden_size)`. |
| `attention_mask` | (optional) int32 tensor of shape `(batch_size, seq_length, seq_length)`, with 1 for positions that can be attended to and 0 in positions that should not be. |
| `return_attention_scores` | If return attention score. |

|     |     |
| --- | --- |
| Returns |     |
| `layer_output` | Float tensor of shape `(batch_size, seq_length, hidden_size)`. |
| `attention_scores` | `Optional`<br><br>Only when return\_attention\_scores is True. |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | A Tensor shape or parameter is invalid. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.