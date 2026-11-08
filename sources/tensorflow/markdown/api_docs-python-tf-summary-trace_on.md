[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/summary/trace_on#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/summary/trace_on)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/summary/trace_on?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/summary/trace_on#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/summary/trace_on#args)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.summary.trace\_on Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/summary/trace_on#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/summary/trace_on#args)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/summary_ops_v2.py#L1354-L1405)

Starts a trace to record computation graphs and profiling information.

tf.summary.trace_on(
        graph=True, profiler=False, profiler_outdir=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Introduction to modules, layers, and models](https://www.tensorflow.org/guide/intro_to_modules) | *   [Examining the TensorFlow Graph](https://www.tensorflow.org/tensorboard/graphs) |

Must be invoked in eager mode.

When enabled, TensorFlow runtime will collect information that can later be exported and consumed by TensorBoard. The trace is activated across the entire TensorFlow runtime and affects all threads of execution.

To stop the trace and export the collected information, use [`tf.summary.trace_export`](https://www.tensorflow.org/api_docs/python/tf/summary/trace_export)
. To stop the trace without exporting, use [`tf.summary.trace_off`](https://www.tensorflow.org/api_docs/python/tf/summary/trace_off)
.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `graph` | If True, enables collection of executed graphs. It includes ones from tf.function invocation and ones from the legacy graph mode. The default is True. |
| `profiler` | If True, enables the advanced profiler. Enabling profiler implicitly enables the graph collection. The profiler may incur a high memory overhead. The default is False. |
| `profiler_outdir` | Output directory for profiler. It is required when profiler is enabled when trace was started. Otherwise, it is ignored. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.