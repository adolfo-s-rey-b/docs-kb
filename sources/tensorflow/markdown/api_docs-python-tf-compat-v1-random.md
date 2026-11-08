[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/random#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/random)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/random?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Frandom&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Modules](https://www.tensorflow.org/api_docs/python/tf/compat/v1/random#modules)
    
*   [Classes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/random#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/compat/v1/random#functions)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

Module: tf.compat.v1.random Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================

*   On this page
*   [Modules](https://www.tensorflow.org/api_docs/python/tf/compat/v1/random#modules)
    
*   [Classes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/random#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/compat/v1/random#functions)
    

Public API for tf.\_api.v2.random namespace

Modules
-------

[`experimental`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/random/experimental)
 module: Public API for tf.\_api.v2.random.experimental namespace

Classes
-------

[`class Algorithm`](https://www.tensorflow.org/api_docs/python/tf/random/Algorithm)
: A random-number-generation (RNG) algorithm.

[`class Generator`](https://www.tensorflow.org/api_docs/python/tf/random/Generator)
: Random-number generator.

Functions
---------

[`all_candidate_sampler(...)`](https://www.tensorflow.org/api_docs/python/tf/random/all_candidate_sampler)
: Generate the set of all classes.

[`categorical(...)`](https://www.tensorflow.org/api_docs/python/tf/random/categorical)
: Draws samples from a categorical distribution.

[`create_rng_state(...)`](https://www.tensorflow.org/api_docs/python/tf/random/create_rng_state)
: Creates a RNG state from an integer or a vector.

[`fixed_unigram_candidate_sampler(...)`](https://www.tensorflow.org/api_docs/python/tf/random/fixed_unigram_candidate_sampler)
: Samples a set of classes using the provided (fixed) base distribution.

[`fold_in(...)`](https://www.tensorflow.org/api_docs/python/tf/random/fold_in)
: Folds in data to an RNG seed to form a new RNG seed.

[`gamma(...)`](https://www.tensorflow.org/api_docs/python/tf/random/gamma)
: Draws `shape` samples from each of the given Gamma distribution(s).

[`get_global_generator(...)`](https://www.tensorflow.org/api_docs/python/tf/random/get_global_generator)
: Retrieves the global generator.

[`get_seed(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_seed)
: Returns the local seeds an operation should use given an op-specific seed.

[`learned_unigram_candidate_sampler(...)`](https://www.tensorflow.org/api_docs/python/tf/random/learned_unigram_candidate_sampler)
: Samples a set of classes from a distribution learned during training.

[`log_uniform_candidate_sampler(...)`](https://www.tensorflow.org/api_docs/python/tf/random/log_uniform_candidate_sampler)
: Samples a set of classes using a log-uniform (Zipfian) base distribution.

[`multinomial(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/multinomial)
: Draws samples from a multinomial distribution. (deprecated)

[`normal(...)`](https://www.tensorflow.org/api_docs/python/tf/random/normal)
: Outputs random values from a normal distribution.

[`poisson(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/random_poisson)
: Draws `shape` samples from each of the given Poisson distribution(s).

[`set_global_generator(...)`](https://www.tensorflow.org/api_docs/python/tf/random/set_global_generator)
: Replaces the global generator with another `Generator` object.

[`set_random_seed(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/set_random_seed)
: Sets the graph-level random seed for the default graph.

[`shuffle(...)`](https://www.tensorflow.org/api_docs/python/tf/random/shuffle)
: Randomly shuffles a tensor along its first dimension.

[`split(...)`](https://www.tensorflow.org/api_docs/python/tf/random/split)
: Splits an RNG seed into `num` new seeds by adding a leading axis.

[`stateless_binomial(...)`](https://www.tensorflow.org/api_docs/python/tf/random/stateless_binomial)
: Outputs deterministic pseudorandom values from a binomial distribution.

[`stateless_categorical(...)`](https://www.tensorflow.org/api_docs/python/tf/random/stateless_categorical)
: Draws deterministic pseudorandom samples from a categorical distribution.

[`stateless_gamma(...)`](https://www.tensorflow.org/api_docs/python/tf/random/stateless_gamma)
: Outputs deterministic pseudorandom values from a gamma distribution.

[`stateless_multinomial(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/random/stateless_multinomial)
: Draws deterministic pseudorandom samples from a multinomial distribution. (deprecated)

[`stateless_normal(...)`](https://www.tensorflow.org/api_docs/python/tf/random/stateless_normal)
: Outputs deterministic pseudorandom values from a normal distribution.

[`stateless_parameterized_truncated_normal(...)`](https://www.tensorflow.org/api_docs/python/tf/random/stateless_parameterized_truncated_normal)
: Outputs random values from a truncated normal distribution.

[`stateless_poisson(...)`](https://www.tensorflow.org/api_docs/python/tf/random/stateless_poisson)
: Outputs deterministic pseudorandom values from a Poisson distribution.

[`stateless_truncated_normal(...)`](https://www.tensorflow.org/api_docs/python/tf/random/stateless_truncated_normal)
: Outputs deterministic pseudorandom values, truncated normally distributed.

[`stateless_uniform(...)`](https://www.tensorflow.org/api_docs/python/tf/random/stateless_uniform)
: Outputs deterministic pseudorandom values from a uniform distribution.

[`truncated_normal(...)`](https://www.tensorflow.org/api_docs/python/tf/random/truncated_normal)
: Outputs random values from a truncated normal distribution.

[`uniform(...)`](https://www.tensorflow.org/api_docs/python/tf/random/uniform)
: Outputs random values from a uniform distribution.

[`uniform_candidate_sampler(...)`](https://www.tensorflow.org/api_docs/python/tf/random/uniform_candidate_sampler)
: Samples a set of classes using a uniform base distribution.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.