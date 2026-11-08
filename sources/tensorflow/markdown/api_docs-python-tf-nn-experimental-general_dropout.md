[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/nn/experimental/general_dropout#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/nn/experimental/general_dropout)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/nn/experimental/general_dropout?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/experimental/general_dropout#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/experimental/general_dropout#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/nn/experimental/general_dropout#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.nn.experimental.general\_dropout Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/experimental/general_dropout#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/experimental/general_dropout#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/nn/experimental/general_dropout#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/nn_ops.py#L5669-L5737)

Computes dropout: randomly sets elements to zero to prevent overfitting.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.nn.experimental.general_dropout`](https://www.tensorflow.org/api_docs/python/tf/nn/experimental/general_dropout)

tf.nn.experimental.general_dropout(
        x, rate, uniform_sampler, noise_shape=None, name=None
    )

Please see [`tf.nn.experimental.stateless_dropout`](https://www.tensorflow.org/api_docs/python/tf/nn/experimental/stateless_dropout)
 for an overview of dropout.

Unlike [`tf.nn.experimental.stateless_dropout`](https://www.tensorflow.org/api_docs/python/tf/nn/experimental/stateless_dropout)
, here you can supply a custom sampler function `uniform_sampler` that (given a shape and a dtype) generates a random, `Uniform[0, 1)`\-distributed tensor (of that shape and dtype). `uniform_sampler` can be e.g. `tf.random.stateless_random_uniform` or [`tf.random.Generator.uniform`](https://www.tensorflow.org/api_docs/python/tf/random/Generator#uniform)\
.\
\
For example, if you are using [`tf.random.Generator`](https://www.tensorflow.org/api_docs/python/tf/random/Generator)\
 to generate random numbers, you can use this code to do dropouts:\
\
    g = tf.random.Generator.from_seed(7)\
\
It has better performance than using [`tf.nn.experimental.stateless_dropout`](https://www.tensorflow.org/api_docs/python/tf/nn/experimental/stateless_dropout)\
 and [`tf.random.Generator.make_seeds`](https://www.tensorflow.org/api_docs/python/tf/random/Generator#make_seeds)\
:\
\
    g = tf.random.Generator.from_seed(7)\
\
because generating and consuming seeds cost extra computation. [`tf.nn.experimental.general_dropout`](https://www.tensorflow.org/api_docs/python/tf/nn/experimental/general_dropout)\
 can let you avoid them.\
\
|     |     |\
| --- | --- |\
| Args<br>---- |     |\
| `x` | A floating point tensor. |\
| `rate` | A scalar `Tensor` with the same type as x. The probability that each element is dropped. For example, setting rate=0.1 would drop 10% of input elements. |\
| `uniform_sampler` | a callable of signature `(shape, dtype) -> Tensor[shape, dtype]`, used to generate a tensor of uniformly-distributed random numbers in the range `[0, 1)`, of the given shape and dtype. |\
| `noise_shape` | A 1-D integer `Tensor`, representing the shape for randomly generated keep/drop flags. |\
| `name` | A name for this operation. |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| A Tensor of the same shape and dtype of `x`. |     |\
\
|     |     |\
| --- | --- |\
| Raises<br>------ |     |\
| `ValueError` | If `rate` is not in `[0, 1)` or if `x` is not a floating point tensor. `rate=1` is disallowed, because the output would be all zeros, which is likely not what was intended. |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.