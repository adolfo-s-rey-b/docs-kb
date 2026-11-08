[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/summary/histogram#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/summary/histogram)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/summary/histogram?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/summary/histogram#used-in-the-notebooks)
    
*   [Arguments](https://www.tensorflow.org/api_docs/python/tf/summary/histogram#arguments)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/summary/histogram#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/summary/histogram#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.summary.histogram Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/summary/histogram#used-in-the-notebooks)
    
*   [Arguments](https://www.tensorflow.org/api_docs/python/tf/summary/histogram#arguments)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/summary/histogram#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/summary/histogram#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/summary/tb_summary.py#L85-L158)

Write a histogram summary.

tf.summary.histogram(
        name, data, step=None, buckets=None, description=None
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Research tools](https://www.tensorflow.org/quantum/tutorials/research_tools) |

See also [`tf.summary.scalar`](https://www.tensorflow.org/api_docs/python/tf/summary/scalar)
, [`tf.summary.SummaryWriter`](https://www.tensorflow.org/api_docs/python/tf/summary/SummaryWriter)
.

Writes a histogram to the current default summary writer, for later analysis in TensorBoard's 'Histograms' and 'Distributions' dashboards (data written using this API will appear in both places). Like [`tf.summary.scalar`](https://www.tensorflow.org/api_docs/python/tf/summary/scalar)
 points, each histogram is associated with a `step` and a `name`. All the histograms with the same `name` constitute a time series of histograms.

The histogram is calculated over all the elements of the given `Tensor` without regard to its shape or rank.

This example writes 2 histograms:

w = tf.summary.create_file_writer('test/logs')
    with w.as_default():
        tf.summary.histogram("activations", tf.random.uniform([100, 50]), step=0)
        tf.summary.histogram("initial_weights", tf.random.normal([1000]), step=0)

A common use case is to examine the changing activation patterns (or lack thereof) at specific layers in a neural network, over time.

w = tf.summary.create_file_writer('test/logs')
    with w.as_default():
    for step in range(100):
        # Generate fake "activations".
        activations = [\
            tf.random.normal([1000], mean=step, stddev=1),\
            tf.random.normal([1000], mean=step, stddev=10),\
            tf.random.normal([1000], mean=step, stddev=100),\
        ]
    
        tf.summary.histogram("layer1/activate", activations[0], step=step)
        tf.summary.histogram("layer2/activate", activations[1], step=step)
        tf.summary.histogram("layer3/activate", activations[2], step=step)

|     |     |
| --- | --- |
| Arguments<br>--------- |     |
| `name` | A name for this summary. The summary tag used for TensorBoard will be this name prefixed by any active name scopes. |
| `data` | A `Tensor` of any shape. The histogram is computed over its elements, which must be castable to `float64`. |
| `step` | Explicit `int64`\-castable monotonic step value for this summary. If omitted, this defaults to [`tf.summary.experimental.get_step()`](https://www.tensorflow.org/api_docs/python/tf/summary/experimental/get_step)<br>, which must not be None. |
| `buckets` | Optional positive `int`. The output will have this many buckets, except in two edge cases. If there is no data, then there are no buckets. If there is data but all points have the same value, then all buckets' left and right endpoints are the same and only the last bucket has nonzero count. Defaults to 30 if not specified. |
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