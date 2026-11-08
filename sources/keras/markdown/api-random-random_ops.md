None

[Keras 3 API documentation](https://keras.io/api/)

[Models API](https://keras.io/api/models/)
 [Layers API](https://keras.io/api/layers/)
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
 [SeedGenerator class](https://keras.io/api/random/seed_generator/)
 [Random operations](https://keras.io/api/random/random_ops/)
 [Quantizers](https://keras.io/api/quantizers/)
 [Scope](https://keras.io/api/scope/)
 [Rematerialization](https://keras.io/api/rematerialization/)
 [Utilities](https://keras.io/api/utils/)

[Keras 2 API documentation](https://keras.io/2/api/)

► [Keras 3 API documentation](https://keras.io/api/)
 / [RNG API](https://keras.io/api/random/)
 / Random operations

Random operations
=================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/random/random.py#L312)

### `beta` function

Copied!

`keras.random.beta(shape, alpha, beta, dtype=None, seed=None)`

Draw samples from a Beta distribution.

The values are drawn from a Beta distribution parametrized by alpha and beta.

**Arguments**

*   **shape**: The shape of the random values to generate.
*   **alpha**: Float or an array of floats representing the first parameter alpha. Must be broadcastable with `beta` and `shape`.
*   **beta**: Float or an array of floats representing the second parameter beta. Must be broadcastable with `alpha` and `shape`.
*   **dtype**: Optional dtype of the tensor. Only floating point types are supported. If not specified, `keras.config.floatx()` is used, which defaults to `float32` unless you configured it otherwise (via `keras.config.set_floatx(float_dtype)`).
*   **seed**: Optional Python integer or instance of [`keras.random.SeedGenerator`](https://keras.io/api/random/seed_generator#seedgenerator-class)
    . By default, the `seed` argument is `None`, and an internal global [`keras.random.SeedGenerator`](https://keras.io/api/random/seed_generator#seedgenerator-class)
     is used. The `seed` argument can be used to ensure deterministic (repeatable) random number generation. Note that passing an integer as the `seed` value will produce the same random values for each call. To generate different random values for repeated calls, an instance of [`keras.random.SeedGenerator`](https://keras.io/api/random/seed_generator#seedgenerator-class)
     must be provided as the `seed` value. Remark concerning the JAX backend: When tracing functions with the JAX backend the global [`keras.random.SeedGenerator`](https://keras.io/api/random/seed_generator#seedgenerator-class)
     is not supported. Therefore, during tracing the default value seed=None will produce an error, and a `seed` argument must be provided.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/random/random.py#L271)

### `binomial` function

Copied!

`keras.random.binomial(shape, counts, probabilities, dtype=None, seed=None)`

Draw samples from a Binomial distribution.

The values are drawn from a Binomial distribution with specified trial count and probability of success.

**Arguments**

*   **shape**: The shape of the random values to generate.
*   **counts**: A number or array of numbers representing the number of trials. It must be broadcastable with `probabilities`.
*   **probabilities**: A float or array of floats representing the probability of success of an individual event. It must be broadcastable with `counts`.
*   **dtype**: Optional dtype of the tensor. Only floating point types are supported. If not specified, `keras.config.floatx()` is used, which defaults to `float32` unless you configured it otherwise (via `keras.config.set_floatx(float_dtype)`).
*   **seed**: Optional Python integer or instance of [`keras.random.SeedGenerator`](https://keras.io/api/random/seed_generator#seedgenerator-class)
    . By default, the `seed` argument is `None`, and an internal global [`keras.random.SeedGenerator`](https://keras.io/api/random/seed_generator#seedgenerator-class)
     is used. The `seed` argument can be used to ensure deterministic (repeatable) random number generation. Note that passing an integer as the `seed` value will produce the same random values for each call. To generate different random values for repeated calls, an instance of [`keras.random.SeedGenerator`](https://keras.io/api/random/seed_generator#seedgenerator-class)
     must be provided as the `seed` value. Remark concerning the JAX backend: When tracing functions with the JAX backend the global [`keras.random.SeedGenerator`](https://keras.io/api/random/seed_generator#seedgenerator-class)
     is not supported. Therefore, during tracing the default value seed=None will produce an error, and a `seed` argument must be provided.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/random/random.py#L37)

### `categorical` function

Copied!

`keras.random.categorical(logits, num_samples, dtype="int32", seed=None)`

Draws samples from a categorical distribution.

This function takes as input `logits`, a 2-D input tensor with shape (batch\_size, num\_classes). Each row of the input represents a categorical distribution, with each column index containing the log-probability for a given class.

The function will output a 2-D tensor with shape (batch\_size, num\_samples), where each row contains samples from the corresponding row in `logits`. Each column index contains an independent samples drawn from the input distribution.

**Arguments**

*   **logits**: 2-D Tensor with shape (batch\_size, num\_classes). Each row should define a categorical distribution with the unnormalized log-probabilities for all classes.
*   **num\_samples**: Int, the number of independent samples to draw for each row of the input. This will be the second dimension of the output tensor's shape.
*   **dtype**: Optional dtype of the output tensor.
*   **seed**: Optional Python integer or instance of [`keras.random.SeedGenerator`](https://keras.io/api/random/seed_generator#seedgenerator-class)
    . By default, the `seed` argument is `None`, and an internal global [`keras.random.SeedGenerator`](https://keras.io/api/random/seed_generator#seedgenerator-class)
     is used. The `seed` argument can be used to ensure deterministic (repeatable) random number generation. Note that passing an integer as the `seed` value will produce the same random values for each call. To generate different random values for repeated calls, an instance of [`keras.random.SeedGenerator`](https://keras.io/api/random/seed_generator#seedgenerator-class)
     must be provided as the `seed` value. Remark concerning the JAX backend: When tracing functions with the JAX backend the global [`keras.random.SeedGenerator`](https://keras.io/api/random/seed_generator#seedgenerator-class)
     is not supported. Therefore, during tracing the default value seed=None will produce an error, and a `seed` argument must be provided.

**Returns**

A 2-D tensor with (batch\_size, num\_samples).

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/random/random.py#L211)

### `dropout` function

Copied!

`keras.random.dropout(inputs, rate, noise_shape=None, seed=None)`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/random/random.py#L243)

### `gamma` function

Copied!

`keras.random.gamma(shape, alpha, dtype=None, seed=None)`

Draw random samples from the Gamma distribution.

**Arguments**

*   **shape**: The shape of the random values to generate.
*   **alpha**: Float, the parameter of the distribution.
*   **dtype**: Optional dtype of the tensor. Only floating point types are supported. If not specified, `keras.config.floatx()` is used, which defaults to `float32` unless you configured it otherwise (via `keras.config.set_floatx(float_dtype)`).
*   **seed**: Optional Python integer or instance of [`keras.random.SeedGenerator`](https://keras.io/api/random/seed_generator#seedgenerator-class)
    . By default, the `seed` argument is `None`, and an internal global [`keras.random.SeedGenerator`](https://keras.io/api/random/seed_generator#seedgenerator-class)
     is used. The `seed` argument can be used to ensure deterministic (repeatable) random number generation. Note that passing an integer as the `seed` value will produce the same random values for each call. To generate different random values for repeated calls, an instance of [`keras.random.SeedGenerator`](https://keras.io/api/random/seed_generator#seedgenerator-class)
     must be provided as the `seed` value. Remark concerning the JAX backend: When tracing functions with the JAX backend the global [`keras.random.SeedGenerator`](https://keras.io/api/random/seed_generator#seedgenerator-class)
     is not supported. Therefore, during tracing the default value seed=None will produce an error, and a `seed` argument must be provided.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/random/random.py#L5)

### `normal` function

Copied!

`keras.random.normal(shape, mean=0.0, stddev=1.0, dtype=None, seed=None)`

Draw random samples from a normal (Gaussian) distribution.

**Arguments**

*   **shape**: The shape of the random values to generate.
*   **mean**: Float, defaults to 0. Mean of the random values to generate.
*   **stddev**: Float, defaults to 1. Standard deviation of the random values to generate.
*   **dtype**: Optional dtype of the tensor. Only floating point types are supported. If not specified, `keras.config.floatx()` is used, which defaults to `float32` unless you configured it otherwise (via `keras.config.set_floatx(float_dtype)`).
*   **seed**: Optional Python integer or instance of [`keras.random.SeedGenerator`](https://keras.io/api/random/seed_generator#seedgenerator-class)
    . By default, the `seed` argument is `None`, and an internal global [`keras.random.SeedGenerator`](https://keras.io/api/random/seed_generator#seedgenerator-class)
     is used. The `seed` argument can be used to ensure deterministic (repeatable) random number generation. Note that passing an integer as the `seed` value will produce the same random values for each call. To generate different random values for repeated calls, an instance of [`keras.random.SeedGenerator`](https://keras.io/api/random/seed_generator#seedgenerator-class)
     must be provided as the `seed` value. Remark concerning the JAX backend: When tracing functions with the JAX backend the global [`keras.random.SeedGenerator`](https://keras.io/api/random/seed_generator#seedgenerator-class)
     is not supported. Therefore, during tracing the default value `seed=None` will produce an error, and a `seed` argument must be provided.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/random/random.py#L131)

### `randint` function

Copied!

`keras.random.randint(shape, minval, maxval, dtype="int32", seed=None)`

Draw random integers from a uniform distribution.

The generated values follow a uniform distribution in the range `[minval, maxval)`. The lower bound `minval` is included in the range, while the upper bound `maxval` is excluded.\
\
`dtype` must be an integer type.\
\
**Arguments**\
\
*   **shape**: The shape of the random values to generate.\
*   **minval**: Float, defaults to 0. Lower bound of the range of random values to generate (inclusive).\
*   **maxval**: Float, defaults to 1. Upper bound of the range of random values to generate (exclusive).\
*   **dtype**: Optional dtype of the tensor. Only integer types are supported. If not specified, `keras.config.floatx()` is used, which defaults to `float32` unless you configured it otherwise (via `keras.config.set_floatx(float_dtype)`)\
*   **seed**: Optional Python integer or instance of [`keras.random.SeedGenerator`](https://keras.io/api/random/seed_generator#seedgenerator-class)\
    . By default, the `seed` argument is `None`, and an internal global [`keras.random.SeedGenerator`](https://keras.io/api/random/seed_generator#seedgenerator-class)\
     is used. The `seed` argument can be used to ensure deterministic (repeatable) random number generation. Note that passing an integer as the `seed` value will produce the same random values for each call. To generate different random values for repeated calls, an instance of [`keras.random.SeedGenerator`](https://keras.io/api/random/seed_generator#seedgenerator-class)\
     must be provided as the `seed` value. Remark concerning the JAX backend: When tracing functions with the JAX backend the global [`keras.random.SeedGenerator`](https://keras.io/api/random/seed_generator#seedgenerator-class)\
     is not supported. Therefore, during tracing the default value seed=None will produce an error, and a `seed` argument must be provided.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/random/random.py#L218)\
\
### `shuffle` function\
\
Copied!\
\
`keras.random.shuffle(x, axis=0, seed=None)`\
\
Shuffle the elements of a tensor uniformly at random along an axis.\
\
**Arguments**\
\
*   **x**: The tensor to be shuffled.\
*   **axis**: An integer specifying the axis along which to shuffle. Defaults to `0`.\
*   **seed**: Optional Python integer or instance of [`keras.random.SeedGenerator`](https://keras.io/api/random/seed_generator#seedgenerator-class)\
    . By default, the `seed` argument is `None`, and an internal global [`keras.random.SeedGenerator`](https://keras.io/api/random/seed_generator#seedgenerator-class)\
     is used. The `seed` argument can be used to ensure deterministic (repeatable) random number generation. Note that passing an integer as the `seed` value will produce the same random values for each call. To generate different random values for repeated calls, an instance of [`keras.random.SeedGenerator`](https://keras.io/api/random/seed_generator#seedgenerator-class)\
     must be provided as the `seed` value. Remark concerning the JAX backend: When tracing functions with the JAX backend the global [`keras.random.SeedGenerator`](https://keras.io/api/random/seed_generator#seedgenerator-class)\
     is not supported. Therefore, during tracing the default value seed=None will produce an error, and a `seed` argument must be provided.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/random/random.py#L175)\
\
### `truncated_normal` function\
\
Copied!\
\
`keras.random.truncated_normal(shape, mean=0.0, stddev=1.0, dtype=None, seed=None)`\
\
Draw samples from a truncated normal distribution.\
\
The values are drawn from a normal distribution with specified mean and standard deviation, discarding and re-drawing any samples that are more than two standard deviations from the mean.\
\
**Arguments**\
\
*   **shape**: The shape of the random values to generate.\
*   **mean**: Float, defaults to 0. Mean of the random values to generate.\
*   **stddev**: Float, defaults to 1. Standard deviation of the random values to generate.\
*   **dtype**: Optional dtype of the tensor. Only floating point types are supported. If not specified, `keras.config.floatx()` is used, which defaults to `float32` unless you configured it otherwise (via `keras.config.set_floatx(float_dtype)`)\
*   **seed**: Optional Python integer or instance of [`keras.random.SeedGenerator`](https://keras.io/api/random/seed_generator#seedgenerator-class)\
    . By default, the `seed` argument is `None`, and an internal global [`keras.random.SeedGenerator`](https://keras.io/api/random/seed_generator#seedgenerator-class)\
     is used. The `seed` argument can be used to ensure deterministic (repeatable) random number generation. Note that passing an integer as the `seed` value will produce the same random values for each call. To generate different random values for repeated calls, an instance of [`keras.random.SeedGenerator`](https://keras.io/api/random/seed_generator#seedgenerator-class)\
     must be provided as the `seed` value. Remark concerning the JAX backend: When tracing functions with the JAX backend the global [`keras.random.SeedGenerator`](https://keras.io/api/random/seed_generator#seedgenerator-class)\
     is not supported. Therefore, during tracing the default value seed=None will produce an error, and a `seed` argument must be provided.\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/random/random.py#L87)\
\
### `uniform` function\
\
Copied!\
\
`keras.random.uniform(shape, minval=0.0, maxval=1.0, dtype=None, seed=None)`\
\
Draw samples from a uniform distribution.\
\
The generated values follow a uniform distribution in the range `[minval, maxval)`. The lower bound `minval` is included in the range, while the upper bound `maxval` is excluded.\
\
`dtype` must be a floating point type, the default range is `[0, 1)`.\
\
**Arguments**\
\
*   **shape**: The shape of the random values to generate.\
*   **minval**: Float, defaults to 0. Lower bound of the range of random values to generate (inclusive).\
*   **maxval**: Float, defaults to 1. Upper bound of the range of random values to generate (exclusive).\
*   **dtype**: Optional dtype of the tensor. Only floating point types are supported. If not specified, `keras.config.floatx()` is used, which defaults to `float32` unless you configured it otherwise (via `keras.config.set_floatx(float_dtype)`)\
*   **seed**: Optional Python integer or instance of [`keras.random.SeedGenerator`](https://keras.io/api/random/seed_generator#seedgenerator-class)\
    . By default, the `seed` argument is `None`, and an internal global [`keras.random.SeedGenerator`](https://keras.io/api/random/seed_generator#seedgenerator-class)\
     is used. The `seed` argument can be used to ensure deterministic (repeatable) random number generation. Note that passing an integer as the `seed` value will produce the same random values for each call. To generate different random values for repeated calls, an instance of [`keras.random.SeedGenerator`](https://keras.io/api/random/seed_generator#seedgenerator-class)\
     must be provided as the `seed` value. Remark concerning the JAX backend: When tracing functions with the JAX backend the global [`keras.random.SeedGenerator`](https://keras.io/api/random/seed_generator#seedgenerator-class)\
     is not supported. Therefore, during tracing the default value seed=None will produce an error, and a `seed` argument must be provided.\
\
* * *\
\
[Random operations](https://keras.io/api/random/random_ops/#random-operations)\
\
[`beta` function](https://keras.io/api/random/random_ops/#beta-function)\
\
[`binomial` function](https://keras.io/api/random/random_ops/#binomial-function)\
\
[`categorical` function](https://keras.io/api/random/random_ops/#categorical-function)\
\
[`dropout` function](https://keras.io/api/random/random_ops/#dropout-function)\
\
[`gamma` function](https://keras.io/api/random/random_ops/#gamma-function)\
\
[`normal` function](https://keras.io/api/random/random_ops/#normal-function)\
\
[`randint` function](https://keras.io/api/random/random_ops/#randint-function)\
\
[`shuffle` function](https://keras.io/api/random/random_ops/#shuffle-function)\
\
[`truncated_normal` function](https://keras.io/api/random/random_ops/#truncatednormal-function)\
\
[`uniform` function](https://keras.io/api/random/random_ops/#uniform-function)