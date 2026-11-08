[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/random/stateless_uniform?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/random/stateless_uniform)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/random/stateless_uniform?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/random/stateless_uniform?version=stable#used-in-the-notebooks_1)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/random/stateless_uniform?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/random/stateless_uniform?version=stable#returns_1)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/random/stateless_uniform?version=stable#raises_1)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.random.stateless\_uniform Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/random/stateless_uniform?version=stable#used-in-the-notebooks_1)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/random/stateless_uniform?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/random/stateless_uniform?version=stable#returns_1)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/random/stateless_uniform?version=stable#raises_1)
    

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/stateless_random_ops.py#L274-L408)

Outputs deterministic pseudorandom values from a uniform distribution.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.random.stateless_uniform`](https://www.tensorflow.org/api_docs/python/tf/random/stateless_uniform)

tf.random.stateless_uniform(
        shape,
        seed,
        minval=0,
        maxval=None,
        dtype=tf.dtypes.float32,
        name=None,
        alg='auto_select'
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Substantial Undocumented Infection Facilitates the Rapid Dissemination of Novel Coronavirus (SARS-CoV2)](https://www.tensorflow.org/probability/examples/Undocumented_Infection_and_the_Dissemination_of_SARS-CoV2)<br>    <br>*   [TFP Release Notes notebook (0.11.0)](https://www.tensorflow.org/probability/examples/TFP_Release_Notebook_0_11_0) |

This is a stateless version of [`tf.random.uniform`](https://www.tensorflow.org/api_docs/python/tf/random/uniform)
: if run twice with the same seeds and shapes, it will produce the same pseudorandom numbers. The output is consistent across multiple runs on the same hardware (and between CPU and GPU), but may change between versions of TensorFlow or on non-CPU/GPU hardware.

The generated values follow a uniform distribution in the range `[minval, maxval)`. The lower bound `minval` is included in the range, while the upper bound `maxval` is excluded.\
\
For floats, the default range is `[0, 1)`. For ints, at least `maxval` must be specified explicitly.\
\
In the integer case, the random integers are slightly biased unless `maxval - minval` is an exact power of two. The bias is small for values of `maxval - minval` significantly smaller than the range of the output (either `2**32` or `2**64`).\
\
For full-range (i.e. inclusive of both max and min) random integers, pass `minval=None` and `maxval=None` with an integer `dtype`. For an integer dtype either both `minval` and `maxval` must be `None` or neither may be `None`. For example:\
\
ints = tf.random.stateless_uniform(\
        [10], seed=(2, 3), minval=None, maxval=None, dtype=tf.int32)\
\
|     |     |\
| --- | --- |\
| Args<br>---- |     |\
| `shape` | A 1-D integer Tensor or Python array. The shape of the output tensor. |\
| `seed` | A shape \[2\] Tensor, the seed to the random number generator. Must have dtype `int32` or `int64`. (When using XLA, only `int32` is allowed.) |\
| `minval` | A Tensor or Python value of type `dtype`, broadcastable with `shape` (for integer types, broadcasting is not supported, so it needs to be a scalar). The lower bound on the range of random values to generate. Pass `None` for full-range integers. Defaults to 0. |\
| `maxval` | A Tensor or Python value of type `dtype`, broadcastable with `shape` (for integer types, broadcasting is not supported, so it needs to be a scalar). The upper bound on the range of random values to generate. Defaults to 1 if `dtype` is floating point. Pass `None` for full-range integers. |\
| `dtype` | The type of the output: `float16`, `bfloat16`, `float32`, `float64`, `int32`, or `int64`. For unbounded uniform ints (`minval`, `maxval` both `None`), `uint32` and `uint64` may be used. Defaults to `float32`. |\
| `name` | A name for the operation (optional). |\
| `alg` | The RNG algorithm used to generate the random numbers. Valid choices are `"philox"` for [the Philox algorithm](https://www.thesalmons.org/john/random123/papers/random123sc11.pdf)<br>, `"threefry"` for [the ThreeFry algorithm](https://www.thesalmons.org/john/random123/papers/random123sc11.pdf)<br>, and `"auto_select"` (default) for the system to automatically select an algorithm based the device type. Values of [`tf.random.Algorithm`](https://www.tensorflow.org/api_docs/python/tf/random/Algorithm)<br> can also be used. Note that with `"auto_select"`, the outputs of this function may change when it is running on a different device. |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| A tensor of the specified shape filled with random uniform values. |     |\
\
|     |     |\
| --- | --- |\
| Raises<br>------ |     |\
| `ValueError` | If `dtype` is integral and only one of `minval` or `maxval` is specified. |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.