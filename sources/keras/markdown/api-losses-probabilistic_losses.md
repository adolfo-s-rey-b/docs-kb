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
 / Probabilistic losses

Probabilistic losses
====================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/losses/losses.py#L601)

### `BinaryCrossentropy` class

Copied!

`keras.losses.BinaryCrossentropy(     from_logits=False,     label_smoothing=0.0,     axis=-1,     reduction="sum_over_batch_size",     name="binary_crossentropy",     dtype=None, )`

Computes the cross-entropy loss between true labels and predicted labels.

Use this cross-entropy loss for binary (0 or 1) classification applications. The loss function requires the following inputs:

*   `y_true` (true label): This is either 0 or 1.
*   `y_pred` (predicted value): This is the model's prediction, i.e, a single floating-point value which either represents a [logit](https://en.wikipedia.org/wiki/Logit)
    , (i.e, value in \[-inf, inf\] when `from_logits=True`) or a probability (i.e, value in \[0., 1.\] when `from_logits=False`).

**Arguments**

*   **from\_logits**: Whether to interpret `y_pred` as a tensor of [logit](https://en.wikipedia.org/wiki/Logit)
     values. By default, we assume that `y_pred` is probabilities (i.e., values in \[0, 1\]).
*   **label\_smoothing**: Float in range \[0, 1\]. When 0, no smoothing occurs. When > 0, we compute the loss between the predicted labels and a smoothed version of the true labels, where the smoothing squeezes the labels towards 0.5. Larger values of `label_smoothing` correspond to heavier smoothing.
*   **axis**: The axis along which to compute crossentropy (the features axis). Defaults to `-1`.
*   **reduction**: Type of reduction to apply to the loss. In almost all cases this should be `"sum_over_batch_size"`. Supported options are `"sum"`, `"sum_over_batch_size"`, `"mean"`, `"mean_with_sample_weight"` or `None`. `"sum"` sums the loss, `"sum_over_batch_size"` and `"mean"` sum the loss and divide by the sample size, and `"mean_with_sample_weight"` sums the loss and divides by the sum of the sample weights. `"none"` and `None` perform no aggregation. Defaults to `"sum_over_batch_size"`.
*   **name**: Optional name for the loss instance.
*   **dtype**: The dtype of the loss's computations. Defaults to `None`, which means using `keras.backend.floatx()`. `keras.backend.floatx()` is a `"float32"` unless set to different value (via `keras.backend.set_floatx()`). If a `keras.DTypePolicy` is provided, then the `compute_dtype` will be utilized.

**Examples**

**Recommended Usage:** (set `from_logits=True`)

With `compile()` API:

Copied!

`model.compile(     loss=keras.losses.BinaryCrossentropy(from_logits=True),     ... )`

As a standalone function:

Copied!

`>>> # Example 1: (batch_size = 1, number of samples = 4) >>> y_true = np.array([0, 1, 0, 0]) >>> y_pred = np.array([-18.6, 0.51, 2.94, -12.8]) >>> bce = keras.losses.BinaryCrossentropy(from_logits=True) >>> bce(y_true, y_pred) 0.8654`

Copied!

``>>> # Example 2: (batch_size = 2, number of samples = 4) >>> y_true = np.array([[0, 1], [0, 0]]) >>> y_pred = np.array([[-18.6, 0.51], [2.94, -12.8]]) >>> # Using default 'auto'/'sum_over_batch_size' reduction type. >>> bce = keras.losses.BinaryCrossentropy(from_logits=True) >>> bce(y_true, y_pred) 0.8654 >>> # Using 'sample_weight' attribute >>> bce(y_true, y_pred, sample_weight=[0.8, 0.2]) 0.243 >>> # Using 'sum' reduction` type. >>> bce = keras.losses.BinaryCrossentropy(from_logits=True, ...     reduction="sum") >>> bce(y_true, y_pred) 1.730 >>> # Using 'none' reduction type. >>> bce = keras.losses.BinaryCrossentropy(from_logits=True, ...     reduction=None) >>> bce(y_true, y_pred) array([0.235, 1.496], dtype=float32)``

**Default Usage:** (set `from_logits=False`)

Copied!

``>>> # Make the following updates to the above "Recommended Usage" section >>> # 1. Set `from_logits=False` >>> keras.losses.BinaryCrossentropy() # OR ...('from_logits=False') >>> # 2. Update `y_pred` to use probabilities instead of logits >>> y_pred = [0.6, 0.3, 0.2, 0.8] # OR [[0.6, 0.3], [0.2, 0.8]]``

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/losses/losses.py#L727)

### `BinaryFocalCrossentropy` class

Copied!

`keras.losses.BinaryFocalCrossentropy(     apply_class_balancing=False,     alpha=0.25,     gamma=2.0,     from_logits=False,     label_smoothing=0.0,     axis=-1,     reduction="sum_over_batch_size",     name="binary_focal_crossentropy",     dtype=None, )`

Computes focal cross-entropy loss between true labels and predictions.

Binary cross-entropy loss is often used for binary (0 or 1) classification tasks. The loss function requires the following inputs:

*   `y_true` (true label): This is either 0 or 1.
*   `y_pred` (predicted value): This is the model's prediction, i.e, a single floating-point value which either represents a [logit](https://en.wikipedia.org/wiki/Logit)
    , (i.e, value in \[-inf, inf\] when `from_logits=True`) or a probability (i.e, value in `[0., 1.]` when `from_logits=False`).

According to [Lin et al., 2018](https://arxiv.org/pdf/1708.02002.pdf)
, it helps to apply a "focal factor" to down-weight easy examples and focus more on hard examples. By default, the focal tensor is computed as follows:

`focal_factor = (1 - output) ** gamma` for class 1 `focal_factor = output ** gamma` for class 0 where `gamma` is a focusing parameter. When `gamma=0`, this function is equivalent to the binary crossentropy loss.

**Arguments**

*   **apply\_class\_balancing**: A bool, whether to apply weight balancing on the binary classes 0 and 1.
*   **alpha**: A weight balancing factor for class 1, default is `0.25` as mentioned in reference [Lin et al., 2018](https://arxiv.org/pdf/1708.02002.pdf)
    . The weight for class 0 is `1.0 - alpha`.
*   **gamma**: A focusing parameter used to compute the focal factor, default is `2.0` as mentioned in the reference [Lin et al., 2018](https://arxiv.org/pdf/1708.02002.pdf)
    .
*   **from\_logits**: Whether to interpret `y_pred` as a tensor of [logit](https://en.wikipedia.org/wiki/Logit)
     values. By default, we assume that `y_pred` are probabilities (i.e., values in `[0, 1]`).
*   **label\_smoothing**: Float in `[0, 1]`. When `0`, no smoothing occurs. When > `0`, we compute the loss between the predicted labels and a smoothed version of the true labels, where the smoothing squeezes the labels towards `0.5`. Larger values of `label_smoothing` correspond to heavier smoothing.
*   **axis**: The axis along which to compute crossentropy (the features axis). Defaults to `-1`.
*   **reduction**: Type of reduction to apply to the loss. In almost all cases this should be `"sum_over_batch_size"`. Supported options are `"sum"`, `"sum_over_batch_size"`, `"mean"`, `"mean_with_sample_weight"` or `None`. `"sum"` sums the loss, `"sum_over_batch_size"` and `"mean"` sum the loss and divide by the sample size, and `"mean_with_sample_weight"` sums the loss and divides by the sum of the sample weights. `"none"` and `None` perform no aggregation. Defaults to `"sum_over_batch_size"`.
*   **name**: Optional name for the loss instance.
*   **dtype**: The dtype of the loss's computations. Defaults to `None`, which means using `keras.backend.floatx()`. `keras.backend.floatx()` is a `"float32"` unless set to different value (via `keras.backend.set_floatx()`). If a `keras.DTypePolicy` is provided, then the `compute_dtype` will be utilized.

**Examples**

With the `compile()` API:

Copied!

`model.compile(     loss=keras.losses.BinaryFocalCrossentropy(         gamma=2.0, from_logits=True),     ... )`

As a standalone function:

Copied!

`>>> # Example 1: (batch_size = 1, number of samples = 4) >>> y_true = np.array([0, 1, 0, 0]) >>> y_pred = np.array([-18.6, 0.51, 2.94, -12.8]) >>> loss = keras.losses.BinaryFocalCrossentropy( ...    gamma=2, from_logits=True) >>> loss(y_true, y_pred) 0.691`

Copied!

`>>> # Apply class weight >>> loss = keras.losses.BinaryFocalCrossentropy( ...     apply_class_balancing=True, gamma=2, from_logits=True) >>> loss(y_true, y_pred) 0.51`

Copied!

`>>> # Example 2: (batch_size = 2, number of samples = 4) >>> y_true = np.array([[0, 1], [0, 0]]) >>> y_pred = np.array([[-18.6, 0.51], [2.94, -12.8]]) >>> # Using default 'auto'/'sum_over_batch_size' reduction type. >>> loss = keras.losses.BinaryFocalCrossentropy( ...     gamma=3, from_logits=True) >>> loss(y_true, y_pred) 0.647`

Copied!

`>>> # Apply class weight >>> loss = keras.losses.BinaryFocalCrossentropy( ...      apply_class_balancing=True, gamma=3, from_logits=True) >>> loss(y_true, y_pred) 0.482`

Copied!

`>>> # Using 'sample_weight' attribute with focal effect >>> loss = keras.losses.BinaryFocalCrossentropy( ...     gamma=3, from_logits=True) >>> loss(y_true, y_pred, sample_weight=[0.8, 0.2]) 0.133`

Copied!

`>>> # Apply class weight >>> loss = keras.losses.BinaryFocalCrossentropy( ...      apply_class_balancing=True, gamma=3, from_logits=True) >>> loss(y_true, y_pred, sample_weight=[0.8, 0.2]) 0.097`

Copied!

``>>> # Using 'sum' reduction` type. >>> loss = keras.losses.BinaryFocalCrossentropy( ...     gamma=4, from_logits=True, ...     reduction="sum") >>> loss(y_true, y_pred) 1.222``

Copied!

`>>> # Apply class weight >>> loss = keras.losses.BinaryFocalCrossentropy( ...     apply_class_balancing=True, gamma=4, from_logits=True, ...     reduction="sum") >>> loss(y_true, y_pred) 0.914`

Copied!

`>>> # Using 'none' reduction type. >>> loss = keras.losses.BinaryFocalCrossentropy( ...     gamma=5, from_logits=True, ...     reduction=None) >>> loss(y_true, y_pred) array([0.0017 1.1561], dtype=float32)`

Copied!

`>>> # Apply class weight >>> loss = keras.losses.BinaryFocalCrossentropy( ...     apply_class_balancing=True, gamma=5, from_logits=True, ...     reduction=None) >>> loss(y_true, y_pred) array([0.0004 0.8670], dtype=float32)`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/losses/losses.py#L915)

### `CategoricalCrossentropy` class

Copied!

`keras.losses.CategoricalCrossentropy(     from_logits=False,     label_smoothing=0.0,     axis=-1,     reduction="sum_over_batch_size",     name="categorical_crossentropy",     dtype=None, )`

Computes the crossentropy loss between the labels and predictions.

Use this crossentropy loss function when there are two or more label classes. We expect labels to be provided in a `one_hot` representation. If you want to provide labels as integers, please use `SparseCategoricalCrossentropy` loss. There should be `num_classes` floating point values per feature, i.e., the shape of both `y_pred` and `y_true` are `[batch_size, num_classes]`.

**Arguments**

*   **from\_logits**: Whether `y_pred` is expected to be a logits tensor. By default, we assume that `y_pred` encodes a probability distribution.
*   **label\_smoothing**: Float in \[0, 1\]. When > 0, label values are smoothed, meaning the confidence on label values are relaxed. For example, if `0.1`, use `0.1 / num_classes` for non-target labels and `0.9 + 0.1 / num_classes` for target labels.
*   **axis**: The axis along which to compute crossentropy (the features axis). Defaults to `-1`.
*   **reduction**: Type of reduction to apply to the loss. In almost all cases this should be `"sum_over_batch_size"`. Supported options are `"sum"`, `"sum_over_batch_size"`, `"mean"`, `"mean_with_sample_weight"` or `None`. `"sum"` sums the loss, `"sum_over_batch_size"` and `"mean"` sum the loss and divide by the sample size, and `"mean_with_sample_weight"` sums the loss and divides by the sum of the sample weights. `"none"` and `None` perform no aggregation. Defaults to `"sum_over_batch_size"`.
*   **name**: Optional name for the loss instance.
*   **dtype**: The dtype of the loss's computations. Defaults to `None`, which means using `keras.backend.floatx()`. `keras.backend.floatx()` is a `"float32"` unless set to different value (via `keras.backend.set_floatx()`). If a `keras.DTypePolicy` is provided, then the `compute_dtype` will be utilized.

**Examples**

Standalone usage:

Copied!

`>>> y_true = np.array([[0, 1, 0], [0, 0, 1]]) >>> y_pred = np.array([[0.05, 0.95, 0], [0.1, 0.8, 0.1]]) >>> # Using 'auto'/'sum_over_batch_size' reduction type. >>> cce = keras.losses.CategoricalCrossentropy() >>> cce(y_true, y_pred) 1.177`

Copied!

`>>> # Calling with 'sample_weight'. >>> cce(y_true, y_pred, sample_weight=np.array([0.3, 0.7])) 0.814`

Copied!

`>>> # Using 'sum' reduction type. >>> cce = keras.losses.CategoricalCrossentropy( ...     reduction="sum") >>> cce(y_true, y_pred) 2.354`

Copied!

`>>> # Using 'none' reduction type. >>> cce = keras.losses.CategoricalCrossentropy( ...     reduction=None) >>> cce(y_true, y_pred) array([0.0513, 2.303], dtype=float32)`

Usage with the `compile()` API:

Copied!

`model.compile(optimizer='sgd',               loss=keras.losses.CategoricalCrossentropy())`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/losses/losses.py#L1019)

### `CategoricalFocalCrossentropy` class

Copied!

`keras.losses.CategoricalFocalCrossentropy(     alpha=0.25,     gamma=2.0,     from_logits=False,     label_smoothing=0.0,     axis=-1,     reduction="sum_over_batch_size",     name="categorical_focal_crossentropy",     dtype=None, )`

Computes the alpha balanced focal crossentropy loss.

Use this crossentropy loss function when there are two or more label classes and if you want to handle class imbalance without using `class_weights`. We expect labels to be provided in a `one_hot` representation.

According to [Lin et al., 2018](https://arxiv.org/pdf/1708.02002.pdf)
, it helps to apply a focal factor to down-weight easy examples and focus more on hard examples. The general formula for the focal loss (FL) is as follows:

`FL(p_t) = (1 - p_t) ** gamma * log(p_t)`

where `p_t` is defined as follows: `p_t = output if y_true == 1, else 1 - output`

`(1 - p_t) ** gamma` is the `modulating_factor`, where `gamma` is a focusing parameter. When `gamma` = 0, there is no focal effect on the cross entropy. `gamma` reduces the importance given to simple examples in a smooth manner.

The authors use alpha-balanced variant of focal loss (FL) in the paper: `FL(p_t) = -alpha * (1 - p_t) ** gamma * log(p_t)`

where `alpha` is the weight factor for the classes. If `alpha` = 1, the loss won't be able to handle class imbalance properly as all classes will have the same weight. This can be a constant or a list of constants. If alpha is a list, it must have the same length as the number of classes.

The formula above can be generalized to: `FL(p_t) = alpha * (1 - p_t) ** gamma * CrossEntropy(y_true, y_pred)`

where minus comes from `CrossEntropy(y_true, y_pred)` (CE).

Extending this to multi-class case is straightforward: `FL(p_t) = alpha * (1 - p_t) ** gamma * CategoricalCE(y_true, y_pred)`

In the snippet below, there is `num_classes` floating pointing values per example. The shape of both `y_pred` and `y_true` are `(batch_size, num_classes)`.

**Arguments**

*   **alpha**: A weight balancing factor for all classes, default is `0.25` as mentioned in the reference. It can be a list of floats or a scalar. In the multi-class case, alpha may be set by inverse class frequency by using `compute_class_weight` from `sklearn.utils`.
*   **gamma**: A focusing parameter, default is `2.0` as mentioned in the reference. It helps to gradually reduce the importance given to simple (easy) examples in a smooth manner.
*   **from\_logits**: Whether `output` is expected to be a logits tensor. By default, we consider that `output` encodes a probability distribution.
*   **label\_smoothing**: Float in \[0, 1\]. When > 0, label values are smoothed, meaning the confidence on label values are relaxed. For example, if `0.1`, use `0.1 / num_classes` for non-target labels and `0.9 + 0.1 / num_classes` for target labels.
*   **axis**: The axis along which to compute crossentropy (the features axis). Defaults to `-1`.
*   **reduction**: Type of reduction to apply to the loss. In almost all cases this should be `"sum_over_batch_size"`. Supported options are `"sum"`, `"sum_over_batch_size"`, `"mean"`, `"mean_with_sample_weight"` or `None`. `"sum"` sums the loss, `"sum_over_batch_size"` and `"mean"` sum the loss and divide by the sample size, and `"mean_with_sample_weight"` sums the loss and divides by the sum of the sample weights. `"none"` and `None` perform no aggregation. Defaults to `"sum_over_batch_size"`.
*   **name**: Optional name for the loss instance.
*   **dtype**: The dtype of the loss's computations. Defaults to `None`, which means using `keras.backend.floatx()`. `keras.backend.floatx()` is a `"float32"` unless set to different value (via `keras.backend.set_floatx()`). If a `keras.DTypePolicy` is provided, then the `compute_dtype` will be utilized.

**Examples**

Standalone usage:

Copied!

`>>> y_true = [[0., 1., 0.], [0., 0., 1.]] >>> y_pred = [[0.05, 0.95, 0], [0.1, 0.8, 0.1]] >>> # Using 'auto'/'sum_over_batch_size' reduction type. >>> cce = keras.losses.CategoricalFocalCrossentropy() >>> cce(y_true, y_pred) 0.23315276`

Copied!

`>>> # Calling with 'sample_weight'. >>> cce(y_true, y_pred, sample_weight=np.array([0.3, 0.7])) 0.1632`

Copied!

`>>> # Using 'sum' reduction type. >>> cce = keras.losses.CategoricalFocalCrossentropy( ...     reduction="sum") >>> cce(y_true, y_pred) 0.46631`

Copied!

`>>> # Using 'none' reduction type. >>> cce = keras.losses.CategoricalFocalCrossentropy( ...     reduction=None) >>> cce(y_true, y_pred) array([3.2058331e-05, 4.6627346e-01], dtype=float32)`

Usage with the `compile()` API:

Copied!

`model.compile(optimizer='adam',               loss=keras.losses.CategoricalFocalCrossentropy())`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/losses/losses.py#L1173)

### `SparseCategoricalCrossentropy` class

Copied!

`keras.losses.SparseCategoricalCrossentropy(     from_logits=False,     ignore_class=None,     reduction="sum_over_batch_size",     axis=-1,     name="sparse_categorical_crossentropy",     dtype=None, )`

Computes the crossentropy loss between the labels and predictions.

Use this crossentropy loss function when there are two or more label classes. We expect labels to be provided as integers. If you want to provide labels using `one-hot` representation, please use `CategoricalCrossentropy` loss. There should be `# classes` floating point values per feature for `y_pred` and a single floating point value per feature for `y_true`.

In the snippet below, there is a single floating point value per example for `y_true` and `num_classes` floating pointing values per example for `y_pred`. The shape of `y_true` is `[batch_size]` and the shape of `y_pred` is `[batch_size, num_classes]`.

**Arguments**

*   **from\_logits**: Whether `y_pred` is expected to be a logits tensor. By default, we assume that `y_pred` encodes a probability distribution.
*   **reduction**: Type of reduction to apply to the loss. In almost all cases this should be `"sum_over_batch_size"`. Supported options are `"sum"`, `"sum_over_batch_size"`, `"mean"`, `"mean_with_sample_weight"` or `None`. `"sum"` sums the loss, `"sum_over_batch_size"` and `"mean"` sum the loss and divide by the sample size, and `"mean_with_sample_weight"` sums the loss and divides by the sum of the sample weights. `"none"` and `None` perform no aggregation. Defaults to `"sum_over_batch_size"`.
*   **axis**: The axis along which to compute crossentropy (the features axis). Defaults to `-1`.
*   **name**: Optional name for the loss instance.
*   **dtype**: The dtype of the loss's computations. Defaults to `None`, which means using `keras.backend.floatx()`. `keras.backend.floatx()` is a `"float32"` unless set to different value (via `keras.backend.set_floatx()`). If a `keras.DTypePolicy` is provided, then the `compute_dtype` will be utilized.

**Examples**

Copied!

`>>> y_true = np.array([1, 2]) >>> y_pred = np.array([[0.05, 0.95, 0], [0.1, 0.8, 0.1]]) >>> # Using 'auto'/'sum_over_batch_size' reduction type. >>> scce = keras.losses.SparseCategoricalCrossentropy() >>> scce(y_true, y_pred) 1.177`

Copied!

`>>> # Calling with 'sample_weight'. >>> scce(y_true, y_pred, sample_weight=np.array([0.3, 0.7])) 0.814`

Copied!

`>>> # Using 'sum' reduction type. >>> scce = keras.losses.SparseCategoricalCrossentropy( ...     reduction="sum") >>> scce(y_true, y_pred) 2.354`

Copied!

`>>> # Using 'none' reduction type. >>> scce = keras.losses.SparseCategoricalCrossentropy( ...     reduction=None) >>> scce(y_true, y_pred) array([0.0513, 2.303], dtype=float32)`

Usage with the `compile()` API:

Copied!

`model.compile(optimizer='sgd',               loss=keras.losses.SparseCategoricalCrossentropy())`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/losses/losses.py#L565)

### `Poisson` class

Copied!

`keras.losses.Poisson(reduction="sum_over_batch_size", name="poisson", dtype=None)`

Computes the Poisson loss between `y_true` & `y_pred`.

Formula:

Copied!

`loss = y_pred - y_true * log(y_pred)`

**Arguments**

*   **reduction**: Type of reduction to apply to the loss. In almost all cases this should be `"sum_over_batch_size"`. Supported options are `"sum"`, `"sum_over_batch_size"`, `"mean"`, `"mean_with_sample_weight"` or `None`. `"sum"` sums the loss, `"sum_over_batch_size"` and `"mean"` sum the loss and divide by the sample size, and `"mean_with_sample_weight"` sums the loss and divides by the sum of the sample weights. `"none"` and `None` perform no aggregation. Defaults to `"sum_over_batch_size"`.
*   **name**: Optional name for the loss instance.
*   **dtype**: The dtype of the loss's computations. Defaults to `None`, which means using `keras.backend.floatx()`. `keras.backend.floatx()` is a `"float32"` unless set to different value (via `keras.backend.set_floatx()`). If a `keras.DTypePolicy` is provided, then the `compute_dtype` will be utilized.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/losses/losses.py#L1274)

### `CTC` class

Copied!

`keras.losses.CTC(reduction="sum_over_batch_size", name="ctc", dtype=None)`

CTC (Connectionist Temporal Classification) loss.

**Arguments**

*   **reduction**: Type of reduction to apply to the loss. In almost all cases this should be `"sum_over_batch_size"`. Supported options are `"sum"`, `"sum_over_batch_size"`, `"mean"`, `"mean_with_sample_weight"` or `None`. `"sum"` sums the loss, `"sum_over_batch_size"` and `"mean"` sum the loss and divide by the sample size, and `"mean_with_sample_weight"` sums the loss and divides by the sum of the sample weights. `"none"` and `None` perform no aggregation. Defaults to `"sum_over_batch_size"`.
*   **name**: Optional name for the loss instance.
*   **dtype**: The dtype of the loss's computations. Defaults to `None`, which means using `keras.backend.floatx()`. `keras.backend.floatx()` is a `"float32"` unless set to different value (via `keras.backend.set_floatx()`). If a `keras.DTypePolicy` is provided, then the `compute_dtype` will be utilized.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/losses/losses.py#L523)

### `KLDivergence` class

Copied!

`keras.losses.KLDivergence(     reduction="sum_over_batch_size", name="kl_divergence", dtype=None )`

Computes Kullback-Leibler divergence loss between `y_true` & `y_pred`.

Formula:

Copied!

`loss = y_true * log(y_true / y_pred)`

`y_true` and `y_pred` are expected to be probability distributions, with values between 0 and 1. They will get clipped to the `[0, 1]` range.

**Arguments**

*   **reduction**: Type of reduction to apply to the loss. In almost all cases this should be `"sum_over_batch_size"`. Supported options are `"sum"`, `"sum_over_batch_size"`, `"mean"`, `"mean_with_sample_weight"` or `None`. `"sum"` sums the loss, `"sum_over_batch_size"` and `"mean"` sum the loss and divide by the sample size, and `"mean_with_sample_weight"` sums the loss and divides by the sum of the sample weights. `"none"` and `None` perform no aggregation. Defaults to `"sum_over_batch_size"`.
*   **name**: Optional name for the loss instance.
*   **dtype**: The dtype of the loss's computations. Defaults to `None`, which means using `keras.backend.floatx()`. `keras.backend.floatx()` is a `"float32"` unless set to different value (via `keras.backend.set_floatx()`). If a `keras.DTypePolicy` is provided, then the `compute_dtype` will be utilized.

* * *

[Probabilistic losses](https://keras.io/api/losses/probabilistic_losses/#probabilistic-losses)

[`BinaryCrossentropy` class](https://keras.io/api/losses/probabilistic_losses/#binarycrossentropy-class)

[`BinaryFocalCrossentropy` class](https://keras.io/api/losses/probabilistic_losses/#binaryfocalcrossentropy-class)

[`CategoricalCrossentropy` class](https://keras.io/api/losses/probabilistic_losses/#categoricalcrossentropy-class)

[`CategoricalFocalCrossentropy` class](https://keras.io/api/losses/probabilistic_losses/#categoricalfocalcrossentropy-class)

[`SparseCategoricalCrossentropy` class](https://keras.io/api/losses/probabilistic_losses/#sparsecategoricalcrossentropy-class)

[`Poisson` class](https://keras.io/api/losses/probabilistic_losses/#poisson-class)

[`CTC` class](https://keras.io/api/losses/probabilistic_losses/#ctc-class)

[`KLDivergence` class](https://keras.io/api/losses/probabilistic_losses/#kldivergence-class)