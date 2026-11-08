None

[Keras 3 API documentation](https://keras.io/api/)
 [Keras 2 API documentation](https://keras.io/2/api/)

[Models API](https://keras.io/2/api/models/)
 [Layers API](https://keras.io/2/api/layers/)
 [The base Layer class](https://keras.io/2/api/layers/base_layer/)
 [Layer activations](https://keras.io/2/api/layers/activations/)
 [Layer weight initializers](https://keras.io/2/api/layers/initializers/)
 [Layer weight regularizers](https://keras.io/2/api/layers/regularizers/)
 [Layer weight constraints](https://keras.io/2/api/layers/constraints/)
 [Core layers](https://keras.io/2/api/layers/core_layers/)
 [Convolution layers](https://keras.io/2/api/layers/convolution_layers/)
 [Pooling layers](https://keras.io/2/api/layers/pooling_layers/)
 [Recurrent layers](https://keras.io/2/api/layers/recurrent_layers/)
 [Preprocessing layers](https://keras.io/2/api/layers/preprocessing_layers/)
 [Normalization layers](https://keras.io/2/api/layers/normalization_layers/)
 [Regularization layers](https://keras.io/2/api/layers/regularization_layers/)
 [Attention layers](https://keras.io/2/api/layers/attention_layers/)
 [Reshaping layers](https://keras.io/2/api/layers/reshaping_layers/)
 [Merging layers](https://keras.io/2/api/layers/merging_layers/)
 [Activation layers](https://keras.io/2/api/layers/activation_layers/)
 [Callbacks API](https://keras.io/2/api/callbacks/)
 [Optimizers](https://keras.io/2/api/optimizers/)
 [Metrics](https://keras.io/2/api/metrics/)
 [Losses](https://keras.io/2/api/losses/)
 [Data loading](https://keras.io/2/api/data_loading/)
 [Built-in small datasets](https://keras.io/2/api/datasets/)
 [Keras Applications](https://keras.io/2/api/applications/)
 [Mixed precision](https://keras.io/2/api/mixed_precision/)
 [Utilities](https://keras.io/2/api/utils/)

► [Keras 2 API documentation](https://keras.io/2/api/)
 / [Layers API](https://keras.io/2/api/layers/)
 / [Normalization layers](https://keras.io/2/api/layers/normalization_layers/)
 / GroupNormalization layer

GroupNormalization layer
========================

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/layers/normalization/group_normalization.py#L31)

### `GroupNormalization` class

Copied!

`tf_keras.layers.GroupNormalization(     groups=32,     axis=-1,     epsilon=0.001,     center=True,     scale=True,     beta_initializer="zeros",     gamma_initializer="ones",     beta_regularizer=None,     gamma_regularizer=None,     beta_constraint=None,     gamma_constraint=None,     **kwargs )`

Group normalization layer.

Group Normalization divides the channels into groups and computes within each group the mean and variance for normalization. Empirically, its accuracy is more stable than batch norm in a wide range of small batch sizes, if learning rate is adjusted linearly with batch sizes.

Relation to Layer Normalization: If the number of groups is set to 1, then this operation becomes nearly identical to Layer Normalization (see Layer Normalization docs for details).

Relation to Instance Normalization: If the number of groups is set to the input dimension (number of groups is equal to number of channels), then this operation becomes identical to Instance Normalization.

**Arguments**

*   **groups**: Integer, the number of groups for Group Normalization. Can be in the range \[1, N\] where N is the input dimension. The input dimension must be divisible by the number of groups. Defaults to `32`.
*   **axis**: Integer or List/Tuple. The axis or axes to normalize across. Typically, this is the features axis/axes. The left-out axes are typically the batch axis/axes. `-1` is the last dimension in the input. Defaults to `-1`.
*   **epsilon**: Small float added to variance to avoid dividing by zero. Defaults to 1e-3
*   **center**: If True, add offset of `beta` to normalized tensor. If False, `beta` is ignored. Defaults to `True`.
*   **scale**: If True, multiply by `gamma`. If False, `gamma` is not used. When the next layer is linear (also e.g. `nn.relu`), this can be disabled since the scaling will be done by the next layer. Defaults to `True`.
*   **beta\_initializer**: Initializer for the beta weight. Defaults to zeros.
*   **gamma\_initializer**: Initializer for the gamma weight. Defaults to ones.
*   **beta\_regularizer**: Optional regularizer for the beta weight. None by default.
*   **gamma\_regularizer**: Optional regularizer for the gamma weight. None by default.
*   **beta\_constraint**: Optional constraint for the beta weight. None by default.
*   **gamma\_constraint**: Optional constraint for the gamma weight. None by default. # Input shape Arbitrary. Use the keyword argument `input_shape` (tuple of integers, does not include the samples axis) when using this layer as the first layer in a model. # Output shape Same shape as input.

**Call arguments**

*   **inputs**: Input tensor (of any rank).
*   **mask**: The mask parameter is a tensor that indicates the weight for each position in the input tensor when computing the mean and variance.

Reference: - [Yuxin Wu & Kaiming He, 2018](https://arxiv.org/abs/1803.08494)

* * *

[GroupNormalization layer](https://keras.io/2/api/layers/normalization_layers/group_normalization/#groupnormalization-layer)

[`GroupNormalization` class](https://keras.io/2/api/layers/normalization_layers/group_normalization/#groupnormalization-class)