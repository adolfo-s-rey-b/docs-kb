[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/AggregationMethod#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/AggregationMethod)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/AggregationMethod?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tf/AggregationMethod#class-variables)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.AggregationMethod Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================

*   On this page
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tf/AggregationMethod#class-variables)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/gradients_util.py#L952-L996)

A class listing aggregation methods used to combine gradients.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.AggregationMethod`](https://www.tensorflow.org/api_docs/python/tf/AggregationMethod)

Computing partial derivatives can require aggregating gradient contributions. This class lists the various methods that can be used to combine gradients in the graph.

The following aggregation methods are part of the stable API for aggregating gradients:

*   `ADD_N`: All of the gradient terms are summed as part of one operation using the "AddN" op (see [`tf.add_n`](https://www.tensorflow.org/api_docs/python/tf/math/add_n)
    ). This method has the property that all gradients must be ready and buffered separately in memory before any aggregation is performed.
*   `DEFAULT`: The system-chosen default aggregation method.

The following aggregation methods are experimental and may not be supported in future releases:

*   `EXPERIMENTAL_TREE`: Gradient terms are summed in pairs using the "AddN" op. This method of summing gradients may reduce performance, but it can improve memory utilization because the gradients can be released earlier.
*   `EXPERIMENTAL_ACCUMULATE_N`: Same as `EXPERIMENTAL_TREE`.

Example usage when computing gradient:

    @tf.function

|     |     |
| --- | --- |
| Class Variables<br>--------------- |     |
| ADD\_N | `0` |
| DEFAULT | `0` |
| EXPERIMENTAL\_ACCUMULATE\_N | `2` |
| EXPERIMENTAL\_TREE | `1` |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.