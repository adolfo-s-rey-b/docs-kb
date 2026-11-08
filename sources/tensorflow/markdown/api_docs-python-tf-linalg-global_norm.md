[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/linalg/global_norm#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/linalg/global_norm)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/linalg/global_norm?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/linalg/global_norm#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/linalg/global_norm#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/linalg/global_norm#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/linalg/global_norm#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.linalg.global\_norm Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/linalg/global_norm#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/linalg/global_norm#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/linalg/global_norm#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/linalg/global_norm#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/clip_ops.py#L245-L295)

Computes the global norm of multiple tensors.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.global_norm`](https://www.tensorflow.org/api_docs/python/tf/linalg/global_norm)
, [`tf.compat.v1.linalg.global_norm`](https://www.tensorflow.org/api_docs/python/tf/linalg/global_norm)

tf.linalg.global_norm(
        t_list, name=None
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Composing Learning Algorithms](https://www.tensorflow.org/federated/tutorials/composing_learning_algorithms) |

Given a tuple or list of tensors `t_list`, this operation returns the global norm of the elements in all tensors in `t_list`. The global norm is computed as:

`global_norm = sqrt(sum([l2norm(t)**2 for t in t_list]))`

Any entries in `t_list` that are of type None are ignored.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `t_list` | A tuple or list of mixed `Tensors`, `IndexedSlices`, or None. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A 0-D (scalar) `Tensor` of type `float`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | If `t_list` is not a sequence. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.