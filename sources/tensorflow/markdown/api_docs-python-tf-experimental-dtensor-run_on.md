[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/run_on#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/run_on)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/run_on?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/run_on#args)
    
*   [Yields](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/run_on#yields)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.experimental.dtensor.run\_on Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/run_on#args)
    
*   [Yields](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/run_on#yields)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/dtensor/python/api.py#L67-L86)

Runs enclosed functions in the DTensor device scope. (deprecated)

@contextlib.contextmanager

This function returns a scope. All the ops and tf.functions in this scope will run on the DTensor device using the mesh provided. This is useful for wrapping any tf.function that doesn't take a DTensor as input but would like to produce DTensor as result. The scope will also make sure all small constants be replicated as DTensor.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `mesh` | A Mesh instance to extract a default mesh from. |

|     |
| --- |
| Yields<br>------ |     |
| A context in which all ops and tf.functions will run on the DTensor device. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.