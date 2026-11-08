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
 / [Normalization layers](https://keras.io/api/layers/normalization_layers/)
 / LayerNormalization layer

LayerNormalization layer
========================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/normalization/layer_normalization.py#L11)

### `LayerNormalization` class

Copied!

`keras.layers.LayerNormalization(     axis=-1,     epsilon=0.001,     center=True,     scale=True,     beta_initializer="zeros",     gamma_initializer="ones",     beta_regularizer=None,     gamma_regularizer=None,     beta_constraint=None,     gamma_constraint=None,     **kwargs )`

Layer normalization layer (Ba et al., 2016).

Normalize the activations of the previous layer for each given example in a batch independently, rather than across a batch like Batch Normalization. i.e. applies a transformation that maintains the mean activation within each example close to 0 and the activation standard deviation close to 1.

If `scale` or `center` are enabled, the layer will scale the normalized outputs by broadcasting them with a trainable variable `gamma`, and center the outputs by broadcasting with a trainable variable `beta`. `gamma` will default to a ones tensor and `beta` will default to a zeros tensor, so that centering and scaling are no-ops before training has begun.

So, with scaling and centering enabled the normalization equations are as follows:

Let the intermediate activations for a mini-batch to be the `inputs`.

For each sample `x_i` in `inputs` with `k` features, we compute the mean and variance of the sample:

Copied!

`mean_i = sum(x_i[j] for j in range(k)) / k var_i = sum((x_i[j] - mean_i) ** 2 for j in range(k)) / k`

and then compute a normalized `x_i_normalized`, including a small factor `epsilon` for numerical stability.

Copied!

`x_i_normalized = (x_i - mean_i) / sqrt(var_i + epsilon)`

And finally `x_i_normalized` is linearly transformed by `gamma` and `beta`, which are learned parameters:

Copied!

`output_i = x_i_normalized * gamma + beta`

`gamma` and `beta` will span the axes of `inputs` specified in `axis`, and this part of the inputs' shape must be fully defined.

For example:

Copied!

`>>> layer = keras.layers.LayerNormalization(axis=[1, 2, 3]) >>> layer.build([5, 20, 30, 40]) >>> print(layer.beta.shape) (20, 30, 40) >>> print(layer.gamma.shape) (20, 30, 40)`

Note that other implementations of layer normalization may choose to define `gamma` and `beta` over a separate set of axes from the axes being normalized across. For example, Group Normalization ([Wu et al. 2018](https://arxiv.org/abs/1803.08494)
) with group size of 1 corresponds to a Layer Normalization that normalizes across height, width, and channel and has `gamma` and `beta` span only the channel dimension. So, this Layer Normalization implementation will not match a Group Normalization layer with group size set to 1.

**Arguments**

*   **axis**: Integer or List/Tuple. The axis or axes to normalize across. Typically, this is the features axis/axes. The left-out axes are typically the batch axis/axes. `-1` is the last dimension in the input. Defaults to `-1`.
*   **epsilon**: Small float added to variance to avoid dividing by zero. Defaults to 1e-3.
*   **center**: If True, add offset of `beta` to normalized tensor. If False, `beta` is ignored. Defaults to `True`.
*   **scale**: If True, multiply by `gamma`. If False, `gamma` is not used. When the next layer is linear (also e.g. `nn.relu`), this can be disabled since the scaling will be done by the next layer. Defaults to `True`.
*   **beta\_initializer**: Initializer for the beta weight. Defaults to zeros.
*   **gamma\_initializer**: Initializer for the gamma weight. Defaults to ones.
*   **beta\_regularizer**: Optional regularizer for the beta weight. None by default.
*   **gamma\_regularizer**: Optional regularizer for the gamma weight. None by default.
*   **beta\_constraint**: Optional constraint for the beta weight. None by default.
*   **gamma\_constraint**: Optional constraint for the gamma weight. None by default.
*   **\*\*kwargs**: Base layer keyword arguments (e.g. `name` and `dtype`).

**Reference**

*   [Lei Ba et al., 2016](https://arxiv.org/abs/1607.06450)
    .

* * *

[LayerNormalization layer](https://keras.io/api/layers/normalization_layers/layer_normalization/#layernormalization-layer)

[`LayerNormalization` class](https://keras.io/api/layers/normalization_layers/layer_normalization/#layernormalization-class)