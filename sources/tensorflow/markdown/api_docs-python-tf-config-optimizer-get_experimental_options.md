[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/config/optimizer/get_experimental_options#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/config/optimizer/get_experimental_options)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/config/optimizer/get_experimental_options?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fconfig%2Foptimizer%2Fget_experimental_options&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/config/optimizer/get_experimental_options#used-in-the-notebooks)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/config/optimizer/get_experimental_options#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.config.optimizer.get\_experimental\_options Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/config/optimizer/get_experimental_options#used-in-the-notebooks)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/config/optimizer/get_experimental_options#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/config.py#L202-L215)

Get experimental optimizer options.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.config.optimizer.get_experimental_options`](https://www.tensorflow.org/api_docs/python/tf/config/optimizer/get_experimental_options)

tf.config.optimizer.get_experimental_options()

### Used in the notebooks

| Used in the guide |
| --- |
| *   [TensorFlow graph optimization with Grappler](https://www.tensorflow.org/guide/graph_optimization) |

Refer to tf.config.optimizer.set\_experimental\_options for a list of current options.

Note that optimizations are only applied in graph mode, (within tf.function). In addition, as these are experimental options, the list is subject to change.

|     |
| --- |
| Returns<br>------- |     |
| Dictionary of configured experimental optimizer options |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.