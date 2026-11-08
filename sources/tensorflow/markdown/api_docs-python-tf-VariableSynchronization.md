[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/VariableSynchronization#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/VariableSynchronization)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/VariableSynchronization?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2FVariableSynchronization&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tf/VariableSynchronization#class-variables)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.VariableSynchronization Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================

*   On this page
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tf/VariableSynchronization#class-variables)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/variables.py#L64-L88)

Indicates when a distributed variable will be synced.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.VariableSynchronization`](https://www.tensorflow.org/api_docs/python/tf/VariableSynchronization)

*   `AUTO`: Indicates that the synchronization will be determined by the current `DistributionStrategy` (eg. With `MirroredStrategy` this would be `ON_WRITE`).
*   `NONE`: Indicates that there will only be one copy of the variable, so there is no need to sync.
*   `ON_WRITE`: Indicates that the variable will be updated across devices every time it is written.
*   `ON_READ`: Indicates that the variable will be aggregated across devices when it is read (eg. when checkpointing or when evaluating an op that uses the variable).
    
    Example:
    

>>> temp_grad=[tf.Variable([0.], trainable=False,\
    ...                      synchronization=tf.VariableSynchronization.ON_READ,\
    ...                      aggregation=tf.VariableAggregation.MEAN\
    ...                      )]

|     |     |
| --- | --- |
| Class Variables<br>--------------- |     |
| AUTO | `<VariableSynchronization.AUTO: 0>` |
| NONE | `<VariableSynchronization.NONE: 1>` |
| ON\_READ | `<VariableSynchronization.ON_READ: 3>` |
| ON\_WRITE | `<VariableSynchronization.ON_WRITE: 2>` |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.