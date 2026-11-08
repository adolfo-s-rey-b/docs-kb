[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/summary/SummaryWriter#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   English
*   中文 – 简体

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.summary.SummaryWriter Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/summary_ops_v2.py#L248-L316)

Interface representing a stateful summary writer object.

Methods
-------

### `as_default`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/summary_ops_v2.py#L272-L304)

as_default(
        step=None
    )

Returns a context manager that enables summary writing.

For convenience, if `step` is not None, this function also sets a default value for the `step` parameter used in summary-writing functions elsewhere in the API so that it need not be explicitly passed in every such invocation. The value can be a constant or a variable.

For example, `step` can be used as:

with writer_a.as_default(step=10):
      tf.summary.scalar(tag, value)   # Logged to writer_a with step 10
      with writer_b.as_default(step=20):
        tf.summary.scalar(tag, value) # Logged to writer_b with step 20
      tf.summary.scalar(tag, value)   # Logged to writer_a with step 10

|     |     |
| --- | --- |
| Args |     |
| `step` | An `int64`\-castable default step value, or `None`. When not `None`, the current step is captured, replaced by a given one, and the original one is restored when the context manager exits. When `None`, the current step is not modified (and not restored when the context manager exits). |

|     |
| --- |
| Returns |     |
| The context manager. |     |

### `close`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/summary_ops_v2.py#L314-L316)

close()

Flushes and closes the summary writer.

### `flush`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/summary_ops_v2.py#L310-L312)

flush()

Flushes any buffered data.

### `init`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/summary_ops_v2.py#L306-L308)

init()

Initializes the summary writer.

### `set_as_default`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/summary_ops_v2.py#L252-L270)

set_as_default(
        step=None
    )

Enables this summary writer for the current thread.

For convenience, if `step` is not None, this function also sets a default value for the `step` parameter used in summary-writing functions elsewhere in the API so that it need not be explicitly passed in every such invocation. The value can be a constant or a variable.

|     |     |
| --- | --- |
| Args |     |
| `step` | An `int64`\-castable default step value, or `None`. When not `None`, the current step is modified to the given value. When `None`, the current step is not modified. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.