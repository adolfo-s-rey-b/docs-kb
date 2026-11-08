[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/random/fold_in#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/random/fold_in)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/random/fold_in?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/random/fold_in#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/random/fold_in#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.random.fold\_in Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/random/fold_in#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/random/fold_in#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/stateless_random_ops.py#L93-L132)

Folds in data to an RNG seed to form a new RNG seed.

#### View aliases

**Main aliases**

[`tf.random.experimental.stateless_fold_in`](https://www.tensorflow.org/api_docs/python/tf/random/fold_in)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.random.experimental.stateless_fold_in`](https://www.tensorflow.org/api_docs/python/tf/random/fold_in)
, [`tf.compat.v1.random.fold_in`](https://www.tensorflow.org/api_docs/python/tf/random/fold_in)

tf.random.fold_in(
        seed, data, alg='auto_select'
    )

For example, in a distributed-training setting, suppose we have a master seed and a replica ID. We want to fold the replica ID into the master seed to form a "replica seed" to be used by that replica later on, so that different replicas will generate different random numbers but the reproducibility of the whole system can still be controlled by the master seed:

    master_seed = [1, 2]

|     |     |
| --- | --- |
| Args<br>---- |     |
| `seed` | an RNG seed (a tensor with shape \[2\] and dtype `int32` or `int64`). (When using XLA, only `int32` is allowed.) |
| `data` | an `int32` or `int64` scalar representing data to be folded in to the seed. |
| `alg` | The RNG algorithm used to generate the random numbers. See [`tf.random.stateless_uniform`](https://www.tensorflow.org/api_docs/python/tf/random/stateless_uniform)<br> for a detailed explanation. |

|     |
| --- |
| Returns<br>------- |     |
| A new RNG seed that is a deterministic function of the inputs and is statistically safe for producing a stream of new pseudo-random values. It will have the same dtype as `data` (if `data` doesn't have an explicit dtype, the dtype will be determined by [`tf.convert_to_tensor`](https://www.tensorflow.org/api_docs/python/tf/convert_to_tensor)<br>). |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.