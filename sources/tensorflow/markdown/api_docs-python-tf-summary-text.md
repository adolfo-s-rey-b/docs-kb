[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/summary/text#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/summary/text)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/summary/text?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fsummary%2Ftext&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/summary/text#used-in-the-notebooks)
    
*   [Arguments](https://www.tensorflow.org/api_docs/python/tf/summary/text#arguments)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/summary/text#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/summary/text#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.summary.text Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/summary/text#used-in-the-notebooks)
    
*   [Arguments](https://www.tensorflow.org/api_docs/python/tf/summary/text#arguments)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/summary/text#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/summary/text#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/summary/tb_summary.py#L302-L370)

Write a text summary.

tf.summary.text(
        name, data, step=None, description=None
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Displaying text data in TensorBoard](https://www.tensorflow.org/tensorboard/text_summaries) |

See also [`tf.summary.scalar`](https://www.tensorflow.org/api_docs/python/tf/summary/scalar)
, [`tf.summary.SummaryWriter`](https://www.tensorflow.org/api_docs/python/tf/summary/SummaryWriter)
, [`tf.summary.image`](https://www.tensorflow.org/api_docs/python/tf/summary/image)
.

Writes text Tensor values for later visualization and analysis in TensorBoard. Writes go to the current default summary writer. Like [`tf.summary.scalar`](https://www.tensorflow.org/api_docs/python/tf/summary/scalar)
 points, text points are each associated with a `step` and a `name`. All the points with the same `name` constitute a time series of text values.

#### For Example:

test_summary_writer = tf.summary.create_file_writer('test/logdir')
    with test_summary_writer.as_default():
        tf.summary.text('first_text', 'hello world!', step=0)
        tf.summary.text('first_text', 'nice to meet you!', step=1)

The text summary can also contain Markdown, and TensorBoard will render the text as such.

with test_summary_writer.as_default():
        text_data = '''
              | *hello* | *there* |
              |---------|---------|
              | this    | is      |
              | a       | table   |
        '''
        text_data = '\n'.join(l.strip() for l in text_data.splitlines())
        tf.summary.text('markdown_text', text_data, step=0)

Since text is Tensor valued, each text point may be a Tensor of string values. rank-1 and rank-2 Tensors are rendered as tables in TensorBoard. For higher ranked Tensors, you'll see just a 2D slice of the data. To avoid this, reshape the Tensor to at most rank-2 prior to passing it to this function.

Demo notebook at ["Displaying text data in TensorBoard"](https://www.tensorflow.org/tensorboard/text_summaries)
.

|     |     |
| --- | --- |
| Arguments<br>--------- |     |
| `name` | A name for this summary. The summary tag used for TensorBoard will be this name prefixed by any active name scopes. |
| `data` | A UTF-8 string Tensor value. |
| `step` | Explicit `int64`\-castable monotonic step value for this summary. If omitted, this defaults to [`tf.summary.experimental.get_step()`](https://www.tensorflow.org/api_docs/python/tf/summary/experimental/get_step)<br>, which must not be None. |
| `description` | Optional long-form description for this summary, as a constant `str`. Markdown is supported. Defaults to empty. |

|     |
| --- |
| Returns<br>------- |     |
| True on success, or false if no summary was emitted because no default summary writer was available. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | if a default writer exists, but no step was provided and [`tf.summary.experimental.get_step()`](https://www.tensorflow.org/api_docs/python/tf/summary/experimental/get_step)<br> is None. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.