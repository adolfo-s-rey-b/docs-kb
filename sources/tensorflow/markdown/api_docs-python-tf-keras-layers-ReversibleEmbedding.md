[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ReversibleEmbedding#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ReversibleEmbedding)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ReversibleEmbedding?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ReversibleEmbedding#args)
    
*   [Call arguments](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ReversibleEmbedding#call-arguments)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ReversibleEmbedding#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ReversibleEmbedding#methods)
    *   [enable\_lora](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ReversibleEmbedding#enable_lora)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ReversibleEmbedding#from_config)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.layers.ReversibleEmbedding Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ReversibleEmbedding#args)
    
*   [Call arguments](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ReversibleEmbedding#call-arguments)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ReversibleEmbedding#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ReversibleEmbedding#methods)
    *   [enable\_lora](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ReversibleEmbedding#enable_lora)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/ReversibleEmbedding#from_config)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/core/reversible_embedding.py#L16-L541)

An embedding layer which can project backwards to the input dim.

Inherits From: [`Embedding`](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Embedding)
, [`Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
, [`Operation`](https://www.tensorflow.org/api_docs/python/tf/keras/Operation)

tf.keras.layers.ReversibleEmbedding(
        input_dim,
        output_dim,
        tie_weights=True,
        embeddings_initializer='uniform',
        embeddings_regularizer=None,
        embeddings_constraint=None,
        mask_zero=False,
        reverse_dtype=None,
        logit_soft_cap=None,
        **kwargs
    )

This layer is an extension of [`keras.layers.Embedding`](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Embedding)
 for language models. This layer can be called "in reverse" with `reverse=True`, in which case the layer will linearly project from `output_dim` back to `input_dim`.

By default, the reverse projection will use the transpose of the `embeddings` weights to project to `input_dim` (weights are "tied"). If `tie_weights=False`, the model will use a separate, trainable variable for reverse projection.

This layer has no bias terms.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input_dim` | Integer. Size of the vocabulary, i.e. maximum integer index + 1. |
| `output_dim` | Integer. Dimension of the dense embedding. |
| `tie_weights` | Boolean, whether or not the matrix for embedding and the matrix for the `reverse` projection should share the same weights. |
| `embeddings_initializer` | Initializer for the `embeddings` matrix (see [`keras.initializers`](https://www.tensorflow.org/api_docs/python/tf/keras/initializers)<br>). |
| `embeddings_regularizer` | Regularizer function applied to the `embeddings` matrix (see [`keras.regularizers`](https://www.tensorflow.org/api_docs/python/tf/keras/regularizers)<br>). |
| `embeddings_constraint` | Constraint function applied to the `embeddings` matrix (see [`keras.constraints`](https://www.tensorflow.org/api_docs/python/tf/keras/constraints)<br>). |
| `mask_zero` | Boolean, whether or not the input value 0 is a special "padding" value that should be masked out. |
| `reverse_dtype` | The dtype for the reverse projection computation. Defaults to the `compute_dtype` of the layer. |
| `logit_soft_cap` | If `logit_soft_cap` is set and `reverse=True`, the output logits will be scaled by `tanh(logits / logit_soft_cap) * logit_soft_cap`. This narrows the range of output logits and can improve training. |
| `**kwargs` | other keyword arguments passed to [`keras.layers.Embedding`](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Embedding)<br>, including `name`, `trainable`, `dtype` etc. |

|     |     |
| --- | --- |
| Call arguments<br>-------------- |     |
| `inputs` | The tensor inputs to the layer. |
| `reverse` | Boolean. If `True` the layer will perform a linear projection from `output_dim` to `input_dim`, instead of a normal embedding call. Default to `False`. |

#### Example:

batch_size = 16
    vocab_size = 100
    hidden_dim = 32
    seq_length = 50
    
    # Generate random inputs.
    token_ids = np.random.randint(vocab_size, size=(batch_size, seq_length))
    
    embedding = keras.layers.ReversibleEmbedding(vocab_size, hidden_dim)
    # Embed tokens to shape `(batch_size, seq_length, hidden_dim)`.
    hidden_states = embedding(token_ids)
    # Project hidden states to shape `(batch_size, seq_length, vocab_size)`.
    logits = embedding(hidden_states, reverse=True)

#### References:

*   [Vaswani et al., 2017](https://arxiv.org/abs/1706.03762)
    
*   [Press and Wolf, 2016](https://arxiv.org/abs/1608.05859)
    

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `embeddings` |     |
| `input` | Retrieves the input tensor(s) of a symbolic operation.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |
| `output` | Retrieves the output tensor(s) of a layer.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |
| `variable_serialization_spec` | Returns a dict mapping quantization modes to variable names in order.<br><br>This spec is used by `save_own_variables` and `load_own_variables` to determine the correct ordering of variables during serialization for each quantization mode. `None` means no quantization. |

Methods
-------

### `enable_lora`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/core/embedding.py#L214-L259)

enable_lora(
        rank,
        lora_alpha=None,
        a_initializer='he_uniform',
        b_initializer='zeros'
    )

### `from_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/core/embedding.py#L369-L377)

@classmethod

Creates an operation from its config.

This method is the reverse of `get_config`, capable of instantiating the same operation from the config dictionary.

if "dtype" in config and isinstance(config["dtype"], dict):
        policy = dtype_policies.deserialize(config["dtype"])

|     |     |
| --- | --- |
| Args |     |
| `config` | A Python dictionary, typically the output of `get_config`. |

|     |
| --- |
| Returns |     |
| An operation instance. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.