[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/T5Transformer#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/T5Transformer)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/T5Transformer?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/T5Transformer#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/T5Transformer#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/T5Transformer#methods)
    *   [create\_variable](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/T5Transformer#create_variable)
        
    *   [decode](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/T5Transformer#decode)
        
    *   [encode](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/T5Transformer#encode)
        
    *   [read\_variable](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/T5Transformer#read_variable)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/T5Transformer#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.nlp.models.T5Transformer Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/T5Transformer#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/T5Transformer#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/T5Transformer#methods)
    *   [create\_variable](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/T5Transformer#create_variable)
        
    *   [decode](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/T5Transformer#decode)
        
    *   [encode](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/T5Transformer#encode)
        
    *   [read\_variable](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/T5Transformer#read_variable)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/T5Transformer#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/models/t5.py#L1379-L1593)

Transformer Encoder+Decoder for sequence to sequence.

tfm.nlp.models.T5Transformer(
        config: tfm.nlp.models.T5TransformerParams,
        compute_dtype: tf.DType = tf.float32,
        **kwargs
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `dtype` | the variable allocation dtype. |
| `name` | a string for the module name. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `checkpoint_items` |     |

Methods
-------

### `create_variable`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/models/t5.py#L52-L59)

create_variable(
        name: Text,
        shape: ShapeLike,
        initializer: Initializer,
        dtype: tf.DType = tf.float32,
        **kwargs
    )

### `decode`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/models/t5.py#L1457-L1539)

decode(
        encoded,
        decoder_target_tokens,
        encoder_input_tokens=None,
        encoder_dense_inputs=None,
        decoder_input_tokens=None,
        encoder_segment_ids=None,
        encoder_dense_segment_ids=None,
        decoder_segment_ids=None,
        decode_position=None,
        cache=None,
        max_decode_len=None,
        decode=False,
        training=False
    ) -> Dict[str, tf.Tensor]

### `encode`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/models/t5.py#L1417-L1455)

encode(
        encoder_input_tokens=None,
        encoder_segment_ids=None,
        encoder_dense_inputs=None,
        encoder_dense_segment_ids=None,
        training=False
    )

### `read_variable`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/models/t5.py#L61-L66)

read_variable(
        variable: tf.Variable, as_dtype: Optional[tf.DType] = None
    )

### `__call__`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/models/t5.py#L1541-L1589)

__call__(
        encoder_input_tokens=None,
        decoder_target_tokens=None,
        encoder_dense_inputs=None,
        encoder_dense_segment_ids=None,
        decoder_input_tokens=None,
        encoder_segment_ids=None,
        decoder_segment_ids=None,
        training=False
    )

Applies Transformer model on the inputs.

|     |     |
| --- | --- |
| Args |     |
| `encoder_input_tokens` | input tokens to the encoder. |
| `decoder_target_tokens` | target tokens to the decoder. |
| `encoder_dense_inputs` | input dense vectors to the encoder. |
| `encoder_dense_segment_ids` | dense input segmentation info for packed |
| `decoder_input_tokens` | input tokens to the decoder, only required for training. |
| `encoder_segment_ids` | input segmentation info for packed examples. examples. |
| `decoder_segment_ids` | target segmentation info for packed examples. |
| `training` | whether it is training pass, affecting dropouts. |

|     |
| --- |
| Returns |     |
| a dictionary of logits/cache. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.