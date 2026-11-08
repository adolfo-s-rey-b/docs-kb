[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tuple#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tuple)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tuple?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Ftuple&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tuple#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tuple#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tuple#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.tuple Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tuple#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tuple#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/tuple#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/control_flow_ops.py#L2106-L2177)

Group tensors together.

tf.compat.v1.tuple(
        tensors, name=None, control_inputs=None
    )

This creates a tuple of tensors with the same values as the `tensors` argument, except that the value of each tensor is only returned after the values of all tensors have been computed.

`control_inputs` contains additional ops that have to finish before this op finishes, but whose outputs are not returned.

This can be used as a "join" mechanism for parallel computations: all the argument tensors can be computed in parallel, but the values of any tensor returned by `tuple` are only available after all the parallel computations are done.

See also [`tf.group`](https://www.tensorflow.org/api_docs/python/tf/group)
 and [`tf.control_dependencies`](https://www.tensorflow.org/api_docs/python/tf/control_dependencies)
.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `tensors` | A list of `Tensor`s or `IndexedSlices`, some entries can be `None`. |
| `name` | (optional) A name to use as a `name_scope` for the operation. |
| `control_inputs` | List of additional ops to finish before returning. |

|     |
| --- |
| Returns<br>------- |     |
| Same as `tensors`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If `tensors` does not contain any `Tensor` or `IndexedSlices`. |
| `TypeError` | If `control_inputs` is not a list of `Operation` or `Tensor` objects. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.