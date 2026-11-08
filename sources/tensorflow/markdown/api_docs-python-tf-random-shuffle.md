[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/random/shuffle#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/random/shuffle)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/random/shuffle?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/random/shuffle#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/random/shuffle#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/random/shuffle#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.random.shuffle Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/random/shuffle#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/random/shuffle#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/random/shuffle#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/random_ops.py#L326-L356)

Randomly shuffles a tensor along its first dimension.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.random.shuffle`](https://www.tensorflow.org/api_docs/python/tf/random/shuffle)
, [`tf.compat.v1.random_shuffle`](https://www.tensorflow.org/api_docs/python/tf/random/shuffle)

tf.random.shuffle(
        value, seed=None, name=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Quickstart for the TensorFlow Core APIs](https://www.tensorflow.org/guide/core/quickstart_core) | *   [Generalized Linear Models](https://www.tensorflow.org/probability/examples/Generalized_Linear_Models) |

The tensor is shuffled along dimension 0, such that each `value[j]` is mapped to one and only one `output[i]`. For example, a mapping that might occur for a 3x2 tensor is:

[[1, 2],       [[5, 6],\
     [3, 4],  ==>   [1, 2],\
     [5, 6]]        [3, 4]]

|     |     |
| --- | --- |
| Args<br>---- |     |
| `value` | A Tensor to be shuffled. |
| `seed` | A Python integer. Used to create a random seed for the distribution. See [`tf.random.set_seed`](https://www.tensorflow.org/api_docs/python/tf/random/set_seed)<br> for behavior. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A tensor of same shape and type as `value`, shuffled along its first dimension. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.