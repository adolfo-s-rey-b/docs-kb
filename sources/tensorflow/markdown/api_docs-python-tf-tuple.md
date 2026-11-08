[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/tuple#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/tuple)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/tuple?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Ftuple&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/tuple#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/tuple#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/tuple#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.tuple Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/tuple#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/tuple#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/tuple#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/control_flow_ops.py#L2037-L2103)

Groups tensors together.

tf.tuple(
        tensors, control_inputs=None, name=None
    )

The returned tensors have the same value as the input tensors, but they are computed only after all the input tensors have been computed.

See also [`tf.group`](https://www.tensorflow.org/api_docs/python/tf/group)
 and [`tf.control_dependencies`](https://www.tensorflow.org/api_docs/python/tf/control_dependencies)
.

#### Example:

    with tf.Graph().as_default():

    with tf.Graph().as_default():

|     |     |
| --- | --- |
| Args<br>---- |     |
| `tensors` | A list of `Tensor`s or `IndexedSlices`, some entries can be `None`. |
| `control_inputs` | List of additional ops to finish before returning. |
| `name` | (optional) A name to use as a `name_scope` for the operation. |

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