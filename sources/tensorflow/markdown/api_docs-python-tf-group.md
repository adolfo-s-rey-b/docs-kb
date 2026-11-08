[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/group#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/group)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/group?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/group#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/group#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/group#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/group#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.group Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/group#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/group#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/group#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/group#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/control_flow_ops.py#L1958-L2034)

Create an op that groups multiple operations.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.group`](https://www.tensorflow.org/api_docs/python/tf/group)

tf.group(
        *inputs, **kwargs
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Migrating model checkpoints](https://www.tensorflow.org/guide/migrate/migrating_checkpoints)<br>    <br>*   [Estimators](https://www.tensorflow.org/guide/estimator)<br>    <br>*   [Validating correctness & numerical equivalence](https://www.tensorflow.org/guide/migrate/validate_correctness) | *   [Wiki40B Language Models](https://www.tensorflow.org/hub/tutorials/wiki40b_lm) |

When this op finishes, all ops in `inputs` have finished. This op has no output.

When operating in a v1-style graph context, ops are not executed in the same order as specified in the code; TensorFlow will attempt to execute ops in parallel or in an order convenient to the result it is computing. [`tf.group`](https://www.tensorflow.org/api_docs/python/tf/group)
 allows you to request that one or more results finish before execution continues.

[`tf.group`](https://www.tensorflow.org/api_docs/python/tf/group)
 creates a single op (of type `NoOp`), and then adds appropriate control dependencies. Thus, `c = tf.group(a, b)` will compute the same graph as this:

with tf.control_dependencies([a, b]):
        c = tf.no_op()

See also [`tf.tuple`](https://www.tensorflow.org/api_docs/python/tf/tuple)
 and [`tf.control_dependencies`](https://www.tensorflow.org/api_docs/python/tf/control_dependencies)
.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `*inputs` | Zero or more tensors to group. |
| `name` | A name for this operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| An Operation that executes all its inputs. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If an unknown keyword argument is provided. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.