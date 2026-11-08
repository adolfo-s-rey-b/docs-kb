[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/summary/scalar#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/summary/scalar)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/summary/scalar?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fsummary%2Fscalar&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/summary/scalar#used-in-the-notebooks)
    
*   [Arguments](https://www.tensorflow.org/api_docs/python/tf/summary/scalar#arguments)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/summary/scalar#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/summary/scalar#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.summary.scalar Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/summary/scalar#used-in-the-notebooks)
    
*   [Arguments](https://www.tensorflow.org/api_docs/python/tf/summary/scalar#arguments)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/summary/scalar#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/summary/scalar#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/summary/tb_summary.py#L243-L299)

Write a scalar summary.

tf.summary.scalar(
        name, data, step=None, description=None
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [pix2pix: Image-to-image translation with a conditional GAN](https://www.tensorflow.org/tutorials/generative/pix2pix)<br>    <br>*   [TensorBoard Scalars: Logging training metrics in Keras](https://www.tensorflow.org/tensorboard/scalars_and_keras)<br>    <br>*   [Get started with TensorBoard](https://www.tensorflow.org/tensorboard/get_started)<br>    <br>*   [Research tools](https://www.tensorflow.org/quantum/tutorials/research_tools)<br>    <br>*   [Migrating tf.summary usage to TF 2.x](https://www.tensorflow.org/tensorboard/migrate) |

See also [`tf.summary.image`](https://www.tensorflow.org/api_docs/python/tf/summary/image)
, [`tf.summary.histogram`](https://www.tensorflow.org/api_docs/python/tf/summary/histogram)
, [`tf.summary.SummaryWriter`](https://www.tensorflow.org/api_docs/python/tf/summary/SummaryWriter)
.

Writes simple numeric values for later analysis in TensorBoard. Writes go to the current default summary writer. Each summary point is associated with an integral `step` value. This enables the incremental logging of time series data. A common usage of this API is to log loss during training to produce a loss curve.

#### For example:

test_summary_writer = tf.summary.create_file_writer('test/logdir')
    with test_summary_writer.as_default():
        tf.summary.scalar('loss', 0.345, step=1)
        tf.summary.scalar('loss', 0.234, step=2)
        tf.summary.scalar('loss', 0.123, step=3)

Multiple independent time series may be logged by giving each series a unique `name` value.

See [Get started with TensorBoard](https://www.tensorflow.org/tensorboard/get_started)
 for more examples of effective usage of [`tf.summary.scalar`](https://www.tensorflow.org/api_docs/python/tf/summary/scalar)
.

In general, this API expects that data points are logged with a monotonically increasing step value. Duplicate points for a single step or points logged out of order by step are not guaranteed to display as desired in TensorBoard.

|     |     |
| --- | --- |
| Arguments<br>--------- |     |
| `name` | A name for this summary. The summary tag used for TensorBoard will be this name prefixed by any active name scopes. |
| `data` | A real numeric scalar value, convertible to a `float32` Tensor. |
| `step` | Explicit `int64`\-castable monotonic step value for this summary. If omitted, this defaults to [`tf.summary.experimental.get_step()`](https://www.tensorflow.org/api_docs/python/tf/summary/experimental/get_step)<br>, which must not be None. |
| `description` | Optional long-form description for this summary, as a constant `str`. Markdown is supported. Defaults to empty. |

|     |
| --- |
| Returns<br>------- |     |
| True on success, or false if no summary was written because no default summary writer was available. |     |

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