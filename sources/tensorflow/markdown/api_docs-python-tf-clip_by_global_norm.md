[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/clip_by_global_norm#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/clip_by_global_norm)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/clip_by_global_norm?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/clip_by_global_norm#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/clip_by_global_norm#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/clip_by_global_norm#raises)
    
*   [References](https://www.tensorflow.org/api_docs/python/tf/clip_by_global_norm#references)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.clip\_by\_global\_norm Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/clip_by_global_norm#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/clip_by_global_norm#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/clip_by_global_norm#raises)
    
*   [References](https://www.tensorflow.org/api_docs/python/tf/clip_by_global_norm#references)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/clip_ops.py#L298-L392)

Clips values of multiple tensors by the ratio of the sum of their norms.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.clip_by_global_norm`](https://www.tensorflow.org/api_docs/python/tf/clip_by_global_norm)

tf.clip_by_global_norm(
        t_list, clip_norm, use_norm=None, name=None
    )

Given a tuple or list of tensors `t_list`, and a clipping ratio `clip_norm`, this operation returns a list of clipped tensors `list_clipped` and the global norm (`global_norm`) of all tensors in `t_list`. Optionally, if you've already computed the global norm for `t_list`, you can specify the global norm with `use_norm`.

To perform the clipping, the values `t_list[i]` are set to:

t_list[i] * clip_norm / max(global_norm, clip_norm)

where:

global_norm = sqrt(sum([l2norm(t)**2 for t in t_list]))

If `clip_norm > global_norm` then the entries in `t_list` remain as they are, otherwise they're all shrunk by the global ratio.

If `global_norm == infinity` then the entries in `t_list` are all set to `NaN` to signal that an error occurred.

Any of the entries of `t_list` that are of type `None` are ignored.

This is the correct way to perform gradient clipping (Pascanu et al., 2012).

However, it is slower than `clip_by_norm()` because all the parameters must be ready before the clipping operation can be performed.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `t_list` | A tuple or list of mixed `Tensors`, `IndexedSlices`, or None. |
| `clip_norm` | A 0-D (scalar) `Tensor` > 0. The clipping ratio. |
| `use_norm` | A 0-D (scalar) `Tensor` of type `float` (optional). The global norm to use. If not provided, `global_norm()` is used to compute the norm. |
| `name` | A name for the operation (optional). |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `list_clipped` | A list of `Tensors` of the same type as `list_t`. |
| `global_norm` | A 0-D (scalar) `Tensor` representing the global norm. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | If `t_list` is not a sequence. |

|     |
| --- |
| References<br>---------- |     |
| On the difficulty of training Recurrent Neural Networks: [Pascanu et al., 2012](http://proceedings.mlr.press/v28/pascanu13.html)<br> ([pdf](http://proceedings.mlr.press/v28/pascanu13.pdf)<br>) |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.