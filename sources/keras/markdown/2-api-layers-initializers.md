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
 / Layer weight initializers

Layer weight initializers
=========================

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/initializers/initializers.py#L365)

### `RandomNormal` class

Copied!

`tf_keras.initializers.RandomNormal(mean=0.0, stddev=0.05, seed=None)`

Initializer that generates tensors with a normal distribution.

Also available via the shortcut function [`tf.keras.initializers.random_normal`](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/random_normal)
.

**Examples**

Copied!

`>>> # Standalone usage: >>> initializer = tf.keras.initializers.RandomNormal(mean=0., stddev=1.) >>> values = initializer(shape=(2, 2))`

Copied!

`>>> # Usage in a TF-Keras layer: >>> initializer = tf.keras.initializers.RandomNormal(mean=0., stddev=1.) >>> layer = tf.keras.layers.Dense(3, kernel_initializer=initializer)`

**Arguments**

*   **mean**: a python scalar or a scalar tensor. Mean of the random values to generate.
*   **stddev**: a python scalar or a scalar tensor. Standard deviation of the random values to generate.
*   **seed**: A Python integer. Used to make the behavior of the initializer deterministic. Note that a seeded initializer will produce the same random values across multiple calls.

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/initializers/initializers.py#L282)

### `RandomUniform` class

Copied!

`tf_keras.initializers.RandomUniform(minval=-0.05, maxval=0.05, seed=None)`

Initializer that generates tensors with a uniform distribution.

Also available via the shortcut function [`tf.keras.initializers.random_uniform`](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/random_uniform)
.

**Examples**

Copied!

`>>> # Standalone usage: >>> initializer = tf.keras.initializers.RandomUniform(minval=0., maxval=1.) >>> values = initializer(shape=(2, 2))`

Copied!

`>>> # Usage in a TF-Keras layer: >>> initializer = tf.keras.initializers.RandomUniform(minval=0., maxval=1.) >>> layer = tf.keras.layers.Dense(3, kernel_initializer=initializer)`

**Arguments**

*   **minval**: A python scalar or a scalar tensor. Lower bound of the range of random values to generate (inclusive).
*   **maxval**: A python scalar or a scalar tensor. Upper bound of the range of random values to generate (exclusive).
*   **seed**: A Python integer. Used to make the behavior of the initializer deterministic. Note that a seeded initializer will produce the same random values across multiple calls.

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/initializers/initializers.py#L443)

### `TruncatedNormal` class

Copied!

`tf_keras.initializers.TruncatedNormal(mean=0.0, stddev=0.05, seed=None)`

Initializer that generates a truncated normal distribution.

Also available via the shortcut function [`tf.keras.initializers.truncated_normal`](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/truncated_normal)
.

The values generated are similar to values from a [`tf.keras.initializers.RandomNormal`](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/RandomNormal)
 initializer except that values more than two standard deviations from the mean are discarded and re-drawn.

**Examples**

Copied!

`>>> # Standalone usage: >>> initializer = tf.keras.initializers.TruncatedNormal(mean=0., stddev=1.) >>> values = initializer(shape=(2, 2))`

Copied!

`>>> # Usage in a TF-Keras layer: >>> initializer = tf.keras.initializers.TruncatedNormal(mean=0., stddev=1.) >>> layer = tf.keras.layers.Dense(3, kernel_initializer=initializer)`

**Arguments**

*   **mean**: a python scalar or a scalar tensor. Mean of the random values to generate.
*   **stddev**: a python scalar or a scalar tensor. Standard deviation of the random values to generate before truncation.
*   **seed**: A Python integer. Used to make the behavior of the initializer deterministic. Note that a seeded initializer will produce the same random values across multiple calls.

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/initializers/initializers.py#L133)

### `Zeros` class

Copied!

`tf_keras.initializers.Zeros()`

Initializer that generates tensors initialized to 0.

Also available via the shortcut function [`tf.keras.initializers.zeros`](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/zeros)
.

**Examples**

Copied!

`>>> # Standalone usage: >>> initializer = tf.keras.initializers.Zeros() >>> values = initializer(shape=(2, 2))`

Copied!

`>>> # Usage in a TF-Keras layer: >>> initializer = tf.keras.initializers.Zeros() >>> layer = tf.keras.layers.Dense(3, kernel_initializer=initializer)`

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/initializers/initializers.py#L175)

### `Ones` class

Copied!

`tf_keras.initializers.Ones()`

Initializer that generates tensors initialized to 1.

Also available via the shortcut function [`tf.keras.initializers.ones`](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/ones)
.

**Examples**

Copied!

`>>> # Standalone usage: >>> initializer = tf.keras.initializers.Ones() >>> values = initializer(shape=(2, 2))`

Copied!

`>>> # Usage in a TF-Keras layer: >>> initializer = tf.keras.initializers.Ones() >>> layer = tf.keras.layers.Dense(3, kernel_initializer=initializer)`

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/initializers/initializers.py#L893)

### `GlorotNormal` class

Copied!

`tf_keras.initializers.GlorotNormal(seed=None)`

The Glorot normal initializer, also called Xavier normal initializer.

Also available via the shortcut function [`tf.keras.initializers.glorot_normal`](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/glorot_normal)
.

Draws samples from a truncated normal distribution centered on 0 with `stddev = sqrt(2 / (fan_in + fan_out))` where `fan_in` is the number of input units in the weight tensor and `fan_out` is the number of output units in the weight tensor.

**Examples**

Copied!

`>>> # Standalone usage: >>> initializer = tf.keras.initializers.GlorotNormal() >>> values = initializer(shape=(2, 2))`

Copied!

`>>> # Usage in a TF-Keras layer: >>> initializer = tf.keras.initializers.GlorotNormal() >>> layer = tf.keras.layers.Dense(3, kernel_initializer=initializer)`

**Arguments**

*   **seed**: A Python integer. Used to make the behavior of the initializer deterministic. Note that a seeded initializer will not produce the same random values across multiple calls, but multiple initializers will produce the same sequence when constructed with the same seed value.

**References**

*   [Glorot et al., 2010](http://proceedings.mlr.press/v9/glorot10a.html)
    

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/initializers/initializers.py#L849)

### `GlorotUniform` class

Copied!

`tf_keras.initializers.GlorotUniform(seed=None)`

The Glorot uniform initializer, also called Xavier uniform initializer.

Also available via the shortcut function [`tf.keras.initializers.glorot_uniform`](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/glorot_uniform)
.

Draws samples from a uniform distribution within `[-limit, limit]`, where `limit = sqrt(6 / (fan_in + fan_out))` (`fan_in` is the number of input units in the weight tensor and `fan_out` is the number of output units).

**Examples**

Copied!

`>>> # Standalone usage: >>> initializer = tf.keras.initializers.GlorotUniform() >>> values = initializer(shape=(2, 2))`

Copied!

`>>> # Usage in a TF-Keras layer: >>> initializer = tf.keras.initializers.GlorotUniform() >>> layer = tf.keras.layers.Dense(3, kernel_initializer=initializer)`

**Arguments**

*   **seed**: A Python integer. Used to make the behavior of the initializer deterministic. Note that a seeded initializer will not produce the same random values across multiple calls, but multiple initializers will produce the same sequence when constructed with the same seed value.

**References**

*   [Glorot et al., 2010](http://proceedings.mlr.press/v9/glorot10a.html)
    

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/initializers/initializers.py#L1027)

### `HeNormal` class

Copied!

`tf_keras.initializers.HeNormal(seed=None)`

He normal initializer.

Also available via the shortcut function [`tf.keras.initializers.he_normal`](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/he_normal)
.

It draws samples from a truncated normal distribution centered on 0 with `stddev = sqrt(2 / fan_in)` where `fan_in` is the number of input units in the weight tensor.

**Examples**

Copied!

`>>> # Standalone usage: >>> initializer = tf.keras.initializers.HeNormal() >>> values = initializer(shape=(2, 2))`

Copied!

`>>> # Usage in a TF-Keras layer: >>> initializer = tf.keras.initializers.HeNormal() >>> layer = tf.keras.layers.Dense(3, kernel_initializer=initializer)`

**Arguments**

*   **seed**: A Python integer. Used to make the behavior of the initializer deterministic. Note that a seeded initializer will not produce the same random values across multiple calls, but multiple initializers will produce the same sequence when constructed with the same seed value.

**References**

*   [He et al., 2015](https://arxiv.org/abs/1502.01852)
    

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/initializers/initializers.py#L1069)

### `HeUniform` class

Copied!

`tf_keras.initializers.HeUniform(seed=None)`

He uniform variance scaling initializer.

Also available via the shortcut function [`tf.keras.initializers.he_uniform`](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/he_uniform)
.

Draws samples from a uniform distribution within `[-limit, limit]`, where `limit = sqrt(6 / fan_in)` (`fan_in` is the number of input units in the weight tensor).

**Examples**

Copied!

`>>> # Standalone usage: >>> initializer = tf.keras.initializers.HeUniform() >>> values = initializer(shape=(2, 2))`

Copied!

`>>> # Usage in a TF-Keras layer: >>> initializer = tf.keras.initializers.HeUniform() >>> layer = tf.keras.layers.Dense(3, kernel_initializer=initializer)`

**Arguments**

*   **seed**: A Python integer. Used to make the behavior of the initializer deterministic. Note that a seeded initializer will not produce the same random values across multiple calls, but multiple initializers will produce the same sequence when constructed with the same seed value.

**References**

*   [He et al., 2015](https://arxiv.org/abs/1502.01852)
    

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/initializers/initializers.py#L787)

### `Identity` class

Copied!

`tf_keras.initializers.Identity(gain=1.0)`

Initializer that generates the identity matrix.

Also available via the shortcut function [`tf.keras.initializers.identity`](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/identity)
.

Only usable for generating 2D matrices.

**Examples**

Copied!

`>>> # Standalone usage: >>> initializer = tf.keras.initializers.Identity() >>> values = initializer(shape=(2, 2))`

Copied!

`>>> # Usage in a TF-Keras layer: >>> initializer = tf.keras.initializers.Identity() >>> layer = tf.keras.layers.Dense(3, kernel_initializer=initializer)`

**Arguments**

*   **gain**: Multiplicative factor to apply to the identity matrix.

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/initializers/initializers.py#L686)

### `Orthogonal` class

Copied!

`tf_keras.initializers.Orthogonal(gain=1.0, seed=None)`

Initializer that generates an orthogonal matrix.

Also available via the shortcut function [`tf.keras.initializers.orthogonal`](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/orthogonal)
.

If the shape of the tensor to initialize is two-dimensional, it is initialized with an orthogonal matrix obtained from the QR decomposition of a matrix of random numbers drawn from a normal distribution. If the matrix has fewer rows than columns then the output will have orthogonal rows. Otherwise, the output will have orthogonal columns.

If the shape of the tensor to initialize is more than two-dimensional, a matrix of shape `(shape[0] * ... * shape[n - 2], shape[n - 1])` is initialized, where `n` is the length of the shape vector. The matrix is subsequently reshaped to give a tensor of the desired shape.

**Examples**

Copied!

`>>> # Standalone usage: >>> initializer = tf.keras.initializers.Orthogonal() >>> values = initializer(shape=(2, 2))`

Copied!

`>>> # Usage in a TF-Keras layer: >>> initializer = tf.keras.initializers.Orthogonal() >>> layer = tf.keras.layers.Dense(3, kernel_initializer=initializer)`

**Arguments**

*   **gain**: multiplicative factor to apply to the orthogonal matrix
*   **seed**: A Python integer. Used to make the behavior of the initializer deterministic. Note that a seeded initializer will produce the same random values across multiple calls.

**References**

*   [Saxe et al., 2014](https://openreview.net/forum?id=_wzZwKpTDF_9C)
    

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/initializers/initializers.py#L217)

### `Constant` class

Copied!

`tf_keras.initializers.Constant(value=0)`

Initializer that generates tensors with constant values.

Also available via the shortcut function [`tf.keras.initializers.constant`](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/constant)
.

Only scalar values are allowed. The constant value provided must be convertible to the dtype requested when calling the initializer.

**Examples**

Copied!

`>>> # Standalone usage: >>> initializer = tf.keras.initializers.Constant(3.) >>> values = initializer(shape=(2, 2))`

Copied!

`>>> # Usage in a TF-Keras layer: >>> initializer = tf.keras.initializers.Constant(3.) >>> layer = tf.keras.layers.Dense(3, kernel_initializer=initializer)`

**Arguments**

*   **value**: A Python scalar.

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/initializers/initializers.py#L533)

### `VarianceScaling` class

Copied!

`tf_keras.initializers.VarianceScaling(     scale=1.0, mode="fan_in", distribution="truncated_normal", seed=None )`

Initializer that adapts its scale to the shape of its input tensors.

Also available via the shortcut function [`tf.keras.initializers.variance_scaling`](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/variance_scaling)
.

With `distribution="truncated_normal" or "untruncated_normal"`, samples are drawn from a truncated/untruncated normal distribution with a mean of zero and a standard deviation (after truncation, if used) `stddev = sqrt(scale / n)`, where `n` is:

*   number of input units in the weight tensor, if `mode="fan_in"`
*   number of output units, if `mode="fan_out"`
*   average of the numbers of input and output units, if `mode="fan_avg"`

With `distribution="uniform"`, samples are drawn from a uniform distribution within `[-limit, limit]`, where `limit = sqrt(3 * scale / n)`.

**Examples**

Copied!

`>>> # Standalone usage: >>> initializer = tf.keras.initializers.VarianceScaling( ... scale=0.1, mode='fan_in', distribution='uniform') >>> values = initializer(shape=(2, 2))`

Copied!

`>>> # Usage in a TF-Keras layer: >>> initializer = tf.keras.initializers.VarianceScaling( ... scale=0.1, mode='fan_in', distribution='uniform') >>> layer = tf.keras.layers.Dense(3, kernel_initializer=initializer)`

**Arguments**

*   **scale**: Scaling factor (positive float).
*   **mode**: One of `"fan_in"`, `"fan_out"`, `"fan_avg"`.
*   **distribution**: Random distribution to use. One of `"truncated_normal"`, `"untruncated_normal"`, or `"uniform"`.
*   **seed**: A Python integer. Used to make the behavior of the initializer deterministic. Note that a seeded initializer will produce the same random values across multiple calls.

* * *

[Layer weight initializers](https://keras.io/2/api/layers/initializers/#layer-weight-initializers)

[`RandomNormal` class](https://keras.io/2/api/layers/initializers/#randomnormal-class)

[`RandomUniform` class](https://keras.io/2/api/layers/initializers/#randomuniform-class)

[`TruncatedNormal` class](https://keras.io/2/api/layers/initializers/#truncatednormal-class)

[`Zeros` class](https://keras.io/2/api/layers/initializers/#zeros-class)

[`Ones` class](https://keras.io/2/api/layers/initializers/#ones-class)

[`GlorotNormal` class](https://keras.io/2/api/layers/initializers/#glorotnormal-class)

[`GlorotUniform` class](https://keras.io/2/api/layers/initializers/#glorotuniform-class)

[`HeNormal` class](https://keras.io/2/api/layers/initializers/#henormal-class)

[`HeUniform` class](https://keras.io/2/api/layers/initializers/#heuniform-class)

[`Identity` class](https://keras.io/2/api/layers/initializers/#identity-class)

[`Orthogonal` class](https://keras.io/2/api/layers/initializers/#orthogonal-class)

[`Constant` class](https://keras.io/2/api/layers/initializers/#constant-class)

[`VarianceScaling` class](https://keras.io/2/api/layers/initializers/#variancescaling-class)