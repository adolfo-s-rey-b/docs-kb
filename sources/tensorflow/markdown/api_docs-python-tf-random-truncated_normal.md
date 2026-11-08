[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/random/truncated_normal#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/random/truncated_normal)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/random/truncated_normal?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Frandom%2Ftruncated_normal&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/random/truncated_normal#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/random/truncated_normal#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/random/truncated_normal#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.random.truncated\_normal Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/random/truncated_normal#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/random/truncated_normal#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/random/truncated_normal#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/random_ops.py#L155-L204)

Outputs random values from a truncated normal distribution.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.random.truncated_normal`](https://www.tensorflow.org/api_docs/python/tf/random/truncated_normal)
, [`tf.compat.v1.truncated_normal`](https://www.tensorflow.org/api_docs/python/tf/random/truncated_normal)

tf.random.truncated_normal(
        shape,
        mean=0.0,
        stddev=1.0,
        dtype=tf.dtypes.float32,
        seed=None,
        name=None
    )

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Ragged tensors](https://www.tensorflow.org/guide/ragged_tensor) |

The values are drawn from a normal distribution with specified mean and standard deviation, discarding and re-drawing any samples that are more than two standard deviations from the mean.

#### Examples:

    tf.random.truncated_normal(shape=[2])

    tf.random.truncated_normal(shape=[2], mean=3, stddev=1, dtype=tf.float32)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `shape` | A 1-D integer Tensor or Python array. The shape of the output tensor. |
| `mean` | A 0-D Tensor or Python value of type `dtype`. The mean of the truncated normal distribution. |
| `stddev` | A 0-D Tensor or Python value of type `dtype`. The standard deviation of the normal distribution, before truncation. |
| `dtype` | The type of the output. Restricted to floating-point types: [`tf.half`](https://www.tensorflow.org/api_docs/python/tf#half)<br>, `tf.float`, [`tf.double`](https://www.tensorflow.org/api_docs/python/tf#double)<br>, etc. |
| `seed` | A Python integer. Used to create a random seed for the distribution. See [`tf.random.set_seed`](https://www.tensorflow.org/api_docs/python/tf/random/set_seed)<br> for more information. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A tensor of the specified shape filled with random truncated normal values. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.