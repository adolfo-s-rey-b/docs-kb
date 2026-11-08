[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/types/experimental/distributed/Mirrored#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/types/experimental/distributed/Mirrored)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/types/experimental/distributed/Mirrored?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.types.experimental.distributed.Mirrored Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/types/distribute.py#L182-L193)

Holds a distributed value: a map from replica id to synchronized values.

Inherits From: [`DistributedValues`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedValues)

`Mirrored` values are [`tf.distribute.DistributedValues`](https://www.tensorflow.org/api_docs/python/tf/distribute/DistributedValues)
 for which we know that the value on all replicas is the same. `Mirrored` values are kept synchronized by the distribution strategy in use, while `tf.types.experimental.PerReplica` values are left unsynchronized. `Mirrored` values typically represent model weights. We can safely read a `Mirrored` value in a cross-replica context by using the value on any replica, while `PerReplica` values should not be read or manipulated directly by the user in a cross-replica context.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.