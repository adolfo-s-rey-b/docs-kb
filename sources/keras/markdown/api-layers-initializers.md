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
 / Layer weight initializers

Layer weight initializers
=========================

Usage of initializers
---------------------

Initializers define the way to set the initial random weights of Keras layers.

The keyword arguments used for passing initializers to layers depends on the layer. Usually, it is simply `kernel_initializer` and `bias_initializer`:

Copied!

`from keras import layers from keras import initializers  layer = layers.Dense(     units=64,     kernel_initializer=initializers.RandomNormal(stddev=0.01),     bias_initializer=initializers.Zeros() )`

All built-in initializers can also be passed via their string identifier:

Copied!

`layer = layers.Dense(     units=64,     kernel_initializer='random_normal',     bias_initializer='zeros' )`

* * *

Available initializers
----------------------

The following built-in initializers are available as part of the `keras.initializers` module:

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/initializers/initializer.py#L4)

### `Initializer` class

Copied!

`keras.Initializer()`

Initializer base class: all Keras initializers inherit from this class.

Initializers should implement a `__call__()` method with one of two possible signatures. If your initializer does not handle distribution layouts, it should use this signature:

Copied!

``def __call__(self, shape, dtype=None):     # returns a tensor of shape `shape` and dtype `dtype`     # containing values drawn using a function of your choice.``

If your initializer handles distribution layouts, it should use this signature. `layout` can either be a [`keras.distribution.TensorLayout`](https://keras.io/api/distribution/layout_map#tensorlayout-class)
 or a backend-specific layout. If the given `layout` is not `None`, the returned value must be distributed according to `layout`.

Copied!

``def __call__(self, shape, dtype=None, layout=None):     # returns a tensor of shape `shape`, dtype `dtype` and distributed     # across devices according to the layout `layout`.     # containing values drawn using a function of your choice.``

Optionally, you can also implement the method `get_config()` and the class method `from_config` in order to support serialization, just like with any Keras object.

Here's a simple example: a random normal initializer.

Copied!

`class ExampleRandomNormal(Initializer):     def __init__(self, mean, stddev):         self.mean = mean         self.stddev = stddev      def __call__(self, shape, dtype=None):         return keras.random.normal(             shape, mean=self.mean, stddev=self.stddev, dtype=dtype         )      def get_config(self):  # To support serialization         return {"mean": self.mean, "stddev": self.stddev}`

Note that we don't have to implement `from_config()` in the example above since the constructor arguments of the class the keys in the config returned by `get_config()` are the same. In this case, the default `from_config()` works fine.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/initializers/random_initializers.py#L30)

### `RandomNormal` class

Copied!

`keras.initializers.RandomNormal(mean=0.0, stddev=0.05, seed=None)`

Random normal initializer.

Draws samples from a normal distribution for given parameters.

**Examples**

Copied!

`>>> # Standalone usage: >>> initializer = RandomNormal(mean=0.0, stddev=1.0) >>> values = initializer(shape=(2, 2))`

Copied!

`>>> # Usage in a Keras layer: >>> initializer = RandomNormal(mean=0.0, stddev=1.0) >>> layer = Dense(3, kernel_initializer=initializer)`

**Arguments**

*   **mean**: A python scalar or a scalar keras tensor. Mean of the random values to generate.
*   **stddev**: A python scalar or a scalar keras tensor. Standard deviation of the random values to generate.
*   **seed**: A Python integer or instance of `keras.backend.SeedGenerator`. Used to make the behavior of the initializer deterministic. Note that an initializer seeded with an integer or `None` (unseeded) will produce the same random values across multiple calls. To get different random values across multiple calls, use as seed an instance of `keras.backend.SeedGenerator`.

**Guides and examples using `RandomNormal`**

*   [Class Attention Image Transformers with LayerScale](https://keras.io/examples/vision/cait/)
    
*   [Electroencephalogram Signal Classification for Brain-Computer Interface](https://keras.io/examples/timeseries/eeg_bci_ssvepformer/)
    
*   [CycleGAN](https://keras.io/examples/generative/cyclegan/)
    

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/initializers/random_initializers.py#L145)

### `RandomUniform` class

Copied!

`keras.initializers.RandomUniform(minval=-0.05, maxval=0.05, seed=None)`

Random uniform initializer.

Draws samples from a uniform distribution for given parameters.

**Examples**

Copied!

`>>> # Standalone usage: >>> initializer = RandomUniform(minval=0.0, maxval=1.0) >>> values = initializer(shape=(2, 2))`

Copied!

`>>> # Usage in a Keras layer: >>> initializer = RandomUniform(minval=0.0, maxval=1.0) >>> layer = Dense(3, kernel_initializer=initializer)`

**Arguments**

*   **minval**: A python scalar or a scalar keras tensor. Lower bound of the range of random values to generate (inclusive).
*   **maxval**: A python scalar or a scalar keras tensor. Upper bound of the range of random values to generate (exclusive).
*   **seed**: A Python integer or instance of `keras.backend.SeedGenerator`. Used to make the behavior of the initializer deterministic. Note that an initializer seeded with an integer or `None` (unseeded) will produce the same random values across multiple calls. To get different random values across multiple calls, use as seed an instance of `keras.backend.SeedGenerator`.

**Guides and examples using `RandomUniform`**

*   [Deep Deterministic Policy Gradient (DDPG)](https://keras.io/examples/rl/ddpg_pendulum/)
    

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/initializers/random_initializers.py#L86)

### `TruncatedNormal` class

Copied!

`keras.initializers.TruncatedNormal(mean=0.0, stddev=0.05, seed=None)`

Initializer that generates a truncated normal distribution.

The values generated are similar to values from a `RandomNormal` initializer, except that values more than two standard deviations from the mean are discarded and re-drawn.

**Examples**

Copied!

`>>> # Standalone usage: >>> initializer = TruncatedNormal(mean=0., stddev=1.) >>> values = initializer(shape=(2, 2))`

Copied!

`>>> # Usage in a Keras layer: >>> initializer = TruncatedNormal(mean=0., stddev=1.) >>> layer = Dense(3, kernel_initializer=initializer)`

**Arguments**

*   **mean**: A python scalar or a scalar keras tensor. Mean of the random values to generate.
*   **stddev**: A python scalar or a scalar keras tensor. Standard deviation of the random values to generate.
*   **seed**: A Python integer or instance of `keras.backend.SeedGenerator`. Used to make the behavior of the initializer deterministic. Note that an initializer seeded with an integer or `None` (unseeded) will produce the same random values across multiple calls. To get different random values across multiple calls, use as seed an instance of `keras.backend.SeedGenerator`.

**Guides and examples using `TruncatedNormal`**

*   [Image Classification using Global Context Vision Transformer](https://keras.io/examples/vision/image_classification_using_global_context_vision_transformer/)
    

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/initializers/constant_initializers.py#L49)

### `Zeros` class

Copied!

`keras.initializers.Zeros()`

Initializer that generates tensors initialized to 0.

**Examples**

Copied!

`>>> # Standalone usage: >>> initializer = Zeros() >>> values = initializer(shape=(2, 2))`

Copied!

`>>> # Usage in a Keras layer: >>> initializer = Zeros() >>> layer = Dense(units=3, kernel_initializer=initializer)`

**Guides and examples using `Zeros`**

*   [Image classification with Swin Transformers](https://keras.io/examples/vision/swin_transformers/)
    
*   [Image Segmentation using Composable Fully-Convolutional Networks](https://keras.io/examples/vision/fully_convolutional_network/)
    
*   [Distilling Vision Transformers](https://keras.io/examples/vision/deit/)
    

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/initializers/constant_initializers.py#L78)

### `Ones` class

Copied!

`keras.initializers.Ones()`

Initializer that generates tensors initialized to 1.

Also available via the shortcut function `ones`.

**Examples**

Copied!

`>>> # Standalone usage: >>> initializer = Ones() >>> values = initializer(shape=(2, 2))`

Copied!

`>>> # Usage in a Keras layer: >>> initializer = Ones() >>> layer = Dense(3, kernel_initializer=initializer)`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/initializers/random_initializers.py#L388)

### `GlorotNormal` class

Copied!

`keras.initializers.GlorotNormal(seed=None, input_axes=None, output_axes=None)`

The Glorot normal initializer, also called Xavier normal initializer.

Draws samples from a truncated normal distribution centered on 0 with `stddev = sqrt(2 / (fan_in + fan_out))` where `fan_in` is the number of input units in the weight tensor and `fan_out` is the number of output units in the weight tensor.

**Examples**

Copied!

`>>> # Standalone usage: >>> initializer = GlorotNormal() >>> values = initializer(shape=(2, 2))`

Copied!

`>>> # Usage in a Keras layer: >>> initializer = GlorotNormal() >>> layer = Dense(3, kernel_initializer=initializer)`

**Arguments**

*   **seed**: A Python integer or instance of `keras.backend.SeedGenerator`. Used to make the behavior of the initializer deterministic. Note that an initializer seeded with an integer or `None` (unseeded) will produce the same random values across multiple calls. To get different random values across multiple calls, use as seed an instance of `keras.backend.SeedGenerator`.

**Reference**

*   [Glorot et al., 2010](http://proceedings.mlr.press/v9/glorot10a.html)
    

**Guides and examples using `GlorotNormal`**

*   [GauGAN for conditional image generation](https://keras.io/examples/generative/gaugan/)
    
*   [Reproducibility in Keras Models](https://keras.io/examples/keras_recipes/reproducibility_recipes/)
    

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/initializers/random_initializers.py#L332)

### `GlorotUniform` class

Copied!

`keras.initializers.GlorotUniform(seed=None, input_axes=None, output_axes=None)`

The Glorot uniform initializer, also called Xavier uniform initializer.

Draws samples from a uniform distribution within `[-limit, limit]`, where `limit = sqrt(6 / (fan_in + fan_out))` (`fan_in` is the number of input units in the weight tensor and `fan_out` is the number of output units).

**Examples**

Copied!

`>>> # Standalone usage: >>> initializer = GlorotUniform() >>> values = initializer(shape=(2, 2))`

Copied!

`>>> # Usage in a Keras layer: >>> initializer = GlorotUniform() >>> layer = Dense(3, kernel_initializer=initializer)`

**Arguments**

*   **seed**: A Python integer or instance of `keras.backend.SeedGenerator`. Used to make the behavior of the initializer deterministic. Note that an initializer seeded with an integer or `None` (unseeded) will produce the same random values across multiple calls. To get different random values across multiple calls, use as seed an instance of `keras.backend.SeedGenerator`.

**Reference**

*   [Glorot et al., 2010](http://proceedings.mlr.press/v9/glorot10a.html)
    

**Guides and examples using `GlorotUniform`**

*   [Traffic forecasting using graph neural networks and LSTM](https://keras.io/examples/timeseries/timeseries_traffic_forecasting/)
    

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/initializers/random_initializers.py#L561)

### `HeNormal` class

Copied!

`keras.initializers.HeNormal(seed=None, input_axes=None, output_axes=None)`

He normal initializer.

It draws samples from a truncated normal distribution centered on 0 with `stddev = sqrt(2 / fan_in)` where `fan_in` is the number of input units in the weight tensor.

**Examples**

Copied!

`>>> # Standalone usage: >>> initializer = HeNormal() >>> values = initializer(shape=(2, 2))`

Copied!

`>>> # Usage in a Keras layer: >>> initializer = HeNormal() >>> layer = Dense(3, kernel_initializer=initializer)`

**Arguments**

*   **seed**: A Python integer or instance of `keras.backend.SeedGenerator`. Used to make the behavior of the initializer deterministic. Note that an initializer seeded with an integer or `None` (unseeded) will produce the same random values across multiple calls. To get different random values across multiple calls, use as seed an instance of `keras.backend.SeedGenerator`.

**Reference**

*   [He et al., 2015](https://arxiv.org/abs/1502.01852)
    

**Guides and examples using `HeNormal`**

*   [Multiclass semantic segmentation using DeepLabV3+](https://keras.io/examples/vision/deeplabv3_plus/)
    

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/initializers/random_initializers.py#L612)

### `HeUniform` class

Copied!

`keras.initializers.HeUniform(seed=None, input_axes=None, output_axes=None)`

He uniform variance scaling initializer.

Draws samples from a uniform distribution within `[-limit, limit]`, where `limit = sqrt(6 / fan_in)` (`fan_in` is the number of input units in the weight tensor).

**Examples**

Copied!

`>>> # Standalone usage: >>> initializer = HeUniform() >>> values = initializer(shape=(2, 2))`

Copied!

`>>> # Usage in a Keras layer: >>> initializer = HeUniform() >>> layer = Dense(3, kernel_initializer=initializer)`

**Arguments**

*   **seed**: A Python integer or instance of `keras.backend.SeedGenerator`. Used to make the behavior of the initializer deterministic. Note that an initializer seeded with an integer or `None` (unseeded) will produce the same random values across multiple calls. To get different random values across multiple calls, use as seed an instance of `keras.backend.SeedGenerator`.

**Reference**

*   [He et al., 2015](https://arxiv.org/abs/1502.01852)
    

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/initializers/random_initializers.py#L702)

### `Orthogonal` class

Copied!

`keras.initializers.Orthogonal(gain=1.0, seed=None)`

Initializer that generates an orthogonal matrix.

If the shape of the tensor to initialize is two-dimensional, it is initialized with an orthogonal matrix obtained from the QR decomposition of a matrix of random numbers drawn from a normal distribution. If the matrix has fewer rows than columns then the output will have orthogonal rows. Otherwise, the output will have orthogonal columns.

If the shape of the tensor to initialize is more than two-dimensional, a matrix of shape `(shape[0] * ... * shape[n - 2], shape[n - 1])` is initialized, where `n` is the length of the shape vector. The matrix is subsequently reshaped to give a tensor of the desired shape.

**Examples**

Copied!

`>>> # Standalone usage: >>> initializer = keras.initializers.Orthogonal() >>> values = initializer(shape=(2, 2))`

Copied!

`>>> # Usage in a Keras layer: >>> initializer = keras.initializers.Orthogonal() >>> layer = keras.layers.Dense(3, kernel_initializer=initializer)`

**Arguments**

*   **gain**: Multiplicative factor to apply to the orthogonal matrix.
*   **seed**: A Python integer. Used to make the behavior of the initializer deterministic.

**Reference**

*   [Saxe et al., 2014](https://openreview.net/forum?id=_wzZwKpTDF_9C)
    

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/initializers/constant_initializers.py#L9)

### `Constant` class

Copied!

`keras.initializers.Constant(value=0.0)`

Initializer that generates tensors with constant values.

Only scalar values are allowed. The constant value provided must be convertible to the dtype requested when calling the initializer.

**Examples**

Copied!

`>>> # Standalone usage: >>> initializer = Constant(10.) >>> values = initializer(shape=(2, 2))`

Copied!

`>>> # Usage in a Keras layer: >>> initializer = Constant(10.) >>> layer = Dense(3, kernel_initializer=initializer)`

**Arguments**

*   **value**: A Python scalar.

**Guides and examples using `Constant`**

*   [Image Classification using Global Context Vision Transformer](https://keras.io/examples/vision/image_classification_using_global_context_vision_transformer/)
    
*   [Image Segmentation using Composable Fully-Convolutional Networks](https://keras.io/examples/vision/fully_convolutional_network/)
    
*   [Point cloud segmentation with PointNet](https://keras.io/examples/vision/pointnet_segmentation/)
    
*   [Point cloud classification](https://keras.io/examples/vision/pointnet/)
    
*   [Class Attention Image Transformers with LayerScale](https://keras.io/examples/vision/cait/)
    
*   [A Transformer-based recommendation system](https://keras.io/examples/structured_data/movielens_recommendations_transformers/)
    
*   [Vector-Quantized Variational Autoencoders](https://keras.io/examples/generative/vq_vae/)
    

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/initializers/random_initializers.py#L201)

### `VarianceScaling` class

Copied!

`keras.initializers.VarianceScaling(     scale=1.0,     mode="fan_in",     distribution="truncated_normal",     seed=None,     input_axes=None,     output_axes=None, )`

Initializer that adapts its scale to the shape of its input tensors.

With `distribution="truncated_normal" or "untruncated_normal"`, samples are drawn from a truncated/untruncated normal distribution with a mean of zero and a standard deviation (after truncation, if used) `stddev = sqrt(scale / n)`, where `n` is:

*   number of input units in the weight tensor, if `mode="fan_in"`
*   number of output units, if `mode="fan_out"`
*   average of the numbers of input and output units, if `mode="fan_avg"`

With `distribution="uniform"`, samples are drawn from a uniform distribution within `[-limit, limit]`, where `limit = sqrt(3 * scale / n)`.

**Examples**

Copied!

`>>> # Standalone usage: >>> initializer = VarianceScaling(     scale=0.1, mode='fan_in', distribution='uniform') >>> values = initializer(shape=(2, 2))`

Copied!

`>>> # Usage in a Keras layer: >>> initializer = VarianceScaling(     scale=0.1, mode='fan_in', distribution='uniform') >>> layer = Dense(3, kernel_initializer=initializer)`

**Arguments**

*   **scale**: Scaling factor (positive float).
*   **mode**: One of `"fan_in"`, `"fan_out"`, `"fan_avg"`.
*   **distribution**: Random distribution to use. One of `"truncated_normal"`, `"untruncated_normal"`, or `"uniform"`.
*   **seed**: A Python integer or instance of `keras.backend.SeedGenerator`. Used to make the behavior of the initializer deterministic. Note that an initializer seeded with an integer or `None` (unseeded) will produce the same random values across multiple calls. To get different random values across multiple calls, use as seed an instance of `keras.backend.SeedGenerator`.
*   **input\_axes**: Optional list of integers. The axes of the input tensor that should be considered for computing the fan-in.
*   **output\_axes**: Optional list of integers. The axes of the output tensor that should be considered for computing the fan-out.

**Guides and examples using `VarianceScaling`**

*   [Parameter-efficient fine-tuning of GPT-2 with LoRA](https://keras.io/examples/nlp/parameter_efficient_finetuning_of_gpt2_with_lora/)
    

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/initializers/random_initializers.py#L445)

### `LecunNormal` class

Copied!

`keras.initializers.LecunNormal(seed=None, input_axes=None, output_axes=None)`

Lecun normal initializer.

Initializers allow you to pre-specify an initialization strategy, encoded in the Initializer object, without knowing the shape and dtype of the variable being initialized.

Draws samples from a truncated normal distribution centered on 0 with `stddev = sqrt(1 / fan_in)` where `fan_in` is the number of input units in the weight tensor.

**Examples**

Copied!

`>>> # Standalone usage: >>> initializer = LecunNormal() >>> values = initializer(shape=(2, 2))`

Copied!

`>>> # Usage in a Keras layer: >>> initializer = LecunNormal() >>> layer = Dense(3, kernel_initializer=initializer)`

**Arguments**

*   **seed**: A Python integer or instance of `keras.backend.SeedGenerator`. Used to make the behavior of the initializer deterministic. Note that an initializer seeded with an integer or `None` (unseeded) will produce the same random values across multiple calls. To get different random values across multiple calls, use as seed an instance of `keras.backend.SeedGenerator`.

**Reference**

*   [Klambauer et al., 2017](https://arxiv.org/abs/1706.02515)
    

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/initializers/random_initializers.py#L505)

### `LecunUniform` class

Copied!

`keras.initializers.LecunUniform(seed=None, input_axes=None, output_axes=None)`

Lecun uniform initializer.

Draws samples from a uniform distribution within `[-limit, limit]`, where `limit = sqrt(3 / fan_in)` (`fan_in` is the number of input units in the weight tensor).

**Examples**

Copied!

`>>> # Standalone usage: >>> initializer = LecunUniform() >>> values = initializer(shape=(2, 2))`

Copied!

`>>> # Usage in a Keras layer: >>> initializer = LecunUniform() >>> layer = Dense(3, kernel_initializer=initializer)`

**Arguments**

*   **seed**: A Python integer or instance of `keras.backend.SeedGenerator`. Used to make the behavior of the initializer deterministic. Note that an initializer seeded with an integer or `None` (unseeded) will produce the same random values across multiple calls. To get different random values across multiple calls, use as seed an instance of `keras.backend.SeedGenerator`.

**Reference**

*   [Klambauer et al., 2017](https://arxiv.org/abs/1706.02515)
    

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/initializers/constant_initializers.py#L109)

### `Identity` class

Copied!

`keras.initializers.IdentityInitializer(gain=1.0)`

Initializer that generates the identity matrix.

Only usable for generating 2D matrices.

**Examples**

Copied!

`>>> # Standalone usage: >>> initializer = Identity() >>> values = initializer(shape=(2, 2))`

Copied!

`>>> # Usage in a Keras layer: >>> initializer = Identity() >>> layer = Dense(3, kernel_initializer=initializer)`

**Arguments**

*   **gain**: Multiplicative factor to apply to the identity matrix.

* * *

Creating custom initializers
----------------------------

### Simple callables

You can pass a custom callable as initializer. It must take the arguments `shape` (shape of the variable to initialize) and `dtype` (dtype of generated values):

Copied!

`def my_init(shape, dtype=None):     return keras.random.normal(shape, dtype=dtype)  layer = Dense(64, kernel_initializer=my_init)`

### `Initializer` subclasses

If you need to configure your initializer via various arguments (e.g. `stddev` argument in `RandomNormal`), you should implement it as a subclass of `keras.initializers.Initializer`.

Initializers should implement a `__call__` method with the following signature:

Copied!

``def __call__(self, shape, dtype=None)`:     # returns a tensor of shape `shape` and dtype `dtype`     # containing values drawn from a distribution of your choice.``

Optionally, you an also implement the method `get_config` and the class method `from_config` in order to support serialization – just like with any Keras object.

Here's a simple example: a random normal initializer.

Copied!

``class ExampleRandomNormal(keras.initializers.Initializer):      def __init__(self, mean, stddev):       self.mean = mean       self.stddev = stddev      def __call__(self, shape, dtype=None)`:       return keras.random.normal(           shape, mean=self.mean, stddev=self.stddev, dtype=dtype)      def get_config(self):  # To support serialization       return {'mean': self.mean, 'stddev': self.stddev}``

Note that we don't have to implement `from_config` in the example above since the constructor arguments of the class the keys in the config returned by `get_config` are the same. In this case, the default `from_config` works fine.

[Layer weight initializers](https://keras.io/api/layers/initializers/#layer-weight-initializers)

[Usage of initializers](https://keras.io/api/layers/initializers/#usage-of-initializers)

[Available initializers](https://keras.io/api/layers/initializers/#available-initializers)

[`Initializer` class](https://keras.io/api/layers/initializers/#initializer-class)

[`RandomNormal` class](https://keras.io/api/layers/initializers/#randomnormal-class)

[`RandomUniform` class](https://keras.io/api/layers/initializers/#randomuniform-class)

[`TruncatedNormal` class](https://keras.io/api/layers/initializers/#truncatednormal-class)

[`Zeros` class](https://keras.io/api/layers/initializers/#zeros-class)

[`Ones` class](https://keras.io/api/layers/initializers/#ones-class)

[`GlorotNormal` class](https://keras.io/api/layers/initializers/#glorotnormal-class)

[`GlorotUniform` class](https://keras.io/api/layers/initializers/#glorotuniform-class)

[`HeNormal` class](https://keras.io/api/layers/initializers/#henormal-class)

[`HeUniform` class](https://keras.io/api/layers/initializers/#heuniform-class)

[`Orthogonal` class](https://keras.io/api/layers/initializers/#orthogonal-class)

[`Constant` class](https://keras.io/api/layers/initializers/#constant-class)

[`VarianceScaling` class](https://keras.io/api/layers/initializers/#variancescaling-class)

[`LecunNormal` class](https://keras.io/api/layers/initializers/#lecunnormal-class)

[`LecunUniform` class](https://keras.io/api/layers/initializers/#lecununiform-class)

[`Identity` class](https://keras.io/api/layers/initializers/#identity-class)

[Creating custom initializers](https://keras.io/api/layers/initializers/#creating-custom-initializers)

[Simple callables](https://keras.io/api/layers/initializers/#simple-callables)

[`Initializer` subclasses](https://keras.io/api/layers/initializers/#initializer-subclasses)