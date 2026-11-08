None

[Keras 3 API documentation](https://keras.io/api/)

[Models API](https://keras.io/api/models/)
 [Layers API](https://keras.io/api/layers/)
 [The base Layer class](https://keras.io/api/layers/base_layer/)
 [Layer activations](https://keras.io/api/layers/activations/)
 [Layer weight initializers](https://keras.io/api/layers/initializers/)
 [Layer weight regularizers](https://keras.io/api/layers/regularizers/)
 [Layer weight constraints](https://keras.io/api/layers/constraints/)
 [Core layers](https://keras.io/api/layers/core_layers/)
 [Convolution layers](https://keras.io/api/layers/convolution_layers/)
 [Pooling layers](https://keras.io/api/layers/pooling_layers/)
 [Recurrent layers](https://keras.io/api/layers/recurrent_layers/)
 [Preprocessing layers](https://keras.io/api/layers/preprocessing_layers/)
 [Normalization layers](https://keras.io/api/layers/normalization_layers/)
 [Regularization layers](https://keras.io/api/layers/regularization_layers/)
 [Attention layers](https://keras.io/api/layers/attention_layers/)
 [Reshaping layers](https://keras.io/api/layers/reshaping_layers/)
 [Merging layers](https://keras.io/api/layers/merging_layers/)
 [Activation layers](https://keras.io/api/layers/activation_layers/)
 [Backend-specific layers](https://keras.io/api/layers/backend_specific_layers/)
 [Callbacks API](https://keras.io/api/callbacks/)
 [Ops API](https://keras.io/api/ops/)
 [Optimizers](https://keras.io/api/optimizers/)
 [Metrics](https://keras.io/api/metrics/)
 [Losses](https://keras.io/api/losses/)
 [Data loading](https://keras.io/api/data_loading/)
 [Tree API](https://keras.io/api/tree/)
 [Built-in small datasets](https://keras.io/api/datasets/)
 [Keras Applications](https://keras.io/api/applications/)
 [Mixed precision](https://keras.io/api/mixed_precision/)
 [Multi-device distribution](https://keras.io/api/distribution/)
 [RNG API](https://keras.io/api/random/)
 [Quantizers](https://keras.io/api/quantizers/)
 [Scope](https://keras.io/api/scope/)
 [Rematerialization](https://keras.io/api/rematerialization/)
 [Utilities](https://keras.io/api/utils/)

[Keras 2 API documentation](https://keras.io/2/api/)

► [Keras 3 API documentation](https://keras.io/api/)
 / [Layers API](https://keras.io/api/layers/)
 / [Core layers](https://keras.io/api/layers/core_layers/)
 / Embedding layer

Embedding layer
===============

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/core/embedding.py#L20)

### `Embedding` class

Copied!

`keras.layers.Embedding(     input_dim,     output_dim,     embeddings_initializer="uniform",     embeddings_regularizer=None,     embeddings_constraint=None,     mask_zero=False,     weights=None,     lora_rank=None,     lora_alpha=None,     quantization_config=None,     **kwargs )`

Turns nonnegative integers (indexes) into dense vectors of fixed size.

e.g. `[[4], [20]] -> [[0.25, 0.1], [0.6, -0.2]]`

This layer can only be used on nonnegative integer inputs of a fixed range.

**Example**

Copied!

``>>> model = keras.Sequential() >>> model.add(keras.layers.Embedding(1000, 64)) >>> # The model will take as input an integer matrix of size (batch, >>> # input_length), and the largest integer (i.e. word index) in the input >>> # should be no larger than 999 (vocabulary size). >>> # Now model.output_shape is (None, 10, 64), where `None` is the batch >>> # dimension. >>> input_array = np.random.randint(1000, size=(32, 10)) >>> model.compile('rmsprop', 'mse') >>> output_array = model.predict(input_array) >>> print(output_array.shape) (32, 10, 64)``

**Arguments**

*   **input\_dim**: Integer. Size of the vocabulary, i.e. maximum integer index + 1.
*   **output\_dim**: Integer. Dimension of the dense embedding.
*   **embeddings\_initializer**: Initializer for the `embeddings` matrix (see `keras.initializers`).
*   **embeddings\_regularizer**: Regularizer function applied to the `embeddings` matrix (see `keras.regularizers`).
*   **embeddings\_constraint**: Constraint function applied to the `embeddings` matrix (see `keras.constraints`).
*   **mask\_zero**: Boolean, whether or not the input value 0 is a special "padding" value that should be masked out. This is useful when using recurrent layers which may take variable length input. If this is `True`, then all subsequent layers in the model need to support masking or an exception will be raised. If `mask_zero` is set to `True`, as a consequence, index 0 cannot be used in the vocabulary (`input_dim` should equal size of vocabulary + 1).
*   **weights**: Optional floating-point matrix of size `(input_dim, output_dim)`. The initial embeddings values to use.
*   **lora\_rank**: Optional integer. If set, the layer's forward pass will implement LoRA (Low-Rank Adaptation) with the provided rank. LoRA sets the layer's embeddings matrix to non-trainable and replaces it with a delta over the original matrix, obtained via multiplying two lower-rank trainable matrices. This can be useful to reduce the computation cost of fine-tuning large embedding layers. You can also enable LoRA on an existing `Embedding` layer by calling `layer.enable_lora(rank)`.
*   **lora\_alpha**: Optional integer. If set, this parameter scales the low-rank adaptation delta (computed as the product of two lower-rank trainable matrices) during the forward pass. The delta is scaled by `lora_alpha / lora_rank`, allowing you to fine-tune the strength of the LoRA adjustment independently of `lora_rank`.

**Input shape**

2D tensor with shape: `(batch_size, input_length)`.

**Output shape**

3D tensor with shape: `(batch_size, input_length, output_dim)`.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/core/reversible_embedding.py#L16)

### `ReversibleEmbedding` class

Copied!

`keras.layers.ReversibleEmbedding(     input_dim,     output_dim,     tie_weights=True,     embeddings_initializer="uniform",     embeddings_regularizer=None,     embeddings_constraint=None,     mask_zero=False,     reverse_dtype=None,     logit_soft_cap=None,     **kwargs )`

An embedding layer which can project backwards to the input dim.

This layer is an extension of [`keras.layers.Embedding`](https://keras.io/api/layers/core_layers/embedding#embedding-class)
 for language models. This layer can be called "in reverse" with `reverse=True`, in which case the layer will linearly project from `output_dim` back to `input_dim`.

By default, the reverse projection will use the transpose of the `embeddings` weights to project to `input_dim` (weights are "tied"). If `tie_weights=False`, the model will use a separate, trainable variable for reverse projection.

This layer has no bias terms.

**Arguments**

*   **input\_dim**: Integer. Size of the vocabulary, i.e. maximum integer index + 1.
*   **output\_dim**: Integer. Dimension of the dense embedding.
*   **tie\_weights**: Boolean, whether or not the matrix for embedding and the matrix for the `reverse` projection should share the same weights.
*   **embeddings\_initializer**: Initializer for the `embeddings` matrix (see `keras.initializers`).
*   **embeddings\_regularizer**: Regularizer function applied to the `embeddings` matrix (see `keras.regularizers`).
*   **embeddings\_constraint**: Constraint function applied to the `embeddings` matrix (see `keras.constraints`).
*   **mask\_zero**: Boolean, whether or not the input value 0 is a special "padding" value that should be masked out.
*   **reverse\_dtype**: The dtype for the reverse projection computation. Defaults to the `compute_dtype` of the layer.
*   **logit\_soft\_cap**: If `logit_soft_cap` is set and `reverse=True`, the output logits will be scaled by `tanh(logits / logit_soft_cap) * logit_soft_cap`. This narrows the range of output logits and can improve training.
*   **\*\*kwargs**: other keyword arguments passed to [`keras.layers.Embedding`](https://keras.io/api/layers/core_layers/embedding#embedding-class)
    , including `name`, `trainable`, `dtype` etc.

**Call arguments**

*   **inputs**: The tensor inputs to the layer.
*   **reverse**: Boolean. If `True` the layer will perform a linear projection from `output_dim` to `input_dim`, instead of a normal embedding call. Default to `False`.

**Example**

Copied!

``batch_size = 16 vocab_size = 100 hidden_dim = 32 seq_length = 50  # Generate random inputs. token_ids = np.random.randint(vocab_size, size=(batch_size, seq_length))  embedding = keras.layers.ReversibleEmbedding(vocab_size, hidden_dim) # Embed tokens to shape `(batch_size, seq_length, hidden_dim)`. hidden_states = embedding(token_ids) # Project hidden states to shape `(batch_size, seq_length, vocab_size)`. logits = embedding(hidden_states, reverse=True)``

**References**

*   [Vaswani et al., 2017](https://arxiv.org/abs/1706.03762)
    
*   [Press and Wolf, 2016](https://arxiv.org/abs/1608.05859)
    

* * *

[Embedding layer](https://keras.io/api/layers/core_layers/embedding/#embedding-layer)

[`Embedding` class](https://keras.io/api/layers/core_layers/embedding/#embedding-class)

[`ReversibleEmbedding` class](https://keras.io/api/layers/core_layers/embedding/#reversibleembedding-class)