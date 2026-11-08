[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/random/experimental#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/random/experimental)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/random/experimental?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/random/experimental#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/compat/v1/random/experimental#functions)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

Module: tf.compat.v1.random.experimental Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================================

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/random/experimental#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/compat/v1/random/experimental#functions)
    

Public API for tf.\_api.v2.random.experimental namespace

Classes
-------

[`class Algorithm`](https://www.tensorflow.org/api_docs/python/tf/random/Algorithm)
: A random-number-generation (RNG) algorithm.

[`class Generator`](https://www.tensorflow.org/api_docs/python/tf/random/Generator)
: Random-number generator.

Functions
---------

[`create_rng_state(...)`](https://www.tensorflow.org/api_docs/python/tf/random/create_rng_state)
: Creates a RNG state from an integer or a vector.

[`get_global_generator(...)`](https://www.tensorflow.org/api_docs/python/tf/random/get_global_generator)
: Retrieves the global generator.

[`index_shuffle(...)`](https://www.tensorflow.org/api_docs/python/tf/random/experimental/index_shuffle)
: Outputs the position of `index` in a permutation of `[0, ..., max_index]`.

[`set_global_generator(...)`](https://www.tensorflow.org/api_docs/python/tf/random/set_global_generator)
: Replaces the global generator with another `Generator` object.

[`stateless_fold_in(...)`](https://www.tensorflow.org/api_docs/python/tf/random/fold_in)
: Folds in data to an RNG seed to form a new RNG seed.

[`stateless_shuffle(...)`](https://www.tensorflow.org/api_docs/python/tf/random/experimental/stateless_shuffle)
: Randomly and deterministically shuffles a tensor along its first dimension.

[`stateless_split(...)`](https://www.tensorflow.org/api_docs/python/tf/random/split)
: Splits an RNG seed into `num` new seeds by adding a leading axis.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.