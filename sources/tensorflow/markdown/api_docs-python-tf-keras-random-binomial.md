[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/random/binomial#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/random/binomial)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/random/binomial?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/random/binomial#args)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.random.binomial Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/random/binomial#args)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/random/random.py#L271-L309)

Draw samples from a Binomial distribution.

tf.keras.random.binomial(
        shape, counts, probabilities, dtype=None, seed=None
    )

The values are drawn from a Binomial distribution with specified trial count and probability of success.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `shape` | The shape of the random values to generate. |
| `counts` | A number or array of numbers representing the number of trials. It must be broadcastable with `probabilities`. |
| `probabilities` | A float or array of floats representing the probability of success of an individual event. It must be broadcastable with `counts`. |
| `dtype` | Optional dtype of the tensor. Only floating point types are supported. If not specified, [`keras.config.floatx()`](https://www.tensorflow.org/api_docs/python/tf/keras/backend/floatx)<br> is used, which defaults to `float32` unless you configured it otherwise (via [`keras.config.set_floatx(float_dtype)`](https://www.tensorflow.org/api_docs/python/tf/keras/backend/set_floatx)<br>). |
| `seed` | Optional Python integer or instance of [`keras.random.SeedGenerator`](https://www.tensorflow.org/api_docs/python/tf/keras/random/SeedGenerator)<br>. By default, the `seed` argument is `None`, and an internal global [`keras.random.SeedGenerator`](https://www.tensorflow.org/api_docs/python/tf/keras/random/SeedGenerator)<br> is used. The `seed` argument can be used to ensure deterministic (repeatable) random number generation. Note that passing an integer as the `seed` value will produce the same random values for each call. To generate different random values for repeated calls, an instance of [`keras.random.SeedGenerator`](https://www.tensorflow.org/api_docs/python/tf/keras/random/SeedGenerator)<br> must be provided as the `seed` value. Remark concerning the JAX backend: When tracing functions with the JAX backend the global [`keras.random.SeedGenerator`](https://www.tensorflow.org/api_docs/python/tf/keras/random/SeedGenerator)<br> is not supported. Therefore, during tracing the default value seed=None will produce an error, and a `seed` argument must be provided. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.