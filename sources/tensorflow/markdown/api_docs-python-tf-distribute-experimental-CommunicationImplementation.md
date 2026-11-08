[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/CommunicationImplementation#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/CommunicationImplementation)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/CommunicationImplementation?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fdistribute%2Fexperimental%2FCommunicationImplementation&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/CommunicationImplementation#class-variables)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.distribute.experimental.CommunicationImplementation Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================================================

*   On this page
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/CommunicationImplementation#class-variables)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/collective_util.py#L26-L44)

Cross device communication implementation.

#### View aliases

**Main aliases**

[`tf.distribute.experimental.CollectiveCommunication`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/CommunicationImplementation)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.distribute.experimental.CollectiveCommunication`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/CommunicationImplementation)
, [`tf.compat.v1.distribute.experimental.CommunicationImplementation`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/CommunicationImplementation)

*   `AUTO`: Automatically chosen by Tensorflow.
*   `RING`: TensorFlow's ring algorithms for all-reduce and all-gather.
*   `NCCL`: NVIDIA®'s NCCL library. This is now only used for all-reduce on GPUs; all-reduce on CPU, all-gather and broadcast fallbacks to RING.

|     |     |
| --- | --- |
| Class Variables<br>--------------- |     |
| AUTO | `<CommunicationImplementation.AUTO: 'AUTO'>` |
| NCCL | `<CommunicationImplementation.NCCL: 'NCCL'>` |
| RING | `<CommunicationImplementation.RING: 'RING'>` |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.