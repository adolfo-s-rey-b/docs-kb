[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/Seq2SeqTransformer#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/Seq2SeqTransformer)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/Seq2SeqTransformer?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/Seq2SeqTransformer#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/Seq2SeqTransformer#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/Seq2SeqTransformer#call)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.nlp.models.Seq2SeqTransformer Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/Seq2SeqTransformer#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/Seq2SeqTransformer#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/Seq2SeqTransformer#call)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/models/seq2seq_transformer.py#L31-L359)

Transformer model with Keras.

tfm.nlp.models.Seq2SeqTransformer(
        vocab_size=33708,
        embedding_width=512,
        dropout_rate=0.0,
        padded_decode=False,
        decode_max_length=None,
        extra_decode_length=0,
        beam_size=4,
        alpha=0.6,
        encoder_layer=None,
        decoder_layer=None,
        eos_id=EOS_ID,
        **kwargs
    )

Implemented as described in: [https://arxiv.org/pdf/1706.03762.pdf](https://arxiv.org/pdf/1706.03762.pdf)

The Transformer model consists of an encoder and decoder. The input is an int sequence (or a batch of sequences). The encoder produces a continuous representation, and the decoder uses the encoder output to generate probabilities for the output sequence.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `vocab_size` | Size of vocabulary. |
| `embedding_width` | Size of hidden layer for embedding. |
| `dropout_rate` | Dropout probability. |
| `padded_decode` | Whether to max\_sequence\_length padding is used. If set False, max\_sequence\_length padding is not used. |
| `decode_max_length` | maximum number of steps to decode a sequence. |
| `extra_decode_length` | Beam search will run extra steps to decode. |
| `beam_size` | Number of beams for beam search |
| `alpha` | The strength of length normalization for beam search. |
| `encoder_layer` | An initialized encoder layer. |
| `decoder_layer` | An initialized decoder layer. |
| `eos_id` | Id of end of sentence token. |
| `**kwargs` | other keyword arguments. |

Methods
-------

### `call`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/models/seq2seq_transformer.py#L149-L296)

call(
        inputs
    )

Calculate target logits or inferred target sequences.

|     |     |
| --- | --- |
| Args |     |
| `inputs` | a dictionary of tensors. Feature `inputs` (optional): int tensor with shape `[batch_size, input_length]`. Feature `embedded_inputs` (optional): float tensor with shape `[batch_size, input_length, embedding_width]`. Feature `targets` (optional): None or int tensor with shape `[batch_size, target_length]`. Feature `input_masks` (optional): When providing the `embedded_inputs`, the dictionary must provide a boolean mask marking the filled time steps. The shape of the tensor is `[batch_size, input_length]`. Either `inputs` or `embedded_inputs` and `input_masks` must be present in the input dictionary. In the second case the projection of the integer tokens to the transformer embedding space is skipped and `input_masks` is expected to be present. |

|     |
| --- |
| Returns |     |
| If targets is defined, then return logits for each word in the target sequence, which is a float tensor with shape `(batch_size, target_length, vocab_size)`. If target is `None`, then generate output sequence one token at a time and returns a dictionary { outputs: `(batch_size, decoded_length)` scores: `(batch_size, 1)`} Even when `float16` is used, the output tensor(s) are always `float32`. |     |

|     |     |
| --- | --- |
| Raises |     |
| `NotImplementedError` | If try to use padded decode method on CPU/GPUs. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.