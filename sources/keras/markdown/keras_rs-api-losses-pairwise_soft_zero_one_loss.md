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
 / [Losses](https://keras.io/keras_rs/api/losses/)
 / PairwiseSoftZeroOneLoss

PairwiseSoftZeroOneLoss
=======================

[\[source\]](https://github.com/keras-team/keras-rs/tree/v0.4.0/keras_rs/src/losses/pairwise_soft_zero_one_loss.py#L9)

### `PairwiseSoftZeroOneLoss` class

Copied!

`keras_rs.losses.PairwiseSoftZeroOneLoss(temperature: float = 1.0, **kwargs: Any)`

Computes pairwise soft zero-one loss between true labels and predicted scores. This loss function is designed for ranking tasks, where the goal is to correctly order items within each list. It computes the loss by comparing pairs of items within each list, penalizing cases where an item with a higher true label has a lower predicted score than an item with a lower true label.

For each list of predicted scores `s` in `y_pred` and the corresponding list of true labels `y` in `y_true`, the loss is computed as follows:

Copied!

`loss = sum_{i} sum_{j} I(y_i > y_j) * (1 - sigmoid(s_i - s_j))`

where:

*   `y_i` and `y_j` are the true labels of items `i` and `j`, respectively.
*   `s_i` and `s_j` are the predicted scores of items `i` and `j`, respectively.
*   `I(y_i > y_j)` is an indicator function that equals 1 if `y_i > y_j`, and 0 otherwise.
*   `(1 - sigmoid(s_i - s_j))` represents the soft zero-one loss, which approximates the ideal zero-one loss (which would be 1 if `s_i < s_j` and 0 otherwise) with a smooth, differentiable function. This makes it suitable for gradient-based optimization.

**Arguments**

*   **reduction**: Type of reduction to apply to the loss. In almost all cases this should be `"sum_over_batch_size"`. Supported options are `"sum"`, `"sum_over_batch_size"`, `"mean"`, `"mean_with_sample_weight"` or `None`. `"sum"` sums the loss, `"sum_over_batch_size"` and `"mean"` sum the loss and divide by the sample size, and `"mean_with_sample_weight"` sums the loss and divides by the sum of the sample weights. `"none"` and `None` perform no aggregation. Defaults to `"sum_over_batch_size"`.
*   **name**: Optional name for the loss instance.
*   **dtype**: The dtype of the loss's computations. Defaults to `None`, which means using `keras.backend.floatx()`. `keras.backend.floatx()` is a `"float32"` unless set to different value (via `keras.backend.set_floatx()`). If a `keras.DTypePolicy` is provided, then the `compute_dtype` will be utilized.

**Examples**

With `compile()` API:

Copied!

`model.compile(     loss=keras_rs.losses.PairwiseSoftZeroOneLoss(),     ... )`

As a standalone function with unbatched inputs:

Copied!

`>>> y_true = np.array([1.0, 0.0, 1.0, 3.0, 2.0]) >>> y_pred = np.array([1.0, 3.0, 2.0, 4.0, 0.8]) >>> pairwise_soft_zero_one_loss = keras_rs.losses.PairwiseSoftZeroOneLoss() >>> pairwise_soft_zero_one_loss(y_true=y_true, y_pred=y_pred) 0.86103`

With batched inputs using default 'auto'/'sum\_over\_batch\_size' reduction:

Copied!

`>>> y_true = np.array([[1.0, 0.0, 1.0, 3.0], [0.0, 1.0, 2.0, 3.0]]) >>> y_pred = np.array([[1.0, 3.0, 2.0, 4.0], [1.0, 1.8, 2.0, 3.0]]) >>> pairwise_soft_zero_one_loss = keras_rs.losses.PairwiseSoftZeroOneLoss() >>> pairwise_soft_zero_one_loss(y_true=y_true, y_pred=y_pred) 0.46202`

With masked inputs (useful for ragged inputs):

Copied!

`>>> y_true = { ...     "labels": np.array([[1.0, 0.0, 1.0, 3.0], [0.0, 1.0, 2.0, 3.0]]), ...     "mask": np.array( ...         [[True, True, True, True], [True, True, False, False]] ...     ), ... } >>> y_pred = np.array([[1.0, 3.0, 2.0, 4.0], [1.0, 1.8, 2.0, 3.0]]) >>> pairwise_soft_zero_one_loss(y_true=y_true, y_pred=y_pred) 0.29468`

With `sample_weight`:

Copied!

`>>> y_true = np.array([[1.0, 0.0, 1.0, 3.0], [0.0, 1.0, 2.0, 3.0]]) >>> y_pred = np.array([[1.0, 3.0, 2.0, 4.0], [1.0, 1.8, 2.0, 3.0]]) >>> sample_weight = np.array( ...     [[2.0, 3.0, 1.0, 1.0], [2.0, 1.0, 0.0, 0.0]] ... ) >>> pairwise_soft_zero_one_loss = keras_rs.losses.PairwiseSoftZeroOneLoss() >>> pairwise_soft_zero_one_loss( ...     y_true=y_true, y_pred=y_pred, sample_weight=sample_weight ... ) 0.40478`

Using `'none'` reduction:

Copied!

`>>> y_true = np.array([[1.0, 0.0, 1.0, 3.0], [0.0, 1.0, 2.0, 3.0]]) >>> y_pred = np.array([[1.0, 3.0, 2.0, 4.0], [1.0, 1.8, 2.0, 3.0]]) >>> pairwise_soft_zero_one_loss = keras_rs.losses.PairwiseSoftZeroOneLoss( ...     reduction="none" ... ) >>> pairwise_soft_zero_one_loss(y_true=y_true, y_pred=y_pred) [     [0.8807971 , 0., 0.73105854, 0.43557024],     [0., 0.31002545, 0.7191075 , 0.61961967] ]`

* * *

[\[source\]](https://github.com/keras-team/keras-rs/tree/v0.4.0/keras_rs/src/losses/pairwise_loss.py#L68)

### `call` method

Copied!

`PairwiseSoftZeroOneLoss.call(y_true: Any, y_pred: Any)`

Compute the pairwise loss.

**Arguments**

*   **y\_true**: tensor or dict. Ground truth values. If tensor, of shape `(list_size)` for unbatched inputs or `(batch_size, list_size)` for batched inputs. If an item has a label of -1, it is ignored in loss computation. If it is a dictionary, it should have two keys: `"labels"` and `"mask"`. `"mask"` can be used to ignore elements in loss computation, i.e., pairs will not be formed with those items. Note that the final mask is an `and` of the passed mask, and `labels >= 0`.
*   **y\_pred**: tensor. The predicted values, of shape `(list_size)` for unbatched inputs or `(batch_size, list_size)` for batched inputs. Should be of the same shape as `y_true`.

**Returns**

The loss.

* * *

[PairwiseSoftZeroOneLoss](https://keras.io/keras_rs/api/losses/pairwise_soft_zero_one_loss/#pairwisesoftzerooneloss)

[`PairwiseSoftZeroOneLoss` class](https://keras.io/keras_rs/api/losses/pairwise_soft_zero_one_loss/#pairwisesoftzerooneloss-class)

[`call` method](https://keras.io/keras_rs/api/losses/pairwise_soft_zero_one_loss/#call-method)