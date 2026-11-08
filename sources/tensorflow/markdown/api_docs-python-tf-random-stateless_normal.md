[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/random/stateless_normal?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/random/stateless_normal)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/random/stateless_normal?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/random/stateless_normal?version=stable#used-in-the-notebooks_1)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/random/stateless_normal?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/random/stateless_normal?version=stable#returns_1)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.random.stateless\_normal Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/random/stateless_normal?version=stable#used-in-the-notebooks_1)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/random/stateless_normal?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/random/stateless_normal?version=stable#returns_1)
    

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/stateless_random_ops.py#L644-L692)

Outputs deterministic pseudorandom values from a normal distribution.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.random.stateless_normal`](https://www.tensorflow.org/api_docs/python/tf/random/stateless_normal)

tf.random.stateless_normal(
        shape,
        seed,
        mean=0.0,
        stddev=1.0,
        dtype=tf.dtypes.float32,
        name=None,
        alg='auto_select'
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Random number generation](https://www.tensorflow.org/guide/random_numbers) | *   [Random noise generation in TFF](https://www.tensorflow.org/federated/tutorials/random_noise_generation)<br>    <br>*   [Multiple changepoint detection and Bayesian model selection](https://www.tensorflow.org/probability/examples/Multiple_changepoint_detection_and_Bayesian_model_selection)<br>    <br>*   [TFP Release Notes notebook (0.11.0)](https://www.tensorflow.org/probability/examples/TFP_Release_Notebook_0_11_0)<br>    <br>*   [Substantial Undocumented Infection Facilitates the Rapid Dissemination of Novel Coronavirus (SARS-CoV2)](https://www.tensorflow.org/probability/examples/Undocumented_Infection_and_the_Dissemination_of_SARS-CoV2) |

This is a stateless version of [`tf.random.normal`](https://www.tensorflow.org/api_docs/python/tf/random/normal)
: if run twice with the same seeds and shapes, it will produce the same pseudorandom numbers. The output is consistent across multiple runs on the same hardware (and between CPU and GPU), but may change between versions of TensorFlow or on non-CPU/GPU hardware.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `shape` | A 1-D integer Tensor or Python array. The shape of the output tensor. |
| `seed` | A shape \[2\] Tensor, the seed to the random number generator. Must have dtype `int32` or `int64`. (When using XLA, only `int32` is allowed.) |
| `mean` | A 0-D Tensor or Python value of type `dtype`. The mean of the normal distribution. |
| `stddev` | A 0-D Tensor or Python value of type `dtype`. The standard deviation of the normal distribution. |
| `dtype` | The float type of the output: `float16`, `bfloat16`, `float32`, `float64`. Defaults to `float32`. |
| `name` | A name for the operation (optional). |
| `alg` | The RNG algorithm used to generate the random numbers. See [`tf.random.stateless_uniform`](https://www.tensorflow.org/api_docs/python/tf/random/stateless_uniform)<br> for a detailed explanation. |

|     |
| --- |
| Returns<br>------- |     |
| A tensor of the specified shape filled with random normal values. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.