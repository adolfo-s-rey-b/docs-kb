[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/profiler/experimental/stop#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/profiler/experimental/stop)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/profiler/experimental/stop?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fprofiler%2Fexperimental%2Fstop&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/profiler/experimental/stop#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/profiler/experimental/stop#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/profiler/experimental/stop#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.profiler.experimental.stop Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/profiler/experimental/stop#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/profiler/experimental/stop#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/profiler/experimental/stop#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/profiler/profiler_v2.py#L129-L153)

Stops the current profiling session.

tf.profiler.experimental.stop(
        save=True
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Research tools](https://www.tensorflow.org/quantum/tutorials/research_tools) |

The profiler session will be stopped and profile results can be saved.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `save` | An optional variable to save the results to TensorBoard. Default True. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `UnavailableError` | If there is no active profiling session. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.