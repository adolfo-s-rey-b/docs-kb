None

[Keras 3 API documentation](https://keras.io/api/)

[Models API](https://keras.io/api/models/)
 [Layers API](https://keras.io/api/layers/)
 [Callbacks API](https://keras.io/api/callbacks/)
 [Ops API](https://keras.io/api/ops/)
 [Optimizers](https://keras.io/api/optimizers/)
 [Metrics](https://keras.io/api/metrics/)
 [Losses](https://keras.io/api/losses/)
 [Probabilistic losses](https://keras.io/api/losses/probabilistic_losses/)
 [Regression losses](https://keras.io/api/losses/regression_losses/)
 [Hinge losses for "maximum-margin" classification](https://keras.io/api/losses/hinge_losses/)
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
 / [Losses](https://keras.io/api/losses/)
 / Hinge losses for "maximum-margin" classification

Hinge losses for "maximum-margin" classification
================================================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/losses/losses.py#L397)

### `Hinge` class

Copied!

`keras.losses.Hinge(reduction="sum_over_batch_size", name="hinge", dtype=None)`

Computes the hinge loss between `y_true` & `y_pred`.

Formula:

Copied!

`loss = maximum(1 - y_true * y_pred, 0)`

`y_true` values are expected to be -1 or 1. If binary (0 or 1) labels are provided we will convert them to -1 or 1.

**Arguments**

*   **reduction**: Type of reduction to apply to the loss. In almost all cases this should be `"sum_over_batch_size"`. Supported options are `"sum"`, `"sum_over_batch_size"`, `"mean"`, `"mean_with_sample_weight"` or `None`. `"sum"` sums the loss, `"sum_over_batch_size"` and `"mean"` sum the loss and divide by the sample size, and `"mean_with_sample_weight"` sums the loss and divides by the sum of the sample weights. `"none"` and `None` perform no aggregation. Defaults to `"sum_over_batch_size"`.
*   **name**: Optional name for the loss instance.
*   **dtype**: The dtype of the loss's computations. Defaults to `None`, which means using `keras.backend.floatx()`. `keras.backend.floatx()` is a `"float32"` unless set to different value (via `keras.backend.set_floatx()`). If a `keras.DTypePolicy` is provided, then the `compute_dtype` will be utilized.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/losses/losses.py#L439)

### `SquaredHinge` class

Copied!

`keras.losses.SquaredHinge(     reduction="sum_over_batch_size", name="squared_hinge", dtype=None )`

Computes the squared hinge loss between `y_true` & `y_pred`.

Formula:

Copied!

`loss = square(maximum(1 - y_true * y_pred, 0))`

`y_true` values are expected to be -1 or 1. If binary (0 or 1) labels are provided we will convert them to -1 or 1.

**Arguments**

*   **reduction**: Type of reduction to apply to the loss. In almost all cases this should be `"sum_over_batch_size"`. Supported options are `"sum"`, `"sum_over_batch_size"`, `"mean"`, `"mean_with_sample_weight"` or `None`. `"sum"` sums the loss, `"sum_over_batch_size"` and `"mean"` sum the loss and divide by the sample size, and `"mean_with_sample_weight"` sums the loss and divides by the sum of the sample weights. `"none"` and `None` perform no aggregation. Defaults to `"sum_over_batch_size"`.
*   **name**: Optional name for the loss instance.
*   **dtype**: The dtype of the loss's computations. Defaults to `None`, which means using `keras.backend.floatx()`. `keras.backend.floatx()` is a `"float32"` unless set to different value (via `keras.backend.set_floatx()`). If a `keras.DTypePolicy` is provided, then the `compute_dtype` will be utilized.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/losses/losses.py#L480)

### `CategoricalHinge` class

Copied!

`keras.losses.CategoricalHinge(     reduction="sum_over_batch_size", name="categorical_hinge", dtype=None )`

Computes the categorical hinge loss between `y_true` & `y_pred`.

Formula:

Copied!

`loss = maximum(neg - pos + 1, 0)`

where `neg=maximum((1-y_true)*y_pred)` and `pos=sum(y_true*y_pred)`

**Arguments**

*   **reduction**: Type of reduction to apply to the loss. In almost all cases this should be `"sum_over_batch_size"`. Supported options are `"sum"`, `"sum_over_batch_size"`, `"mean"`, `"mean_with_sample_weight"` or `None`. `"sum"` sums the loss, `"sum_over_batch_size"` and `"mean"` sum the loss and divide by the sample size, and `"mean_with_sample_weight"` sums the loss and divides by the sum of the sample weights. `"none"` and `None` perform no aggregation. Defaults to `"sum_over_batch_size"`.
*   **name**: Optional name for the loss instance.
*   **dtype**: The dtype of the loss's computations. Defaults to `None`, which means using `keras.backend.floatx()`. `keras.backend.floatx()` is a `"float32"` unless set to different value (via `keras.backend.set_floatx()`). If a `keras.DTypePolicy` is provided, then the `compute_dtype` will be utilized.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/losses/losses.py#L1536)

### `CategoricalGeneralizedCrossEntropy` class

Copied!

`keras.losses.CategoricalGeneralizedCrossEntropy(     q=0.5,     reduction="sum_over_batch_size",     name="categorical_generalized_cross_entropy",     dtype=None, )`

Computes the Generalized Cross Entropy loss between `y_true` & `y_pred`.

Generalized Cross Entropy (GCE) is a noise-robust loss function that provides better robustness against noisy labels than standard cross entropy. It generalizes both cross entropy and mean absolute error through the parameter q, where values closer to 1 make the loss more robust to noisy labels.

Formula:

Copied!

`loss = (1 - p**q) / q`

where `p` is the predicted probability for the true class and `q` is the noise parameter.

**Arguments**

*   **q**: Float in range `(0, 1)`. It is the noise parameter. Controls the behavior of the loss:
    *   As `q` approaches 0: Behaves more like cross entropy
    *   As `q` approaches 1: Behaves more like mean absolute error Defaults to `0.5`
*   **reduction**: Type of reduction to apply to the loss. In almost all cases this should be `"sum_over_batch_size"`. Supported options are `"sum"`, `"sum_over_batch_size"`, `"mean"`, `"mean_with_sample_weight"` or `None`. `"sum"` sums the loss, `"sum_over_batch_size"` and `"mean"` sum the loss and divide by the sample size, and `"mean_with_sample_weight"` sums the loss and divides by the sum of the sample weights. `"none"` and `None` perform no aggregation. Defaults to `"sum_over_batch_size"`.
*   **name**: Optional name for the loss instance.
*   **dtype**: The dtype of the loss's computations. Defaults to `None`, which means using `keras.backend.floatx()`. `keras.backend.floatx()` is a `"float32"` unless set to different value (via `keras.backend.set_floatx()`). If a `keras.DTypePolicy` is provided, then the `compute_dtype` will be utilized.

**Example**

Copied!

`y_true = np.array([0, 1, 0, 1]) y_pred = np.array([[0.7, 0.3], [0.2, 0.8], [0.6, 0.4], [0.4, 0.6]]) keras.losses.CategoricalGeneralizedCrossEntropy()(y_true, y_pred)`

**References**

*   [Zhang, Sabuncu, 2018](https://arxiv.org/abs/1805.07836)
     ("Generalized Cross Entropy Loss for Training Deep Neural Networks with Noisy Labels")

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/losses/losses.py#L1444)

### `Circle` class

Copied!

`keras.losses.Circle(     gamma=80.0,     margin=0.4,     remove_diagonal=True,     reduction="sum_over_batch_size",     name="circle",     dtype=None, )`

Computes Circle Loss between integer labels and L2-normalized embeddings.

This is a metric learning loss designed to minimize within-class distance and maximize between-class distance in a flexible manner by dynamically adjusting the penalty strength based on optimization status of each similarity score.

To use Circle Loss effectively, the model should output embeddings without an activation function (such as a `Dense` layer with `activation=None`) followed by UnitNormalization layer to ensure unit-norm embeddings.

**Arguments**

*   **gamma**: Scaling factor that determines the largest scale of each similarity score. Defaults to `80`.
*   **margin**: The relaxation factor, below this distance, negatives are up weighted and positives are down weighted. Similarly, above this distance negatives are down weighted and positive are up weighted. Defaults to `0.4`.
*   **remove\_diagonal**: Boolean, whether to remove self-similarities from the positive mask. Defaults to `True`.
*   **reduction**: Type of reduction to apply to the loss. In almost all cases this should be `"sum_over_batch_size"`. Supported options are `"sum"`, `"sum_over_batch_size"`, `"mean"`, `"mean_with_sample_weight"` or `None`. `"sum"` sums the loss, `"sum_over_batch_size"` and `"mean"` sum the loss and divide by the sample size, and `"mean_with_sample_weight"` sums the loss and divides by the sum of the sample weights. `"none"` and `None` perform no aggregation. Defaults to `"sum_over_batch_size"`.
*   **name**: Optional name for the loss instance.
*   **dtype**: The dtype of the loss's computations. Defaults to `None`, which means using `keras.backend.floatx()`. `keras.backend.floatx()` is a `"float32"` unless set to different value (via `keras.backend.set_floatx()`). If a `keras.DTypePolicy` is provided, then the `compute_dtype` will be utilized.

**Examples**

Usage with the `compile()` API:

Copied!

`model = models.Sequential([     keras.layers.Input(shape=(224, 224, 3)),     keras.layers.Conv2D(16, (3, 3), activation='relu'),     keras.layers.Flatten(),     keras.layers.Dense(64, activation=None),  # No activation     keras.layers.UnitNormalization()  # L2 normalization ])  model.compile(optimizer="adam", loss=keras.losses.Circle())`

**Reference**

*   [Yifan Sun et al., 2020](https://arxiv.org/abs/2002.10857)
    

* * *

[Hinge losses for "maximum-margin" classification](https://keras.io/api/losses/hinge_losses/#hinge-losses-for-maximummargin-classification)

[`Hinge` class](https://keras.io/api/losses/hinge_losses/#hinge-class)

[`SquaredHinge` class](https://keras.io/api/losses/hinge_losses/#squaredhinge-class)

[`CategoricalHinge` class](https://keras.io/api/losses/hinge_losses/#categoricalhinge-class)

[`CategoricalGeneralizedCrossEntropy` class](https://keras.io/api/losses/hinge_losses/#categoricalgeneralizedcrossentropy-class)

[`Circle` class](https://keras.io/api/losses/hinge_losses/#circle-class)