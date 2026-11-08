[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/advise#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/advise)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/advise?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/advise#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/advise#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.profiler.advise Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/advise#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/profiler/advise#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/profiler/model_analyzer.py#L385-L422)

Auto profile and advise.

tf.compat.v1.profiler.advise(
        graph=None, run_meta=None, options=_DEFAULT_ADVISE_OPTIONS
    )

Builds profiles and automatically check anomalies of various aspects. For more details: [https://github.com/tensorflow/tensorflow/tree/master/tensorflow/core/profiler/README.md](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/core/profiler/README.md)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `graph` | tf.Graph. If None and eager execution is not enabled, use default graph. |
| `run_meta` | optional tensorflow.RunMetadata proto. It is necessary to support run time information profiling, such as time and memory. |
| `options` | see ALL\_ADVICE example above. Default checks everything. |

|     |
| --- |
| Returns<br>------- |     |
| Returns AdviceProto proto |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.