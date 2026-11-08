[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/random/split#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/random/split)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/random/split?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Frandom%2Fsplit&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/random/split#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/random/split#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/random/split#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.random.split Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/random/split#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/random/split#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/random/split#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/stateless_random_ops.py#L51-L90)

Splits an RNG seed into `num` new seeds by adding a leading axis.

#### View aliases

**Main aliases**

[`tf.random.experimental.stateless_split`](https://www.tensorflow.org/api_docs/python/tf/random/split)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.random.experimental.stateless_split`](https://www.tensorflow.org/api_docs/python/tf/random/split)
, [`tf.compat.v1.random.split`](https://www.tensorflow.org/api_docs/python/tf/random/split)

tf.random.split(
        seed, num=2, alg='auto_select'
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Data augmentation](https://www.tensorflow.org/tutorials/images/data_augmentation) |

#### Example:

    seed = [1, 2]

|     |     |
| --- | --- |
| Args<br>---- |     |
| `seed` | an RNG seed (a tensor with shape \[2\] and dtype `int32` or `int64`). (When using XLA, only `int32` is allowed.) |
| `num` | optional, a positive integer or scalar tensor indicating the number of seeds to produce (default 2). |
| `alg` | The RNG algorithm used to generate the random numbers. See [`tf.random.stateless_uniform`](https://www.tensorflow.org/api_docs/python/tf/random/stateless_uniform)<br> for a detailed explanation. |

|     |
| --- |
| Returns<br>------- |     |
| A tensor with shape \[num, 2\] representing `num` new seeds. It will have the same dtype as `seed` (if `seed` doesn't have an explicit dtype, the dtype will be determined by [`tf.convert_to_tensor`](https://www.tensorflow.org/api_docs/python/tf/convert_to_tensor)<br>). |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.