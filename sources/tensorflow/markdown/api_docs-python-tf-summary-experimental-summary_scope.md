[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/summary/experimental/summary_scope#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/summary/experimental/summary_scope)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/summary/experimental/summary_scope?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/summary/experimental/summary_scope#args)
    
*   [Yields](https://www.tensorflow.org/api_docs/python/tf/summary/experimental/summary_scope#yields)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.summary.experimental.summary\_scope Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/summary/experimental/summary_scope#args)
    
*   [Yields](https://www.tensorflow.org/api_docs/python/tf/summary/experimental/summary_scope#yields)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/summary_ops_v2.py#L700-L738)

Experimental context manager for use when defining a custom summary op.

@tf_contextlib.contextmanager

This behaves similarly to [`tf.name_scope`](https://www.tensorflow.org/api_docs/python/tf/name_scope)
, except that it returns a generated summary tag in addition to the scope name. The tag is structurally similar to the scope name - derived from the user-provided name, prefixed with enclosing name scopes if any - but we relax the constraint that it be uniquified, as well as the character set limitation (so the user-provided name can contain characters not legal for scope names; in the scope name these are removed).

This makes the summary tag more predictable and consistent for the user.

For example, to define a new summary op called `my_op`:

def my_op(name, my_value, step):
      with tf.summary.summary_scope(name, "MyOp", [my_value]) as (tag, scope):
        my_value = tf.convert_to_tensor(my_value)
        return tf.summary.write(tag, my_value, step=step)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `name` | string name for the summary. |
| `default_name` | Optional; if provided, used as default name of the summary. |
| `values` | Optional; passed as `values` parameter to name\_scope. |

|     |
| --- |
| Yields<br>------ |     |
| A tuple `(tag, scope)` as described above. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.