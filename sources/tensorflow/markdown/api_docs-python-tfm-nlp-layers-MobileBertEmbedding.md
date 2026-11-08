[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/MobileBertEmbedding#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/MobileBertEmbedding)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/MobileBertEmbedding?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/MobileBertEmbedding#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/MobileBertEmbedding#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/MobileBertEmbedding#call)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.nlp.layers.MobileBertEmbedding Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/MobileBertEmbedding#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/MobileBertEmbedding#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/MobileBertEmbedding#call)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/layers/mobile_bert_layers.py#L69-L167)

Performs an embedding lookup for MobileBERT.

tfm.nlp.layers.MobileBertEmbedding(
        word_vocab_size,
        word_embed_size,
        type_vocab_size,
        output_embed_size,
        max_sequence_length=512,
        normalization_type='no_norm',
        initializer=tf_keras.initializers.TruncatedNormal(stddev=0.02),
        dropout_rate=0.1,
        **kwargs
    )

This layer includes word embedding, token type embedding, position embedding.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `word_vocab_size` | Number of words in the vocabulary. |
| `word_embed_size` | Word embedding size. |
| `type_vocab_size` | Number of word types. |
| `output_embed_size` | Embedding size for the final embedding output. |
| `max_sequence_length` | Maximum length of input sequence. |
| `normalization_type` | String. The type of normalization\_type, only `no_norm` and `layer_norm` are supported. |
| `initializer` | The initializer to use for the embedding weights and linear projection weights. |
| `dropout_rate` | Dropout rate. |
| `**kwargs` | keyword arguments. |

Methods
-------

### `call`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/layers/mobile_bert_layers.py#L150-L167)

call(
        input_ids, token_type_ids=None
    )

This is where the layer's logic lives.

The `call()` method may not create state (except in its first invocation, wrapping the creation of variables or other resources in [`tf.init_scope()`](https://www.tensorflow.org/api_docs/python/tf/init_scope)
). It is recommended to create state, including [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable)
 instances and nested `Layer` instances, in `__init__()`, or in the `build()` method that is called automatically before `call()` executes for the first time.

|     |     |
| --- | --- |
| Args |     |
| `inputs` | Input tensor, or dict/list/tuple of input tensors. The first positional `inputs` argument is subject to special rules:<br><br>*   `inputs` must be explicitly passed. A layer cannot have zero arguments, and `inputs` cannot be provided via the default value of a keyword argument.<br>*   NumPy array or Python scalar values in `inputs` get cast as tensors.<br>*   TF-Keras mask metadata is only collected from `inputs`.<br>*   Layers are built (`build(input_shape)` method) using shape info from `inputs` only.<br>*   `input_spec` compatibility is only checked against `inputs`.<br>*   Mixed precision input casting is only applied to `inputs`. If a layer has tensor arguments in `*args` or `**kwargs`, their casting behavior in mixed precision should be handled manually.<br>*   The SavedModel input specification is generated using `inputs` only.<br>*   Integration with various ecosystem packages like TFMOT, TFLite, TF.js, etc is only supported for `inputs` and not for tensors in positional and keyword arguments. |
| `*args` | Additional positional arguments. May contain tensors, although this is not recommended, for the reasons above. |
| `**kwargs` | Additional keyword arguments. May contain tensors, although this is not recommended, for the reasons above. The following optional keyword arguments are reserved:*   `training`: Boolean scalar tensor of Python boolean indicating whether the `call` is meant for training or inference.<br>*   `mask`: Boolean input mask. If the layer's `call()` method takes a `mask` argument, its default value will be set to the mask generated for `inputs` by the previous layer (if `input` did come from a layer that generated a corresponding mask, i.e. if it came from a TF-Keras layer with masking support). |

|     |
| --- |
| Returns |     |
| A tensor or list/tuple of tensors. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.