[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/random/SeedGenerator#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/random/SeedGenerator)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/random/SeedGenerator?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/random/SeedGenerator#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/random/SeedGenerator#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/random/SeedGenerator#get_config)
        
    *   [next](https://www.tensorflow.org/api_docs/python/tf/keras/random/SeedGenerator#next)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.random.SeedGenerator Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================================

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/random/SeedGenerator#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/random/SeedGenerator#from_config)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/random/SeedGenerator#get_config)
        
    *   [next](https://www.tensorflow.org/api_docs/python/tf/keras/random/SeedGenerator#next)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/random/seed_generator.py#L14-L118)

Generates variable seeds upon each call to a function generating random numbers.

tf.keras.random.SeedGenerator(
        seed=None, name=None, **kwargs
    )

In Keras, all random number generators (such as [`keras.random.normal()`](https://www.tensorflow.org/api_docs/python/tf/keras/random/normal)
) are stateless, meaning that if you pass an integer seed to them (such as `seed=42`), they will return the same values for repeated calls. To get different values for each call, a `SeedGenerator` providing the state of the random generator has to be used.

Note that all the random number generators have a default seed of None, which implies that an internal global SeedGenerator is used. If you need to decouple the RNG from the global state you can provide a local `StateGenerator` with either a deterministic or random initial state.

Remark concerning the JAX backend: Note that the use of a local `StateGenerator` as seed argument is required for JIT compilation of RNG with the JAX backend, because the use of global state is not supported.

#### Example:

seed_gen = keras.random.SeedGenerator(seed=42)
    values = keras.random.normal(shape=(2, 3), seed=seed_gen)
    new_values = keras.random.normal(shape=(2, 3), seed=seed_gen)

#### Usage in a layer:

class Dropout(keras.Layer):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.seed_generator = keras.random.SeedGenerator(1337)
    
        def call(self, x, training=False):
            if training:
                return keras.random.dropout(
                    x, rate=0.5, seed=self.seed_generator
                )
            return x

Methods
-------

### `from_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/random/seed_generator.py#L116-L118)

@classmethod

### `get_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/random/seed_generator.py#L113-L114)

get_config()

### `next`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/random/seed_generator.py#L98-L111)

next(
        ordered=True
    )

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.