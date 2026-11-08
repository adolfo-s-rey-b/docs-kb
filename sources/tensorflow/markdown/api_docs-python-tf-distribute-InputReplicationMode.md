[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/distribute/InputReplicationMode#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/distribute/InputReplicationMode)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/distribute/InputReplicationMode?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tf/distribute/InputReplicationMode#class-variables)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.distribute.InputReplicationMode Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================================

*   On this page
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tf/distribute/InputReplicationMode#class-variables)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/distribute_lib.py#L823-L837)

Replication mode for input function.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.distribute.InputReplicationMode`](https://www.tensorflow.org/api_docs/python/tf/distribute/InputReplicationMode)

*   `PER_WORKER`: The input function will be called on each worker independently, creating as many input pipelines as number of workers. Replicas will dequeue from the local Dataset on their worker. [`tf.distribute.Strategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy)
     doesn't manage any state sharing between such separate input pipelines.
*   `PER_REPLICA`: The input function will be called on each replica separately. [`tf.distribute.Strategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy)
     doesn't manage any state sharing between such separate input pipelines.

|     |     |
| --- | --- |
| Class Variables<br>--------------- |     |
| PER\_REPLICA | `<InputReplicationMode.PER_REPLICA: 'PER_REPLICA'>` |
| PER\_WORKER | `<InputReplicationMode.PER_WORKER: 'PER_WORKER'>` |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.