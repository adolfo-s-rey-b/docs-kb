[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/forward_compatible#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/forward_compatible)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/forward_compatible?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/forward_compatible#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/forward_compatible#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.forward\_compatible Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/forward_compatible#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/forward_compatible#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/compat/compat.py#L65-L122)

Return true if the forward compatibility window has expired.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.compat.forward_compatible`](https://www.tensorflow.org/api_docs/python/tf/compat/forward_compatible)

tf.compat.forward_compatible(
        year, month, day
    )

See [Version compatibility](https://www.tensorflow.org/guide/versions#backward_and_partial_forward_compatibility)
.

Forward-compatibility refers to scenarios where the producer of a TensorFlow model (a GraphDef or SavedModel) is compiled against a version of the TensorFlow library newer than what the consumer was compiled against. The "producer" is typically a Python program that constructs and trains a model while the "consumer" is typically another program that loads and serves the model.

TensorFlow has been supporting a 3 week forward-compatibility window for programs compiled from source at HEAD.

For example, consider the case where a new operation `MyNewAwesomeAdd` is created with the intent of replacing the implementation of an existing Python wrapper - [`tf.add`](https://www.tensorflow.org/api_docs/python/tf/math/add)
. The Python wrapper implementation should change from something like:

def add(inputs, name=None):
      return gen_math_ops.add(inputs, name)

to:

from tensorflow.python.compat import compat
    
    def add(inputs, name=None):
      if compat.forward_compatible(year, month, day):
        # Can use the awesome new implementation.
        return gen_math_ops.my_new_awesome_add(inputs, name)
      # To maintain forward compatibility, use the old implementation.
      return gen_math_ops.add(inputs, name)

Where `year`, `month`, and `day` specify the date beyond which binaries that consume a model are expected to have been updated to include the new operations. This date is typically at least 3 weeks beyond the date the code that adds the new operation is committed.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `year` | A year (e.g., 2018). Must be an `int`. |
| `month` | A month (1 <= month <= 12) in year. Must be an `int`. |
| `day` | A day (1 <= day <= 31, or 30, or 29, or 28) in month. Must be an `int`. |

|     |
| --- |
| Returns<br>------- |     |
| True if the caller can expect that serialized TensorFlow graphs produced can be consumed by programs that are compiled with the TensorFlow library source code after (year, month, day). |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.