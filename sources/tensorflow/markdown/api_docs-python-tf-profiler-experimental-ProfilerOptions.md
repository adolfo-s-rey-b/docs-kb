[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/profiler/experimental/ProfilerOptions#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/profiler/experimental/ProfilerOptions)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/profiler/experimental/ProfilerOptions?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Fields](https://www.tensorflow.org/api_docs/python/tf/profiler/experimental/ProfilerOptions#fields)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/profiler/experimental/ProfilerOptions#attributes)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.profiler.experimental.ProfilerOptions Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================================

*   On this page
*   [Fields](https://www.tensorflow.org/api_docs/python/tf/profiler/experimental/ProfilerOptions#fields)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/profiler/experimental/ProfilerOptions#attributes)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/profiler/profiler_v2.py#L45-L77)

Options for finer control over the profiler.

tf.profiler.experimental.ProfilerOptions(
        host_tracer_level=2,
        python_tracer_level=0,
        device_tracer_level=1,
        delay_ms=None
    )

Use [`tf.profiler.experimental.ProfilerOptions`](https://www.tensorflow.org/api_docs/python/tf/profiler/experimental/ProfilerOptions)
 to control [`tf.profiler`](https://www.tensorflow.org/api_docs/python/tf/profiler)
 behavior.

|     |     |
| --- | --- |
| Fields<br>------ |     |
| `host_tracer_level` | Adjust CPU tracing level. Values are: `1` - critical info only, `2` - info, `3` - verbose. \[default value is `2`\] |
| `python_tracer_level` | Toggle tracing of Python function calls. Values are: `1` - enabled, `0` - disabled \[default value is `0`\] |
| `device_tracer_level` | Adjust device (TPU/GPU) tracing level. Values are: `1` - enabled, `0` - disabled \[default value is `1`\] |
| `delay_ms` | Requests for all hosts to start profiling at a timestamp that is `delay_ms` away from the current time. `delay_ms` is in milliseconds. If zero, each host will start profiling immediately upon receiving the request. Default value is `None`, allowing the profiler guess the best value. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `host_tracer_level` | A `namedtuple` alias for field number 0 |
| `python_tracer_level` | A `namedtuple` alias for field number 1 |
| `device_tracer_level` | A `namedtuple` alias for field number 2 |
| `delay_ms` | A `namedtuple` alias for field number 3 |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.