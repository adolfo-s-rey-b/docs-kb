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
 / SeedGenerator class

SeedGenerator class
===================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/random/seed_generator.py#L14)

### `SeedGenerator` class

Copied!

`keras.random.SeedGenerator(seed=None, name=None, **kwargs)`

Generates variable seeds upon each call to a function generating random numbers.

In Keras, all random number generators (such as `keras.random.normal()`) are stateless, meaning that if you pass an integer seed to them (such as `seed=42`), they will return the same values for repeated calls. To get different values for each call, a `SeedGenerator` providing the state of the random generator has to be used.

Note that all the random number generators have a default seed of None, which implies that an internal global SeedGenerator is used. If you need to decouple the RNG from the global state you can provide a local `StateGenerator` with either a deterministic or random initial state.

Remark concerning the JAX backend: Note that the use of a local `StateGenerator` as seed argument is required for JIT compilation of RNG with the JAX backend, because the use of global state is not supported.

**Example**

Copied!

`seed_gen = keras.random.SeedGenerator(seed=42) values = keras.random.normal(shape=(2, 3), seed=seed_gen) new_values = keras.random.normal(shape=(2, 3), seed=seed_gen)`

Usage in a layer:

Copied!

`class Dropout(keras.Layer):     def __init__(self, **kwargs):         super().__init__(**kwargs)         self.seed_generator = keras.random.SeedGenerator(1337)      def call(self, x, training=False):         if training:             return keras.random.dropout(                 x, rate=0.5, seed=self.seed_generator             )         return x`

* * *

[SeedGenerator class](https://keras.io/api/random/seed_generator/#seedgenerator-class)

[`SeedGenerator` class](https://keras.io/api/random/seed_generator/#seedgenerator-class)