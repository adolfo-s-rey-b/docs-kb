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
 / [Feature Interaction Layers](https://keras.io/keras_rs/api/feature_interaction_layers/)
 / FeatureCross layer

FeatureCross layer
==================

[\[source\]](https://github.com/keras-team/keras-rs/tree/v0.4.0/keras_rs/src/layers/feature_interaction/feature_cross.py#L11)

### `FeatureCross` class

Copied!

`keras_rs.layers.FeatureCross(     projection_dim: int | None = None,     diag_scale: float | None = 0.0,     use_bias: bool = True,     pre_activation: (         str | keras.src.layers.activations.activation.Activation | None     ) = None,     kernel_initializer: (         str | keras.src.initializers.initializer.Initializer     ) = "glorot_uniform",     bias_initializer: str | keras.src.initializers.initializer.Initializer = "zeros",     kernel_regularizer: (         str | None | keras.src.regularizers.regularizers.Regularizer     ) = None,     bias_regularizer: str | None | keras.src.regularizers.regularizers.Regularizer = None,     **kwargs: Any )`

FeatureCross layer in Deep & Cross Network (DCN).

A layer that creates explicit and bounded-degree feature interactions efficiently. The `call` method accepts two inputs: `x0` contains the original features; the second input `xi` is the output of the previous `FeatureCross` layer in the stack, i.e., the i-th `FeatureCross` layer. For the first `FeatureCross` layer in the stack, `x0 = xi`.

The output is `x_{i+1} = x0 .* (W * x_i + bias + diag_scale * x_i) + x_i`, where .\* denotes element-wise multiplication. W could be a full-rank matrix, or a low-rank matrix `U*V` to reduce the computational cost, and `diag_scale` increases the diagonal of W to improve training stability ( especially for the low-rank case).

**Arguments**

*   **projection\_dim**: int. Dimension for down-projecting the input to reduce computational cost. If `None` (default), the full matrix, `W` (with shape `(input_dim, input_dim)`) is used. Otherwise, a low-rank matrix `W = U*V` will be used, where `U` is of shape `(input_dim, projection_dim)` and `V` is of shape `(projection_dim, input_dim)`. `projection_dim` need to be smaller than `input_dim//2` to improve the model efficiency. In practice, we've observed that `projection_dim = input_dim//4` consistently preserved the accuracy of a full-rank version.
*   **diag\_scale**: non-negative float. Used to increase the diagonal of the kernel W by `diag_scale`, i.e., `W + diag_scale * I`, where I is the identity matrix. Defaults to `None`.
*   **use\_bias**: bool. Whether to add a bias term for this layer. Defaults to `True`.
*   **pre\_activation**: string or `keras.activations`. Activation applied to output matrix of the layer, before multiplication with the input. Can be used to control the scale of the layer's outputs and improve stability. Defaults to `None`.
*   **kernel\_initializer**: string or `keras.initializers` initializer. Initializer to use for the kernel matrix. Defaults to `"glorot_uniform"`.
*   **bias\_initializer**: string or `keras.initializers` initializer. Initializer to use for the bias vector. Defaults to `"ones"`.
*   **kernel\_regularizer**: string or `keras.regularizer` regularizer. Regularizer to use for the kernel matrix.
*   **bias\_regularizer**: string or `keras.regularizer` regularizer. Regularizer to use for the bias vector.
*   **\*\*kwargs**: Args to pass to the base class.

**Example**

Copied!

`# 1. Simple forward pass batch_size = 2 embedding_dim = 32 feature1 = np.random.randn(batch_size, embedding_dim) feature2 = np.random.randn(batch_size, embedding_dim) crossed_features = keras_rs.layers.FeatureCross()(feature1, feature2)  # 2. After embedding layer in a model vocabulary_size = 32 embedding_dim = 6  # Create a simple model containing the layer. inputs = keras.Input(shape=(), name='indices', dtype="int32") x0 = keras.layers.Embedding(     input_dim=vocabulary_size,     output_dim=embedding_dim )(inputs) x1 = keras_rs.layers.FeatureCross()(x0, x0) x2 = keras_rs.layers.FeatureCross()(x0, x1) logits = keras.layers.Dense(units=10)(x2) model = keras.Model(inputs, logits)  # Call the model on the inputs. batch_size = 2 input_data = np.random.randint(0, vocabulary_size, size=(batch_size,)) outputs = model(input_data)`

**References**

*   [R. Wang et al.](https://arxiv.org/abs/2008.13535)
    
*   [R. Wang et al.](https://arxiv.org/abs/1708.05123)
    

* * *

[\[source\]](https://github.com/keras-team/keras-rs/tree/v0.4.0/keras_rs/src/layers/feature_interaction/feature_cross.py#L155)

### `call` method

Copied!

`FeatureCross.call(x0: Any, x: typing.Any | None = None)`

Forward pass of the cross layer.

**Arguments**

*   **x0**: a Tensor. The input to the cross layer. N-rank tensor with shape `(batch_size, ..., input_dim)`.
*   **x**: a Tensor. Optional. If provided, the layer will compute crosses between x0 and x. Otherwise, the layer will compute crosses between x0 and itself. Should have the same shape as `x0`.

**Returns**

Tensor of crosses, with the same shape as `x0`.

* * *

[FeatureCross layer](https://keras.io/keras_rs/api/feature_interaction_layers/feature_cross/#featurecross-layer)

[`FeatureCross` class](https://keras.io/keras_rs/api/feature_interaction_layers/feature_cross/#featurecross-class)

[`call` method](https://keras.io/keras_rs/api/feature_interaction_layers/feature_cross/#call-method)