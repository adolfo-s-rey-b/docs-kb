[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/distribute/ReduceOp#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/distribute/ReduceOp)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/distribute/ReduceOp?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tf/distribute/ReduceOp#class-variables)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.distribute.ReduceOp Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================

*   On this page
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tf/distribute/ReduceOp#class-variables)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/reduce_util.py#L23-L47)

Indicates how a set of values should be reduced.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.distribute.ReduceOp`](https://www.tensorflow.org/api_docs/python/tf/distribute/ReduceOp)

*   `SUM`: Add all the values.
*   `MEAN`: Take the arithmetic mean ("average") of the values.

|     |     |
| --- | --- |
| Class Variables<br>--------------- |     |
| MEAN | `<ReduceOp.MEAN: 'MEAN'>` |
| SUM | `<ReduceOp.SUM: 'SUM'>` |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.