[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/multinomial#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/multinomial)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/multinomial?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/multinomial#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/multinomial#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.multinomial Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/multinomial#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/multinomial#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/random_ops.py#L362-L391)

Draws samples from a multinomial distribution. (deprecated)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.random.multinomial`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/multinomial)

tf.compat.v1.multinomial(
        logits, num_samples, seed=None, name=None, output_dtype=None
    )

#### Example:

# samples has shape [1, 5], where each value is either 0 or 1 with equal
    # probability.
    samples = tf.random.categorical(tf.math.log([[0.5, 0.5]]), 5)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `logits` | 2-D Tensor with shape `[batch_size, num_classes]`. Each slice `[i, :]` represents the unnormalized log-probabilities for all classes. |
| `num_samples` | 0-D. Number of independent samples to draw for each row slice. |
| `seed` | A Python integer. Used to create a random seed for the distribution. See [`tf.random.set_seed`](https://www.tensorflow.org/api_docs/python/tf/random/set_seed)<br> for behavior. |
| `name` | Optional name for the operation. |
| `output_dtype` | The integer type of the output: `int32` or `int64`. Defaults to `int64`. |

|     |
| --- |
| Returns<br>------- |     |
| The drawn samples of shape `[batch_size, num_samples]`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.