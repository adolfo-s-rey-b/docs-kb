[Skip to main content](https://www.tensorflow.org/api_docs/python/orbit/actions/SaveCheckpointIfPreempted#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/orbit/actions/SaveCheckpointIfPreempted)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/orbit/actions/SaveCheckpointIfPreempted?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/orbit/actions/SaveCheckpointIfPreempted#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/orbit/actions/SaveCheckpointIfPreempted#methods)
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/orbit/actions/SaveCheckpointIfPreempted#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

orbit.actions.SaveCheckpointIfPreempted Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/orbit/actions/SaveCheckpointIfPreempted#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/orbit/actions/SaveCheckpointIfPreempted#methods)
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/orbit/actions/SaveCheckpointIfPreempted#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/orbit/actions/save_checkpoint_if_preempted.py#L22-L62)

Action that saves on-demand checkpoints after a preemption.

orbit.actions.SaveCheckpointIfPreempted(
        cluster_resolver: tf.distribute.cluster_resolver.ClusterResolver,
        checkpoint_manager: tf.train.CheckpointManager,
        checkpoint_number: Optional[tf.Variable] = None,
        keep_running_after_save: Optional[bool] = False
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `cluster_resolver` | A [`tf.distribute.cluster_resolver.ClusterResolver`](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/ClusterResolver)<br> object. |
| `checkpoint_manager` | A [`tf.train.CheckpointManager`](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointManager)<br> object. |
| `checkpoint_number` | A [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable)<br> to indicate the checkpoint\_number for checkpoint manager, usually it will be the global step. |
| `keep_running_after_save` | Whether to keep the job running after the preemption on-demand checkpoint. Only set to True when in-process preemption recovery with tf.distribute.experimental.PreemptionWatcher is enabled. |

Methods
-------

### `__call__`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/orbit/actions/save_checkpoint_if_preempted.py#L59-L62)

__call__(
        _
    ) -> None

Call self as a function.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-02-13 UTC.