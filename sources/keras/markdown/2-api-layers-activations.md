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
 / Layer activations

Layer activations
=================

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/activations.py#L268)

### `relu` function

Copied!

`tf_keras.activations.relu(x, alpha=0.0, max_value=None, threshold=0.0)`

Applies the rectified linear unit activation function.

With default values, this returns the standard ReLU activation: `max(x, 0)`, the element-wise maximum of 0 and the input tensor.

Modifying default parameters allows you to use non-zero thresholds, change the max value of the activation, and to use a non-zero multiple of the input for values below the threshold.

**Example**

Copied!

`>>> foo = tf.constant([-10, -5, 0.0, 5, 10], dtype = tf.float32) >>> tf.keras.activations.relu(foo).numpy() array([ 0.,  0.,  0.,  5., 10.], dtype=float32) >>> tf.keras.activations.relu(foo, alpha=0.5).numpy() array([-5. , -2.5,  0. ,  5. , 10. ], dtype=float32) >>> tf.keras.activations.relu(foo, max_value=5.).numpy() array([0., 0., 0., 5., 5.], dtype=float32) >>> tf.keras.activations.relu(foo, threshold=5.).numpy() array([-0., -0.,  0.,  0., 10.], dtype=float32)`

**Arguments**

*   **x**: Input `tensor` or `variable`.
*   **alpha**: A `float` that governs the slope for values lower than the threshold.
*   **max\_value**: A `float` that sets the saturation threshold (the largest value the function will return).
*   **threshold**: A `float` giving the threshold value of the activation function below which values will be damped or set to zero.

**Returns**

A `Tensor` representing the input tensor, transformed by the relu activation function. Tensor will be of the same shape and dtype of input `x`.

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/activations.py#L373)

### `sigmoid` function

Copied!

`tf_keras.activations.sigmoid(x)`

Sigmoid activation function, `sigmoid(x) = 1 / (1 + exp(-x))`.

Applies the sigmoid activation function. For small values (<-5), `sigmoid` returns a value close to zero, and for large values (>5) the result of the function gets close to 1.

Sigmoid is equivalent to a 2-element Softmax, where the second element is assumed to be zero. The sigmoid function always returns a value between 0 and 1.

**Example**

Copied!

`>>> a = tf.constant([-20, -1.0, 0.0, 1.0, 20], dtype = tf.float32) >>> b = tf.keras.activations.sigmoid(a) >>> b.numpy() array([2.0611537e-09, 2.6894143e-01, 5.0000000e-01, 7.3105860e-01,          1.0000000e+00], dtype=float32)`

**Arguments**

*   **x**: Input tensor.

**Returns**

*   **Tensor with the sigmoid activation**: `1 / (1 + exp(-x))`.

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/activations.py#L46)

### `softmax` function

Copied!

`tf_keras.activations.softmax(x, axis=-1)`

Softmax converts a vector of values to a probability distribution.

The elements of the output vector are in range (0, 1) and sum to 1.

Each vector is handled independently. The `axis` argument sets which axis of the input the function is applied along.

Softmax is often used as the activation for the last layer of a classification network because the result could be interpreted as a probability distribution.

The softmax of each vector x is computed as `exp(x) / tf.reduce_sum(exp(x))`.

The input values in are the log-odds of the resulting probability.

**Arguments**

*   \_\_x \_\_: Input tensor.
*   **axis**: Integer, axis along which the softmax normalization is applied.

**Returns**

Tensor, output of softmax transformation (all values are non-negative and sum to 1).

**Examples**

**Example 1: standalone usage**

Copied!

`>>> inputs = tf.random.normal(shape=(32, 10)) >>> outputs = tf.keras.activations.softmax(inputs) >>> tf.reduce_sum(outputs[0, :])  # Each sample in the batch now sums to 1 <tf.Tensor: shape=(), dtype=float32, numpy=1.0000001>`

**Example 2: usage in a `Dense` layer**

Copied!

`>>> layer = tf.keras.layers.Dense(32, ...                               activation=tf.keras.activations.softmax)`

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/activations.py#L194)

### `softplus` function

Copied!

`tf_keras.activations.softplus(x)`

Softplus activation function, `softplus(x) = log(exp(x) + 1)`.

Example Usage:

Copied!

`>>> a = tf.constant([-20, -1.0, 0.0, 1.0, 20], dtype = tf.float32) >>> b = tf.keras.activations.softplus(a) >>> b.numpy() array([2.0611537e-09, 3.1326166e-01, 6.9314718e-01, 1.3132616e+00,          2.0000000e+01], dtype=float32)`

**Arguments**

*   **x**: Input tensor.

**Returns**

*   **The softplus activation**: `log(exp(x) + 1)`.

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/activations.py#L216)

### `softsign` function

Copied!

`tf_keras.activations.softsign(x)`

Softsign activation function, `softsign(x) = x / (abs(x) + 1)`.

Example Usage:

Copied!

`>>> a = tf.constant([-1.0, 0.0, 1.0], dtype = tf.float32) >>> b = tf.keras.activations.softsign(a) >>> b.numpy() array([-0.5,  0. ,  0.5], dtype=float32)`

**Arguments**

*   **x**: Input tensor.

**Returns**

*   **The softsign activation**: `x / (abs(x) + 1)`.

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/activations.py#L351)

### `tanh` function

Copied!

`tf_keras.activations.tanh(x)`

Hyperbolic tangent activation function.

**Example**

Copied!

`>>> a = tf.constant([-3.0, -1.0, 0.0, 1.0, 3.0], dtype = tf.float32) >>> b = tf.keras.activations.tanh(a) >>> b.numpy() array([-0.9950547, -0.7615942,  0.,  0.7615942,  0.9950547], dtype=float32)`

**Arguments**

*   **x**: Input tensor.

**Returns**

*   **Tensor of same shape and dtype of input `x`, with tanh activation**: `tanh(x) = sinh(x)/cosh(x) = ((exp(x) - exp(-x))/(exp(x) + exp(-x)))`.

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/activations.py#L140)

### `selu` function

Copied!

`tf_keras.activations.selu(x)`

Scaled Exponential Linear Unit (SELU).

The Scaled Exponential Linear Unit (SELU) activation function is defined as:

*   `if x > 0: return scale * x`
*   `if x < 0: return scale * alpha * (exp(x) - 1)`

where `alpha` and `scale` are pre-defined constants (`alpha=1.67326324` and `scale=1.05070098`).

Basically, the SELU activation function multiplies `scale` (> 1) with the output of the [`tf.keras.activations.elu`](https://www.tensorflow.org/api_docs/python/tf/keras/activations/elu)
 function to ensure a slope larger than one for positive inputs.

The values of `alpha` and `scale` are chosen so that the mean and variance of the inputs are preserved between two consecutive layers as long as the weights are initialized correctly (see [`tf.keras.initializers.LecunNormal`](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/LecunNormal)
 initializer) and the number of input units is "large enough" (see reference paper for more information).

Example Usage:

Copied!

`>>> num_classes = 10  # 10-class problem >>> model = tf.keras.Sequential() >>> model.add(tf.keras.layers.Dense(64, kernel_initializer='lecun_normal', ...                                 activation='selu')) >>> model.add(tf.keras.layers.Dense(32, kernel_initializer='lecun_normal', ...                                 activation='selu')) >>> model.add(tf.keras.layers.Dense(16, kernel_initializer='lecun_normal', ...                                 activation='selu')) >>> model.add(tf.keras.layers.Dense(num_classes, activation='softmax'))`

**Arguments**

*   **x**: A tensor or variable to compute the activation function for.

**Returns**

*   **The scaled exponential unit activation**: `scale * elu(x, alpha)`.

Notes: - To be used together with the [`tf.keras.initializers.LecunNormal`](https://www.tensorflow.org/api_docs/python/tf/keras/initializers/LecunNormal)
 initializer. - To be used together with the dropout variant [`tf.keras.layers.AlphaDropout`](https://www.tensorflow.org/api_docs/python/tf/keras/layers/AlphaDropout)
 (not regular dropout).

**References**

*   [Klambauer et al., 2017](https://arxiv.org/abs/1706.02515)
    

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/activations.py#L90)

### `elu` function

Copied!

`tf_keras.activations.elu(x, alpha=1.0)`

Exponential Linear Unit.

The exponential linear unit (ELU) with `alpha > 0` is: `x` if `x > 0` and `alpha * (exp(x) - 1)` if `x < 0` The ELU hyperparameter `alpha` controls the value to which an ELU saturates for negative net inputs. ELUs diminish the vanishing gradient effect.

ELUs have negative values which pushes the mean of the activations closer to zero. Mean activations that are closer to zero enable faster learning as they bring the gradient closer to the natural gradient. ELUs saturate to a negative value when the argument gets smaller. Saturation means a small derivative which decreases the variation and the information that is propagated to the next layer.

Example Usage:

Copied!

`>>> import tensorflow as tf >>> model = tf.keras.Sequential() >>> model.add(tf.keras.layers.Conv2D(32, (3, 3), activation='elu', ...          input_shape=(28, 28, 1))) >>> model.add(tf.keras.layers.MaxPooling2D((2, 2))) >>> model.add(tf.keras.layers.Conv2D(64, (3, 3), activation='elu')) >>> model.add(tf.keras.layers.MaxPooling2D((2, 2))) >>> model.add(tf.keras.layers.Conv2D(64, (3, 3), activation='elu'))`

**Arguments**

*   **x**: Input tensor.
*   **alpha**: A scalar, slope of negative section. `alpha` controls the value to which an ELU saturates for negative net inputs.

**Returns**

*   **The exponential linear unit (ELU) activation function**: `x` if `x > 0` and `alpha * (exp(x) - 1)` if `x < 0`.

**Reference**

*   [Fast and Accurate Deep Network Learning by Exponential Linear Units (ELUs) (Clevert et al, 2016)](https://arxiv.org/abs/1511.07289)
    

* * *

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/activations.py#L403)

### `exponential` function

Copied!

`tf_keras.activations.exponential(x)`

Exponential activation function.

**Example**

Copied!

`>>> a = tf.constant([-3.0, -1.0, 0.0, 1.0, 3.0], dtype = tf.float32) >>> b = tf.keras.activations.exponential(a) >>> b.numpy() array([0.04978707,  0.36787945,  1.,  2.7182817 , 20.085537], dtype=float32)`

**Arguments**

*   **x**: Input tensor.

**Returns**

*   **Tensor with exponential activation**: `exp(x)`.

* * *

[Layer activations](https://keras.io/2/api/layers/activations/#layer-activations)

[`relu` function](https://keras.io/2/api/layers/activations/#relu-function)

[`sigmoid` function](https://keras.io/2/api/layers/activations/#sigmoid-function)

[`softmax` function](https://keras.io/2/api/layers/activations/#softmax-function)

[`softplus` function](https://keras.io/2/api/layers/activations/#softplus-function)

[`softsign` function](https://keras.io/2/api/layers/activations/#softsign-function)

[`tanh` function](https://keras.io/2/api/layers/activations/#tanh-function)

[`selu` function](https://keras.io/2/api/layers/activations/#selu-function)

[`elu` function](https://keras.io/2/api/layers/activations/#elu-function)

[`exponential` function](https://keras.io/2/api/layers/activations/#exponential-function)