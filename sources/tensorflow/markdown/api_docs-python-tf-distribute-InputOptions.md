[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/distribute/InputOptions#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/distribute/InputOptions)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/distribute/InputOptions?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/distribute/InputOptions#used-in-the-notebooks)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/distribute/InputOptions#attributes)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.distribute.InputOptions Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/distribute/InputOptions#used-in-the-notebooks)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/distribute/InputOptions#attributes)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/distribute_lib.py#L1014-L1079)

Run options for `experimental_distribute_dataset(s_from_function)`.

tf.distribute.InputOptions(
        experimental_fetch_to_device=None,
        experimental_replication_mode=tf.distribute.InputReplicationMode.PER_WORKER,
        experimental_place_dataset_on_device=False,
        experimental_per_replica_buffer_size=1
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Migrate from TPU embedding\_columns to TPUEmbedding layer](https://www.tensorflow.org/guide/migrate/tpu_embedding) | *   [TensorFlow 2 TPUEmbeddingLayer: Quick Start](https://www.tensorflow.org/recommenders/examples/tpu_embedding_layer) |

This can be used to hold some strategy specific configs.

# Setup TPUStrategy
    resolver = tf.distribute.cluster_resolver.TPUClusterResolver(tpu='')
    tf.config.experimental_connect_to_cluster(resolver)
    tf.tpu.experimental.initialize_tpu_system(resolver)
    strategy = tf.distribute.TPUStrategy(resolver)
    
    dataset = tf.data.Dataset.range(16)
    distributed_dataset_on_host = (
        strategy.experimental_distribute_dataset(
            dataset,
            tf.distribute.InputOptions(
                experimental_replication_mode=
                experimental_replication_mode.PER_WORKER,
                experimental_place_dataset_on_device=False,
                experimental_per_replica_buffer_size=1)))

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `experimental_fetch_to_device` | Boolean. If True, dataset elements will be prefetched to accelerator device memory. When False, dataset elements are prefetched to host device memory. Must be False when using TPUEmbedding API. experimental\_fetch\_to\_device can only be used with experimental\_replication\_mode=PER\_WORKER. Default behavior is same as setting it to True. |
| `experimental_replication_mode` | Replication mode for the input function. Currently, the InputReplicationMode.PER\_REPLICA is only supported with tf.distribute.MirroredStrategy. experimental\_distribute\_datasets\_from\_function. The default value is InputReplicationMode.PER\_WORKER. |
| `experimental_place_dataset_on_device` | Boolean. Default to False. When True, dataset will be placed on the device, otherwise it will remain on the host. experimental\_place\_dataset\_on\_device=True can only be used with experimental\_replication\_mode=PER\_REPLICA |
| `experimental_per_replica_buffer_size` | Integer. Default to 1. Indicates the prefetch buffer size in the replica device memory. Users can set it to 0 to completely disable prefetching behavior, or a number greater than 1 to enable larger buffer size. Note that this option is still valid with `experimental_fetch_to_device=False`. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.