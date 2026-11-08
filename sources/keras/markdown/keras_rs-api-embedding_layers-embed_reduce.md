None

[KerasRS](https://keras.io/keras_rs/)

[API documentation](https://keras.io/keras_rs/api/)
 [Embedding Layers](https://keras.io/keras_rs/api/embedding_layers/)
 [Feature Interaction Layers](https://keras.io/keras_rs/api/feature_interaction_layers/)
 [Retrieval Layers](https://keras.io/keras_rs/api/retrieval_layers/)
 [Losses](https://keras.io/keras_rs/api/losses/)
 [Metrics](https://keras.io/keras_rs/api/metrics/)
 [Examples](https://keras.io/keras_rs/examples/)

► [KerasRS](https://keras.io/keras_rs/)
 / [API documentation](https://keras.io/keras_rs/api/)
 / [Embedding Layers](https://keras.io/keras_rs/api/embedding_layers/)
 / EmbedReduce layer

EmbedReduce layer
=================

[\[source\]](https://github.com/keras-team/keras-rs/tree/v0.4.0/keras_rs/src/layers/embedding/embed_reduce.py#L90)

### `EmbedReduce` class

Copied!

`keras_rs.layers.EmbedReduce(     input_dim: int,     output_dim: int,     embeddings_initializer: Union[         str,         keras.src.initializers.initializer.Initializer,         type[keras.src.initializers.initializer.Initializer],         Callable[[Sequence[int | None], str], Any],         Any,     ] = "uniform",     embeddings_regularizer: Union[         str,         keras.src.regularizers.regularizers.Regularizer,         type[keras.src.regularizers.regularizers.Regularizer],         Callable[[Any], Any],         NoneType,     ] = None,     embeddings_constraint: Union[         str,         keras.src.constraints.constraints.Constraint,         type[keras.src.constraints.constraints.Constraint],         Callable[[Any], Any],         NoneType,     ] = None,     mask_zero: bool = False,     weights: Any = None,     combiner: str = "mean",     **kwargs: Any )`

An embedding layer that reduces with a combiner.

This layer embeds inputs and then applies a reduction to combine a set of embeddings into a single embedding. This is typically used to embed a sequence of items as a single embedding.

If the inputs passed to `__call__` are 1D, no reduction is applied. If the inputs are 2D, dimension 1 is reduced using the combiner so that the result is of shape `(batch_size, output_dim`). Inputs of rank 3 and higher are not allowed. Weights can optionally be passed to the `__call__` method to apply weights to different samples before reduction.

This layer supports sparse inputs and ragged inputs with backends that support them. The output after reduction is dense. For ragged inputs, the ragged dimension must be 1 as it is the dimension that is reduced.

**Arguments**

*   **input\_dim**: Integer. Size of the vocabulary, maximum integer index + 1.
*   **output\_dim**: Integer. Dimension of the dense embedding.
*   **embeddings\_initializer**: Initializer for the `embeddings` matrix (see `keras.initializers`).
*   **embeddings\_regularizer**: Regularizer function applied to the `embeddings` matrix (see `keras.regularizers`).
*   **embeddings\_constraint**: Constraint function applied to the `embeddings` matrix (see `keras.constraints`).
*   **mask\_zero**: Boolean, whether or not the input value 0 is a special "padding" value that should be masked out. This is useful when using recurrent layers which may take variable length input. If this is `True`, then all subsequent layers in the model need to support masking or an exception will be raised. If `mask_zero` is set to `True`, as a consequence, index 0 cannot be used in the vocabulary (`input_dim` should equal size of vocabulary + 1).
*   **weights**: Optional floating-point matrix of size `(input_dim, output_dim)`. The initial embeddings values to use.
*   **combiner**: Specifies how to reduce if there are multiple entries in a single row. Currently `mean`, `sqrtn` and `sum` are supported. `mean` is the default. `sqrtn` often achieves good accuracy, in particular with bag-of-words columns.
*   **\*\*kwargs**: Additional keyword arguments passed to `Embedding`.

* * *

[\[source\]](https://github.com/keras-team/keras-rs/tree/v0.4.0/keras_rs/src/layers/embedding/embed_reduce.py#L162)

### `call` method

Copied!

`EmbedReduce.call(inputs: Any, weights: typing.Any | None = None)`

Apply embedding and reduction.

**Arguments**

*   **inputs**: 1D tensor to embed or 2D tensor to embed and reduce.
*   **weights**: Optional tensor of weights to apply before reduction, which can be 1D or 2D and must match for the first dimension of `inputs` (1D case) or match the shape of `inputs` (2D case).

**Returns**

A dense 2D tensor of shape `(batch_size, output_dim)`.

* * *

[EmbedReduce layer](https://keras.io/keras_rs/api/embedding_layers/embed_reduce/#embedreduce-layer)

[`EmbedReduce` class](https://keras.io/keras_rs/api/embedding_layers/embed_reduce/#embedreduce-class)

[`call` method](https://keras.io/keras_rs/api/embedding_layers/embed_reduce/#call-method)