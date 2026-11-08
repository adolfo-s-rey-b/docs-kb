[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/PreemptionWatcher#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   English
*   中文 – 简体

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.distribute.experimental.PreemptionWatcher Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/failure_handling/preemption_watcher.py#L44-L137)

Watch preemption signal and store it.

tf.distribute.experimental.PreemptionWatcher()

Notice: Currently only support Borg TPU environment with TPUClusterResolver.

This class provides a way to monitor the preemption signal during training on TPU. It will start a background thread to watch the training process, trying to fetch preemption message from the coordination service. When preemption happens, the preempted worker will write the preemption message to the coordination service. Thus getting a non-empty preemption message means there is a preemption happened.

User can use the preemption message as a reliable preemption indicator, and then set the coordinator to reconnect to the TPU worker instead of a fully restart triggered by Borg. For example, a training process with preemption recovery will be like:

keep_running = True
    preemption_watcher = None
    while keep_running:
      try:
        # Initialize TPU cluster and stratygy.
        resolver = tf.distribute.cluster_resolver.TPUClusterResolver()
        tf.config.experimental_connect_to_cluster(resolver)
        tf.tpu.experimental.initialize_tpu_system(resolver)
        strategy = tf.distribute.TPUStrategy(resolver)
    
        # PreemptionWatcher must be created after connected to cluster.
        preemption_watcher = tf.distribute.experimental.PreemptionWatcher()
        train_model(strategy)
        keep_running = False
      except Exception as e:
        if preemption_watcher and preemption_watcher.preemption_message:
          preemption_watcher.block_until_worker_exit()
          keep_running = True
        else:
          raise e

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `preemption_message` | A variable to store the preemption message fetched from the coordination service. If it is not None, then there is a preemption happened. |
| `platform` | A PlatformDevice to indicate the current job's platform. Refer to failure\_handling\_util.py for the definition of enum class PlatformDevice. |

Methods
-------

### `block_until_worker_exit`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/failure_handling/preemption_watcher.py#L117-L137)

block_until_worker_exit()

Block coordinator until workers exit.

In some rare cases, another error could be raised during the preemption grace period. This will cause the coordinator to reconnect to the same TPU workers, which will be killed later. It prevents the coordinator to reconnect to new TPU workers, and falls back to a hard restart. To avoid this situation, this method will block the coordinator to reconnect until workers exit. This method will be a no-op for non-TPU platform.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.