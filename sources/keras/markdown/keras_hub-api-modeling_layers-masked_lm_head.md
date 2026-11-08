None

[KerasHub: Pretrained Models](https://keras.io/keras_hub/)

[Getting started](https://keras.io/keras_hub/getting_started/)
 [Developer guides](https://keras.io/keras_hub/guides/)
 [API documentation](https://keras.io/keras_hub/api/)
 [Modeling API](https://keras.io/keras_hub/api/base_classes/)
 [Model Architectures](https://keras.io/keras_hub/api/models/)
 [Tokenizers](https://keras.io/keras_hub/api/tokenizers/)
 [Preprocessing Layers](https://keras.io/keras_hub/api/preprocessing_layers/)
 [Modeling Layers](https://keras.io/keras_hub/api/modeling_layers/)
 [Samplers](https://keras.io/keras_hub/api/samplers/)
 [Metrics](https://keras.io/keras_hub/api/metrics/)
 [Pretrained models list](https://keras.io/keras_hub/presets/)

► [KerasHub: Pretrained Models](https://keras.io/keras_hub/)
 / [API documentation](https://keras.io/keras_hub/api/)
 / [Modeling Layers](https://keras.io/keras_hub/api/modeling_layers/)
 / MaskedLMHead layer

MaskedLMHead layer
==================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/layers/modeling/masked_lm_head.py#L7)

### `MaskedLMHead` class

Copied!

`keras_hub.layers.MaskedLMHead(     vocabulary_size=None,     token_embedding=None,     intermediate_activation="relu",     activation=None,     layer_norm_epsilon=1e-05,     kernel_initializer="glorot_uniform",     bias_initializer="zeros",     **kwargs )`

Masked Language Model (MaskedLM) head.

This layer takes two inputs:

*   `inputs`: which should be a tensor of encoded tokens with shape `(batch_size, sequence_length, hidden_dim)`.
*   `mask_positions`: which should be a tensor of integer positions to predict with shape `(batch_size, masks_per_sequence)`.

The token encodings should usually be the last output of an encoder model, and mask positions should be the integer positions you would like to predict for the MaskedLM task.

The layer will first gather the token encodings at the mask positions. These gathered tokens will be passed through a dense layer the same size as encoding dimension, then transformed to predictions the same size as the input vocabulary. This layer will produce a single output with shape `(batch_size, masks_per_sequence, vocabulary_size)`, which can be used to compute an MaskedLM loss function.

This layer is often be paired with [`keras_hub.layers.MaskedLMMaskGenerator`](https://keras.io/keras_hub/api/preprocessing_layers/masked_lm_mask_generator#maskedlmmaskgenerator-class)
, which will help prepare inputs for the MaskedLM task.

**Arguments**

*   **vocabulary\_size**: The total size of the vocabulary for predictions.
*   **token\_embedding**: Optional. A [`keras_hub.layers.ReversibleEmbedding`](https://keras.io/keras_hub/api/modeling_layers/reversible_embedding#reversibleembedding-class)
     instance. If passed, the layer will be used to project from the `hidden_dim` of the model to the output `vocabulary_size`.
*   **intermediate\_activation**: The activation function of intermediate dense layer.
*   **activation**: The activation function for the outputs of the layer. Usually either `None` (return logits), or `"softmax"` (return probabilities).
*   **layer\_norm\_epsilon**: float. The epsilon value in layer normalization components. Defaults to `1e-5`.
*   **kernel\_initializer**: string or `keras.initializers` initializer. The kernel initializer for the dense and multiheaded attention layers. Defaults to `"glorot_uniform"`.
*   **bias\_initializer**: string or `keras.initializers` initializer. The bias initializer for the dense and multiheaded attention layers. Defaults to `"zeros"`.
*   **\*\*kwargs**: other keyword arguments passed to `keras.layers.Layer`, including `name`, `trainable`, `dtype` etc.

**Example**

Copied!

``batch_size = 16 vocab_size = 100 hidden_dim = 32 seq_length = 50  # Generate random inputs. token_ids = np.random.randint(vocab_size, size=(batch_size, seq_length)) # Choose random positions as the masked inputs. mask_positions = np.random.randint(seq_length, size=(batch_size, 5))  # Embed tokens in a `hidden_dim` feature space. token_embedding = keras_hub.layers.ReversibleEmbedding(     vocab_size,     hidden_dim, ) hidden_states = token_embedding(token_ids)  preds = keras_hub.layers.MaskedLMHead(     vocabulary_size=vocab_size,     token_embedding=token_embedding,     activation="softmax", )(hidden_states, mask_positions)``

**References**

*   [Press and Wolf, 2016](https://arxiv.org/abs/1608.05859)
    

* * *

[MaskedLMHead layer](https://keras.io/keras_hub/api/modeling_layers/masked_lm_head/#maskedlmhead-layer)

[`MaskedLMHead` class](https://keras.io/keras_hub/api/modeling_layers/masked_lm_head/#maskedlmhead-class)