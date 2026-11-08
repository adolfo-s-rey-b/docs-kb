[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/profile#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/profile)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/profile?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/profile#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/profile#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.profiler.profile Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/profile#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/profile#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/profiler/model_analyzer.py#L310-L382)

Profile model.

tf.compat.v1.profiler.profile(
        graph=None,
        run_meta=None,
        op_log=None,
        cmd='scope',
        options=_DEFAULT_PROFILE_OPTIONS
    )

Tutorials and examples can be found in: [https://github.com/tensorflow/tensorflow/blob/master/tensorflow/core/profiler/g3doc/python\_api.md](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/core/profiler/g3doc/python_api.md)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `graph` | tf.Graph. If None and eager execution is not enabled, use default graph. |
| `run_meta` | optional tensorflow.RunMetadata proto. It is necessary to support run time information profiling, such as time and memory. |
| `op_log` | tensorflow.tfprof.OpLogProto proto. User can assign "types" to graph nodes with op\_log. "types" allow user to flexibly group and account profiles using options\['accounted\_type\_regexes'\]. |
| `cmd` | string. Either 'op', 'scope', 'graph' or 'code'. 'op' view organizes profile using operation type. (e.g. MatMul) 'scope' view organizes profile using graph node name scope. 'graph' view organizes profile using graph node inputs/outputs. 'code' view organizes profile using Python call stack. |
| `options` | A dict of options. See core/profiler/g3doc/options.md. |

|     |
| --- |
| Returns<br>------- |     |
| If cmd is 'scope' or 'graph', returns GraphNodeProto proto. If cmd is 'op' or 'code', returns MultiGraphNodeProto proto. Side effect: stdout/file/timeline.json depending on options\['output'\] |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.