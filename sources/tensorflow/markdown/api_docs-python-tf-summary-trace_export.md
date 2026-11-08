[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/summary/trace_export#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/summary/trace_export)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/summary/trace_export?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/summary/trace_export#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/summary/trace_export#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/summary/trace_export#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.summary.trace\_export Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/summary/trace_export#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/summary/trace_export#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/summary/trace_export#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/summary_ops_v2.py#L1410-L1462)

Stops and exports the active trace as a Summary and/or profile file.

tf.summary.trace_export(
        name, step=None, profiler_outdir=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Introduction to modules, layers, and models](https://www.tensorflow.org/guide/intro_to_modules) | *   [Examining the TensorFlow Graph](https://www.tensorflow.org/tensorboard/graphs) |

Stops the trace and exports all metadata collected during the trace to the default SummaryWriter, if one has been set.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `name` | A name for the summary to be written. |
| `step` | Explicit `int64`\-castable monotonic step value for this summary. If omitted, this defaults to [`tf.summary.experimental.get_step()`](https://www.tensorflow.org/api_docs/python/tf/summary/experimental/get_step)<br>, which must not be None. |
| `profiler_outdir` | This arg is a no-op. Please set this in trace\_on(). |

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