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
 / GroupNormalization layer

GroupNormalization layer
========================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/normalization/group_normalization.py#L11)

### `GroupNormalization` class

Copied!

`keras.layers.GroupNormalization(     groups=32,     axis=-1,     epsilon=0.001,     center=True,     scale=True,     beta_initializer="zeros",     gamma_initializer="ones",     beta_regularizer=None,     gamma_regularizer=None,     beta_constraint=None,     gamma_constraint=None,     **kwargs )`

Group normalization layer.

Group Normalization divides the channels into groups and computes within each group the mean and variance for normalization. Empirically, its accuracy is more stable than batch norm in a wide range of small batch sizes, if learning rate is adjusted linearly with batch sizes.

Relation to Layer Normalization: If the number of groups is set to 1, then this operation becomes nearly identical to Layer Normalization (see Layer Normalization docs for details).

Relation to Instance Normalization: If the number of groups is set to the input dimension (number of groups is equal to number of channels), then this operation becomes identical to Instance Normalization. You can achieve this via `groups=-1`.

**Arguments**

*   **groups**: Integer, the number of groups for Group Normalization. Can be in the range `[1, N]` where N is the input dimension. The input dimension must be divisible by the number of groups. Defaults to 32.
*   **axis**: Integer or List/Tuple. The axis or axes to normalize across. Typically, this is the features axis/axes. The left-out axes are typically the batch axis/axes. -1 is the last dimension in the input. Defaults to `-1`.
*   **epsilon**: Small float added to variance to avoid dividing by zero. Defaults to 1e-3.
*   **center**: If `True`, add offset of `beta` to normalized tensor. If `False`, `beta` is ignored. Defaults to `True`.
*   **scale**: If `True`, multiply by `gamma`. If `False`, `gamma` is not used. When the next layer is linear (also e.g. `relu`), this can be disabled since the scaling will be done by the next layer. Defaults to `True`.
*   **beta\_initializer**: Initializer for the beta weight. Defaults to zeros.
*   **gamma\_initializer**: Initializer for the gamma weight. Defaults to ones.
*   **beta\_regularizer**: Optional regularizer for the beta weight. None by default.
*   **gamma\_regularizer**: Optional regularizer for the gamma weight. None by default.
*   **beta\_constraint**: Optional constraint for the beta weight. None by default.
*   **gamma\_constraint**: Optional constraint for the gamma weight. None by default. # Input shape Arbitrary. Use the keyword argument `input_shape` (tuple of integers, does not include the samples axis) when using this layer as the first layer in a model. # Output shape Same shape as input.
*   **\*\*kwargs**: Base layer keyword arguments (e.g. `name` and `dtype`).

**Reference**

*   [Yuxin Wu & Kaiming He, 2018](https://arxiv.org/abs/1803.08494)
    

* * *

[GroupNormalization layer](https://keras.io/api/layers/normalization_layers/group_normalization/#groupnormalization-layer)

[`GroupNormalization` class](https://keras.io/api/layers/normalization_layers/group_normalization/#groupnormalization-class)