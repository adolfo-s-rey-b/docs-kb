[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/random/uniform#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/random/uniform)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/random/uniform?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Frandom%2Funiform&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/random/uniform#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/random/uniform#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/random/uniform#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/random/uniform#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.random.uniform Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/random/uniform#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/random/uniform#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/random/uniform#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/random/uniform#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/random_ops.py#L211-L320)

Outputs random values from a uniform distribution.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.random.uniform`](https://www.tensorflow.org/api_docs/python/tf/random/uniform)
, [`tf.compat.v1.random_uniform`](https://www.tensorflow.org/api_docs/python/tf/random/uniform)

tf.random.uniform(
        shape,
        minval=0,
        maxval=None,
        dtype=tf.dtypes.float32,
        seed=None,
        name=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Validating correctness & numerical equivalence](https://www.tensorflow.org/guide/migrate/validate_correctness)<br>    <br>*   [tf.data: Build TensorFlow input pipelines](https://www.tensorflow.org/guide/data)<br>    <br>*   [Introduction to graphs and tf.function](https://www.tensorflow.org/guide/intro_to_graphs)<br>    <br>*   [Logistic regression for binary classification with Core APIs](https://www.tensorflow.org/guide/core/logistic_regression_core)<br>    <br>*   [Quickstart for the TensorFlow Core APIs](https://www.tensorflow.org/guide/core/quickstart_core) | *   [Customization basics: tensors and operations](https://www.tensorflow.org/tutorials/customization/basics)<br>    <br>*   [Parameter server training with ParameterServerStrategy](https://www.tensorflow.org/tutorials/distribute/parameter_server_training)<br>    <br>*   [Learned data compression](https://www.tensorflow.org/tutorials/generative/data_compression)<br>    <br>*   [DeepDream](https://www.tensorflow.org/tutorials/generative/deepdream)<br>    <br>*   [pix2pix: Image-to-image translation with a conditional GAN](https://www.tensorflow.org/tutorials/generative/pix2pix) |

The generated values follow a uniform distribution in the range `[minval, maxval)`. The lower bound `minval` is included in the range, while the upper bound `maxval` is excluded.\
\
For floats, the default range is `[0, 1)`. For ints, at least `maxval` must be specified explicitly.\
\
In the integer case, the random integers are slightly biased unless `maxval - minval` is an exact power of two. The bias is small for values of `maxval - minval` significantly smaller than the range of the output (either `2**32` or `2**64`).\
\
#### Examples:\
\
    tf.random.uniform(shape=[2])\
\
The `seed` argument produces a deterministic sequence of tensors across multiple calls. To repeat that sequence, use [`tf.random.set_seed`](https://www.tensorflow.org/api_docs/python/tf/random/set_seed)\
:\
\
    tf.random.set_seed(5)\
\
Without [`tf.random.set_seed`](https://www.tensorflow.org/api_docs/python/tf/random/set_seed)\
 but with a `seed` argument is specified, small changes to function graphs or previously executed operations will change the returned value. See [`tf.random.set_seed`](https://www.tensorflow.org/api_docs/python/tf/random/set_seed)\
 for details.\
\
|     |     |\
| --- | --- |\
| Args<br>---- |     |\
| `shape` | A 1-D integer Tensor or Python array. The shape of the output tensor. |\
| `minval` | A Tensor or Python value of type `dtype`, broadcastable with `shape` (for integer types, broadcasting is not supported, so it needs to be a scalar). The lower bound on the range of random values to generate (inclusive). Defaults to 0. |\
| `maxval` | A Tensor or Python value of type `dtype`, broadcastable with `shape` (for integer types, broadcasting is not supported, so it needs to be a scalar). The upper bound on the range of random values to generate (exclusive). Defaults to 1 if `dtype` is floating point. |\
| `dtype` | The type of the output: `float16`, `bfloat16`, `float32`, `float64`, `int32`, or `int64`. Defaults to `float32`. |\
| `seed` | A Python integer. Used in combination with [`tf.random.set_seed`](https://www.tensorflow.org/api_docs/python/tf/random/set_seed)<br> to create a reproducible sequence of tensors across multiple calls. |\
| `name` | A name for the operation (optional). |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| A tensor of the specified shape filled with random uniform values. |     |\
\
|     |     |\
| --- | --- |\
| Raises<br>------ |     |\
| `ValueError` | If `dtype` is integral and `maxval` is not specified. |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.