[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/T5TransformerParams#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/T5TransformerParams)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/T5TransformerParams?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/T5TransformerParams#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/T5TransformerParams#methods)
    *   [weight\_initializer](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/T5TransformerParams#weight_initializer)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/T5TransformerParams#__eq__)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/T5TransformerParams#class-variables)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.nlp.models.T5TransformerParams Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/T5TransformerParams#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/T5TransformerParams#methods)
    *   [weight\_initializer](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/T5TransformerParams#weight_initializer)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/T5TransformerParams#__eq__)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/T5TransformerParams#class-variables)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/models/t5.py#L1005-L1034)

Transformer parameters.

tfm.nlp.models.T5TransformerParams(
        num_layers: int,
        d_model: int,
        d_kv: int,
        num_heads: int,
        d_ff: int,
        vocab_size: int,
        target_vocab_size: Optional[int] = None,
        dropout_rate: float = 0.0,
        layer_norm_epsilon: float = 1e-06,
        shared_embedding: bool = False,
        vocab_embeddings_initializer: Optional[Initializer] = None,
        relative_attention_num_buckets: int = 32,
        relative_attention_max_distance: int = 128,
        relative_embeddings_initializer: Optional[Initializer] = None,
        weight_initializer: Optional[Initializer] = tfm.nlp.models.T5TransformerParams.weight_initializer,
        bias_initializer: Optional[Initializer] = None,
        rescale_query: bool = False,
        bidirectional: bool = True,
        ffn_activations: Sequence[str] = tfm.nlp.models.T5TransformerParams.ffn_activations,
        logits_via_embedding: bool = True,
        num_decoder_layers: Optional[int] = None,
        one_hot_embedding: bool = True,
        layer_sharing: bool = False,
        use_shared_relative_position_bias: bool = True,
        return_attention_scores: bool = False
    )

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `num_layers` | Dataclass field |
| `d_model` | Dataclass field |
| `d_kv` | Dataclass field |
| `num_heads` | Dataclass field |
| `d_ff` | Dataclass field |
| `vocab_size` | Dataclass field |
| `target_vocab_size` | Dataclass field |
| `dropout_rate` | Dataclass field |
| `layer_norm_epsilon` | Dataclass field |
| `shared_embedding` | Dataclass field |
| `vocab_embeddings_initializer` | Dataclass field |
| `relative_attention_num_buckets` | Dataclass field |
| `relative_attention_max_distance` | Dataclass field |
| `relative_embeddings_initializer` | Dataclass field |
| `weight_initializer` | Dataclass field |
| `bias_initializer` | Dataclass field |
| `rescale_query` | Dataclass field |
| `bidirectional` | Dataclass field |
| `ffn_activations` | Dataclass field |
| `logits_via_embedding` | Dataclass field |
| `num_decoder_layers` | Dataclass field |
| `one_hot_embedding` | Dataclass field |
| `layer_sharing` | Dataclass field |
| `use_shared_relative_position_bias` | Dataclass field |
| `return_attention_scores` | Dataclass field |

Methods
-------

### `weight_initializer`

weight_initializer(
        dtype=None, **kwargs
    )

He normal initializer.

Also available via the shortcut function [`tf.keras.initializers.he_normal`](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/HeNormal)
.

It draws samples from a truncated normal distribution centered on 0 with `stddev = sqrt(2 / fan_in)` where `fan_in` is the number of input units in the weight tensor.

#### Examples:

    # Standalone usage:

    # Usage in a TF-Keras layer:

|     |     |
| --- | --- |
| Args |     |
| `seed` | A Python integer. Used to make the behavior of the initializer deterministic. Note that a seeded initializer will not produce the same random values across multiple calls, but multiple initializers will produce the same sequence when constructed with the same seed value. |

|     |
| --- |
| References |     |
| *   [He et al., 2015](https://arxiv.org/abs/1502.01852) |     |

### `__eq__`

__eq__(
        other
    )

Return self==value.

|     |     |
| --- | --- |
| Class Variables<br>--------------- |     |
| bias\_initializer | `None` |
| bidirectional | `True` |
| dropout\_rate | `0.0` |
| ffn\_activations | `('relu',)` |
| layer\_norm\_epsilon | `1e-06` |
| layer\_sharing | `False` |
| logits\_via\_embedding | `True` |
| num\_decoder\_layers | `None` |
| one\_hot\_embedding | `True` |
| relative\_attention\_max\_distance | `128` |
| relative\_attention\_num\_buckets | `32` |
| relative\_embeddings\_initializer | `None` |
| rescale\_query | `False` |
| return\_attention\_scores | `False` |
| shared\_embedding | `False` |
| target\_vocab\_size | `None` |
| use\_shared\_relative\_position\_bias | `True` |
| vocab\_embeddings\_initializer | `None` |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.