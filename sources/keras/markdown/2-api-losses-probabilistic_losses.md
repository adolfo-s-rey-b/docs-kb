None

[Keras 3 API documentation](https://keras.io/api/)
 [Keras 2 API documentation](https://keras.io/2/api/)

[Models API](https://keras.io/2/api/models/)
 [Layers API](https://keras.io/2/api/layers/)
 [Callbacks API](https://keras.io/2/api/callbacks/)
 [Optimizers](https://keras.io/2/api/optimizers/)
 [Metrics](https://keras.io/2/api/metrics/)
 [Losses](https://keras.io/2/api/losses/)
 [Probabilistic losses](https://keras.io/2/api/losses/probabilistic_losses/)
 [Regression losses](https://keras.io/2/api/losses/regression_losses/)
 [Hinge losses for "maximum-margin" classification](https://keras.io/2/api/losses/hinge_losses/)
 [Data loading](https://keras.io/2/api/data_loading/)
 [Built-in small datasets](https://keras.io/2/api/datasets/)
 [Keras Applications](https://keras.io/2/api/applications/)
 [Mixed precision](https://keras.io/2/api/mixed_precision/)
 [Utilities](https://keras.io/2/api/utils/)

► [Keras 2 API documentation](https://keras.io/2/api/)
 / [Losses](https://keras.io/2/api/losses/)
 / Probabilistic losses

Probabilistic losses
====================

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/losses.py#L561)

### `BinaryCrossentropy` class

Copied!

`tf_keras.losses.BinaryCrossentropy(     from_logits=False,     label_smoothing=0.0,     axis=-1,     reduction="auto",     name="binary_crossentropy", )`

Computes the cross-entropy loss between true labels and predicted labels.

Use this cross-entropy loss for binary (0 or 1) classification applications. The loss function requires the following inputs:

*   `y_true` (true label): This is either 0 or 1.
*   `y_pred` (predicted value): This is the model's prediction, i.e, a single floating-point value which either represents a [logit](https://en.wikipedia.org/wiki/Logit)
    , (i.e, value in \[-inf, inf\] when `from_logits=True`) or a probability (i.e, value in \[0., 1.\] when `from_logits=False`).

**Recommended Usage:** (set `from_logits=True`)

With [`tf.keras`](https://www.tensorflow.org/api_docs/python/tf/keras)
 API:

Copied!

`model.compile(     loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),     .... )`

As a standalone function:

Copied!

`>>> # Example 1: (batch_size = 1, number of samples = 4) >>> y_true = [0, 1, 0, 0] >>> y_pred = [-18.6, 0.51, 2.94, -12.8] >>> bce = tf.keras.losses.BinaryCrossentropy(from_logits=True) >>> bce(y_true, y_pred).numpy() 0.865`

Copied!

``>>> # Example 2: (batch_size = 2, number of samples = 4) >>> y_true = [[0, 1], [0, 0]] >>> y_pred = [[-18.6, 0.51], [2.94, -12.8]] >>> # Using default 'auto'/'sum_over_batch_size' reduction type. >>> bce = tf.keras.losses.BinaryCrossentropy(from_logits=True) >>> bce(y_true, y_pred).numpy() 0.865 >>> # Using 'sample_weight' attribute >>> bce(y_true, y_pred, sample_weight=[0.8, 0.2]).numpy() 0.243 >>> # Using 'sum' reduction` type. >>> bce = tf.keras.losses.BinaryCrossentropy(from_logits=True, ...     reduction=tf.keras.losses.Reduction.SUM) >>> bce(y_true, y_pred).numpy() 1.730 >>> # Using 'none' reduction type. >>> bce = tf.keras.losses.BinaryCrossentropy(from_logits=True, ...     reduction=tf.keras.losses.Reduction.NONE) >>> bce(y_true, y_pred).numpy() array([0.235, 1.496], dtype=float32)``

**Default Usage:** (set `from_logits=False`)

Copied!

``>>> # Make the following updates to the above "Recommended Usage" section >>> # 1. Set `from_logits=False` >>> tf.keras.losses.BinaryCrossentropy() # OR ...('from_logits=False') >>> # 2. Update `y_pred` to use probabilities instead of logits >>> y_pred = [0.6, 0.3, 0.2, 0.8] # OR [[0.6, 0.3], [0.2, 0.8]]``

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/losses.py#L844)

### `CategoricalCrossentropy` class

Copied!

`tf_keras.losses.CategoricalCrossentropy(     from_logits=False,     label_smoothing=0.0,     axis=-1,     reduction="auto",     name="categorical_crossentropy", )`

Computes the crossentropy loss between the labels and predictions.

Use this crossentropy loss function when there are two or more label classes. We expect labels to be provided in a `one_hot` representation. If you want to provide labels as integers, please use `SparseCategoricalCrossentropy` loss. There should be `# classes` floating point values per feature.

In the snippet below, there is `# classes` floating pointing values per example. The shape of both `y_pred` and `y_true` are `[batch_size, num_classes]`.

Standalone usage:

Copied!

`>>> y_true = [[0, 1, 0], [0, 0, 1]] >>> y_pred = [[0.05, 0.95, 0], [0.1, 0.8, 0.1]] >>> # Using 'auto'/'sum_over_batch_size' reduction type. >>> cce = tf.keras.losses.CategoricalCrossentropy() >>> cce(y_true, y_pred).numpy() 1.177`

Copied!

`>>> # Calling with 'sample_weight'. >>> cce(y_true, y_pred, sample_weight=tf.constant([0.3, 0.7])).numpy() 0.814`

Copied!

`>>> # Using 'sum' reduction type. >>> cce = tf.keras.losses.CategoricalCrossentropy( ...     reduction=tf.keras.losses.Reduction.SUM) >>> cce(y_true, y_pred).numpy() 2.354`

Copied!

`>>> # Using 'none' reduction type. >>> cce = tf.keras.losses.CategoricalCrossentropy( ...     reduction=tf.keras.losses.Reduction.NONE) >>> cce(y_true, y_pred).numpy() array([0.0513, 2.303], dtype=float32)`

Usage with the `compile()` API:

Copied!

`model.compile(optimizer='sgd',               loss=tf.keras.losses.CategoricalCrossentropy())`

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/losses.py#L1073)

### `SparseCategoricalCrossentropy` class

Copied!

`tf_keras.losses.SparseCategoricalCrossentropy(     from_logits=False,     ignore_class=None,     reduction="auto",     name="sparse_categorical_crossentropy", )`

Computes the crossentropy loss between the labels and predictions.

Use this crossentropy loss function when there are two or more label classes. We expect labels to be provided as integers. If you want to provide labels using `one-hot` representation, please use `CategoricalCrossentropy` loss. There should be `# classes` floating point values per feature for `y_pred` and a single floating point value per feature for `y_true`.

In the snippet below, there is a single floating point value per example for `y_true` and `# classes` floating pointing values per example for `y_pred`. The shape of `y_true` is `[batch_size]` and the shape of `y_pred` is `[batch_size, num_classes]`.

Standalone usage:

Copied!

`>>> y_true = [1, 2] >>> y_pred = [[0.05, 0.95, 0], [0.1, 0.8, 0.1]] >>> # Using 'auto'/'sum_over_batch_size' reduction type. >>> scce = tf.keras.losses.SparseCategoricalCrossentropy() >>> scce(y_true, y_pred).numpy() 1.177`

Copied!

`>>> # Calling with 'sample_weight'. >>> scce(y_true, y_pred, sample_weight=tf.constant([0.3, 0.7])).numpy() 0.814`

Copied!

`>>> # Using 'sum' reduction type. >>> scce = tf.keras.losses.SparseCategoricalCrossentropy( ...     reduction=tf.keras.losses.Reduction.SUM) >>> scce(y_true, y_pred).numpy() 2.354`

Copied!

`>>> # Using 'none' reduction type. >>> scce = tf.keras.losses.SparseCategoricalCrossentropy( ...     reduction=tf.keras.losses.Reduction.NONE) >>> scce(y_true, y_pred).numpy() array([0.0513, 2.303], dtype=float32)`

Usage with the `compile()` API:

Copied!

`model.compile(optimizer='sgd',               loss=tf.keras.losses.SparseCategoricalCrossentropy())`

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/losses.py#L1422)

### `Poisson` class

Copied!

`tf_keras.losses.Poisson(reduction="auto", name="poisson")`

Computes the Poisson loss between `y_true` & `y_pred`.

`loss = y_pred - y_true * log(y_pred)`

Standalone usage:

Copied!

`>>> y_true = [[0., 1.], [0., 0.]] >>> y_pred = [[1., 1.], [0., 0.]] >>> # Using 'auto'/'sum_over_batch_size' reduction type. >>> p = tf.keras.losses.Poisson() >>> p(y_true, y_pred).numpy() 0.5`

Copied!

`>>> # Calling with 'sample_weight'. >>> p(y_true, y_pred, sample_weight=[0.8, 0.2]).numpy() 0.4`

Copied!

`>>> # Using 'sum' reduction type. >>> p = tf.keras.losses.Poisson( ...     reduction=tf.keras.losses.Reduction.SUM) >>> p(y_true, y_pred).numpy() 0.999`

Copied!

`>>> # Using 'none' reduction type. >>> p = tf.keras.losses.Poisson( ...     reduction=tf.keras.losses.Reduction.NONE) >>> p(y_true, y_pred).numpy() array([0.999, 0.], dtype=float32)`

Usage with the `compile()` API:

Copied!

`model.compile(optimizer='sgd', loss=tf.keras.losses.Poisson())`

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/losses.py#L2488)

### `binary_crossentropy` function

Copied!

`tf_keras.losses.binary_crossentropy(     y_true, y_pred, from_logits=False, label_smoothing=0.0, axis=-1 )`

Computes the binary crossentropy loss.

Standalone usage:

Copied!

`>>> y_true = [[0, 1], [0, 0]] >>> y_pred = [[0.6, 0.4], [0.4, 0.6]] >>> loss = tf.keras.losses.binary_crossentropy(y_true, y_pred) >>> assert loss.shape == (2,) >>> loss.numpy() array([0.916 , 0.714], dtype=float32)`

**Arguments**

*   **y\_true**: Ground truth values. shape = `[batch_size, d0, .. dN]`.
*   **y\_pred**: The predicted values. shape = `[batch_size, d0, .. dN]`.
*   **from\_logits**: Whether `y_pred` is expected to be a logits tensor. By default, we assume that `y_pred` encodes a probability distribution.
*   **label\_smoothing**: Float in \[0, 1\]. If > `0` then smooth the labels by squeezing them towards 0.5 That is, using `1. - 0.5 * label_smoothing` for the target class and `0.5 * label_smoothing` for the non-target class.
*   **axis**: The axis along which the mean is computed. Defaults to -1.

**Returns**

Binary crossentropy loss value. shape = `[batch_size, d0, .. dN-1]`.

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/losses.py#L2159)

### `categorical_crossentropy` function

Copied!

`tf_keras.losses.categorical_crossentropy(     y_true, y_pred, from_logits=False, label_smoothing=0.0, axis=-1 )`

Computes the categorical crossentropy loss.

Standalone usage:

Copied!

`>>> y_true = [[0, 1, 0], [0, 0, 1]] >>> y_pred = [[0.05, 0.95, 0], [0.1, 0.8, 0.1]] >>> loss = tf.keras.losses.categorical_crossentropy(y_true, y_pred) >>> assert loss.shape == (2,) >>> loss.numpy() array([0.0513, 2.303], dtype=float32)`

**Arguments**

*   **y\_true**: Tensor of one-hot true targets.
*   **y\_pred**: Tensor of predicted targets.
*   **from\_logits**: Whether `y_pred` is expected to be a logits tensor. By default, we assume that `y_pred` encodes a probability distribution.
*   **label\_smoothing**: Float in \[0, 1\]. If > `0` then smooth the labels. For example, if `0.1`, use `0.1 / num_classes` for non-target labels and `0.9 + 0.1 / num_classes` for target labels.
*   **axis**: Defaults to -1. The dimension along which the entropy is computed.

**Returns**

Categorical crossentropy loss value.

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/losses.py#L2403)

### `sparse_categorical_crossentropy` function

Copied!

`tf_keras.losses.sparse_categorical_crossentropy(     y_true, y_pred, from_logits=False, axis=-1, ignore_class=None )`

Computes the sparse categorical crossentropy loss.

Standalone usage:

Copied!

`>>> y_true = [1, 2] >>> y_pred = [[0.05, 0.95, 0], [0.1, 0.8, 0.1]] >>> loss = tf.keras.losses.sparse_categorical_crossentropy(y_true, y_pred) >>> assert loss.shape == (2,) >>> loss.numpy() array([0.0513, 2.303], dtype=float32)`

Copied!

`>>> y_true = [[[ 0,  2], ...            [-1, -1]], ...           [[ 0,  2], ...            [-1, -1]]] >>> y_pred = [[[[1.0, 0.0, 0.0], [0.0, 0.0, 1.0]], ...             [[0.2, 0.5, 0.3], [0.0, 1.0, 0.0]]], ...           [[[1.0, 0.0, 0.0], [0.0, 0.5, 0.5]], ...            [[0.2, 0.5, 0.3], [0.0, 1.0, 0.0]]]] >>> loss = tf.keras.losses.sparse_categorical_crossentropy( ...   y_true, y_pred, ignore_class=-1) >>> loss.numpy() array([[[2.3841855e-07, 2.3841855e-07],         [0.0000000e+00, 0.0000000e+00]],        [[2.3841855e-07, 6.9314730e-01],         [0.0000000e+00, 0.0000000e+00]]], dtype=float32)`

**Arguments**

*   **y\_true**: Ground truth values.
*   **y\_pred**: The predicted values.
*   **from\_logits**: Whether `y_pred` is expected to be a logits tensor. By default, we assume that `y_pred` encodes a probability distribution.
*   **axis**: Defaults to -1. The dimension along which the entropy is computed.
*   **ignore\_class**: Optional integer. The ID of a class to be ignored during loss computation. This is useful, for example, in segmentation problems featuring a "void" class (commonly -1 or 255) in segmentation maps. By default (`ignore_class=None`), all classes are considered.

**Returns**

Sparse categorical crossentropy loss value.

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/losses.py#L2761)

### `poisson` function

Copied!

`tf_keras.losses.poisson(y_true, y_pred)`

Computes the Poisson loss between y\_true and y\_pred.

The Poisson loss is the mean of the elements of the `Tensor` `y_pred - y_true * log(y_pred)`.

Standalone usage:

Copied!

`>>> y_true = np.random.randint(0, 2, size=(2, 3)) >>> y_pred = np.random.random(size=(2, 3)) >>> loss = tf.keras.losses.poisson(y_true, y_pred) >>> assert loss.shape == (2,) >>> y_pred = y_pred + 1e-7 >>> assert np.allclose( ...     loss.numpy(), np.mean(y_pred - y_true * np.log(y_pred), axis=-1), ...     atol=1e-5)`

**Arguments**

*   **y\_true**: Ground truth values. shape = `[batch_size, d0, .. dN]`.
*   **y\_pred**: The predicted values. shape = `[batch_size, d0, .. dN]`.

**Returns**

Poisson loss value. shape = `[batch_size, d0, .. dN-1]`.

**Raises**

*   **InvalidArgumentError**: If `y_true` and `y_pred` have incompatible shapes.

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/losses.py#L1539)

### `KLDivergence` class

Copied!

`tf_keras.losses.KLDivergence(reduction="auto", name="kl_divergence")`

Computes Kullback-Leibler divergence loss between `y_true` & `y_pred`.

`loss = y_true * log(y_true / y_pred)`

See: https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler\_divergence

Standalone usage:

Copied!

`>>> y_true = [[0, 1], [0, 0]] >>> y_pred = [[0.6, 0.4], [0.4, 0.6]] >>> # Using 'auto'/'sum_over_batch_size' reduction type. >>> kl = tf.keras.losses.KLDivergence() >>> kl(y_true, y_pred).numpy() 0.458`

Copied!

`>>> # Calling with 'sample_weight'. >>> kl(y_true, y_pred, sample_weight=[0.8, 0.2]).numpy() 0.366`

Copied!

`>>> # Using 'sum' reduction type. >>> kl = tf.keras.losses.KLDivergence( ...     reduction=tf.keras.losses.Reduction.SUM) >>> kl(y_true, y_pred).numpy() 0.916`

Copied!

`>>> # Using 'none' reduction type. >>> kl = tf.keras.losses.KLDivergence( ...     reduction=tf.keras.losses.Reduction.NONE) >>> kl(y_true, y_pred).numpy() array([0.916, -3.08e-06], dtype=float32)`

Usage with the `compile()` API:

Copied!

`model.compile(optimizer='sgd', loss=tf.keras.losses.KLDivergence())`

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/losses.py#L2715)

### `kl_divergence` function

Copied!

`tf_keras.losses.kl_divergence(y_true, y_pred)`

Computes Kullback-Leibler divergence loss between `y_true` & `y_pred`.

`loss = y_true * log(y_true / y_pred)`

See: https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler\_divergence

Standalone usage:

Copied!

`>>> y_true = np.random.randint(0, 2, size=(2, 3)).astype(np.float64) >>> y_pred = np.random.random(size=(2, 3)) >>> loss = tf.keras.losses.kullback_leibler_divergence(y_true, y_pred) >>> assert loss.shape == (2,) >>> y_true = tf.keras.backend.clip(y_true, 1e-7, 1) >>> y_pred = tf.keras.backend.clip(y_pred, 1e-7, 1) >>> assert np.array_equal( ...     loss.numpy(), np.sum(y_true * np.log(y_true / y_pred), axis=-1))`

**Arguments**

*   **y\_true**: Tensor of true targets.
*   **y\_pred**: Tensor of predicted targets.

**Returns**

A `Tensor` with loss.

**Raises**

*   **TypeError**: If `y_true` cannot be cast to the `y_pred.dtype`.

* * *

[Probabilistic losses](https://keras.io/2/api/losses/probabilistic_losses/#probabilistic-losses)

[`BinaryCrossentropy` class](https://keras.io/2/api/losses/probabilistic_losses/#binarycrossentropy-class)

[`CategoricalCrossentropy` class](https://keras.io/2/api/losses/probabilistic_losses/#categoricalcrossentropy-class)

[`SparseCategoricalCrossentropy` class](https://keras.io/2/api/losses/probabilistic_losses/#sparsecategoricalcrossentropy-class)

[`Poisson` class](https://keras.io/2/api/losses/probabilistic_losses/#poisson-class)

[`binary_crossentropy` function](https://keras.io/2/api/losses/probabilistic_losses/#binarycrossentropy-function)

[`categorical_crossentropy` function](https://keras.io/2/api/losses/probabilistic_losses/#categoricalcrossentropy-function)

[`sparse_categorical_crossentropy` function](https://keras.io/2/api/losses/probabilistic_losses/#sparsecategoricalcrossentropy-function)

[`poisson` function](https://keras.io/2/api/losses/probabilistic_losses/#poisson-function)

[`KLDivergence` class](https://keras.io/2/api/losses/probabilistic_losses/#kldivergence-class)

[`kl_divergence` function](https://keras.io/2/api/losses/probabilistic_losses/#kldivergence-function)