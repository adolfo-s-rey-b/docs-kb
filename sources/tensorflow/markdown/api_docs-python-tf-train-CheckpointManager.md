[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointManager#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointManager)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointManager?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointManager#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointManager#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointManager#raises)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointManager#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointManager#methods)
    *   [restore\_or\_initialize](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointManager#restore_or_initialize)
        
    *   [save](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointManager#save)
        
    *   [sync](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointManager#sync)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.train.CheckpointManager Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointManager#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointManager#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointManager#raises)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointManager#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointManager#methods)
    *   [restore\_or\_initialize](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointManager#restore_or_initialize)
        
    *   [save](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointManager#save)
        
    *   [sync](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointManager#sync)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/checkpoint/checkpoint_management.py#L518-L902)

Manages multiple checkpoints by keeping some and deleting unneeded ones.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.train.CheckpointManager`](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointManager)

tf.train.CheckpointManager(
        checkpoint,
        directory,
        max_to_keep,
        keep_checkpoint_every_n_hours=None,
        checkpoint_name='ckpt',
        step_counter=None,
        checkpoint_interval=None,
        init_fn=None,
        last_checkpoint_step=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Training checkpoints](https://www.tensorflow.org/guide/checkpoint)<br>    <br>*   [tf.data: Build TensorFlow input pipelines](https://www.tensorflow.org/guide/data)<br>    <br>*   [Migrate the fault tolerance mechanism](https://www.tensorflow.org/guide/migrate/fault_tolerance) | *   [Distributed training with DTensors](https://www.tensorflow.org/tutorials/distribute/dtensor_ml_tutorial)<br>    <br>*   [Custom training loop with Keras and MultiWorkerMirroredStrategy](https://www.tensorflow.org/tutorials/distribute/multi_worker_with_ctl)<br>    <br>*   [Multi-worker training with Keras](https://www.tensorflow.org/tutorials/distribute/multi_worker_with_keras)<br>    <br>*   [CycleGAN](https://www.tensorflow.org/tutorials/generative/cyclegan)<br>    <br>*   [Training with Orbit](https://www.tensorflow.org/tfmodels/orbit/index) |

#### Example usage:

import tensorflow as tf
    checkpoint = tf.train.Checkpoint(optimizer=optimizer, model=model)
    manager = tf.train.CheckpointManager(
        checkpoint, directory="/tmp/model", max_to_keep=5)
    status = checkpoint.restore(manager.latest_checkpoint)
    while True:
      # train
      manager.save()

`CheckpointManager` preserves its own state across instantiations (see the `__init__` documentation for details). Only one should be active in a particular directory at a time.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `checkpoint` | The [`tf.train.Checkpoint`](https://www.tensorflow.org/api_docs/python/tf/train/Checkpoint)<br> instance to save and manage checkpoints for. |
| `directory` | The path to a directory in which to write checkpoints. A special file named "checkpoint" is also written to this directory (in a human-readable text format) which contains the state of the `CheckpointManager`. |
| `max_to_keep` | An integer, the number of checkpoints to keep. Unless preserved by `keep_checkpoint_every_n_hours`, checkpoints will be deleted from the active set, oldest first, until only `max_to_keep` checkpoints remain. If `None`, no checkpoints are deleted and everything stays in the active set. Note that `max_to_keep=None` will keep all checkpoint paths in memory and in the checkpoint state protocol buffer on disk. |
| `keep_checkpoint_every_n_hours` | Upon removal from the active set, a checkpoint will be preserved if it has been at least `keep_checkpoint_every_n_hours` since the last preserved checkpoint. The default setting of `None` does not preserve any checkpoints in this way. |
| `checkpoint_name` | Custom name for the checkpoint file. |
| `step_counter` | A [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable)<br> instance for checking the current step counter value, in case users want to save checkpoints every N steps. It should be passed if `checkpoint_interval` is not None. |
| `checkpoint_interval` | An integer, indicates the minimum step interval between two checkpoints. |
| `init_fn` | Callable. A function to do customized initialization if no checkpoints are in the directory. |
| `last_checkpoint_step` | An integer, indicating the step number of the last checkpoint saved. This will be used as the starting point for checking checkpoint\_interval against the current step. If None, the last checkpoint step will be set to None. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If `max_to_keep` is not a positive integer. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `checkpoint` | Returns the [`tf.train.Checkpoint`](https://www.tensorflow.org/api_docs/python/tf/train/Checkpoint)<br> object. |
| `checkpoint_interval` |     |
| `checkpoints` | A list of managed checkpoints.<br><br>Note that checkpoints saved due to `keep_checkpoint_every_n_hours` will not show up in this list (to avoid ever-growing filename lists). |
| `directory` |     |
| `latest_checkpoint` | The prefix of the most recent checkpoint in `directory`.<br><br>Equivalent to [`tf.train.latest_checkpoint(directory)`](https://www.tensorflow.org/api_docs/python/tf/train/latest_checkpoint)<br> where `directory` is the constructor argument to `CheckpointManager`.<br><br>Suitable for passing to [`tf.train.Checkpoint.restore`](https://www.tensorflow.org/api_docs/python/tf/train/Checkpoint#restore)<br> to resume training. |

Methods
-------

### `restore_or_initialize`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/checkpoint/checkpoint_management.py#L862-L897)

restore_or_initialize()

Restore items in `checkpoint` from the latest checkpoint file.

This method will first try to restore from the most recent checkpoint in `directory`. If no checkpoints exist in `directory`, and `init_fn` is specified, this method will call `init_fn` to do customized initialization. This can be used to support initialization from pretrained models.

Note that unlike [`tf.train.Checkpoint.restore()`](https://www.tensorflow.org/api_docs/python/tf/train/Checkpoint#restore)
, this method doesn't return a load status object that users can run assertions on (e.g. assert\_consumed()). Thus to run assertions, users should directly use [`tf.train.Checkpoint.restore()`](https://www.tensorflow.org/api_docs/python/tf/train/Checkpoint#restore)
 method.

|     |
| --- |
| Returns |     |
| The restored checkpoint path if the latest checkpoint is found and restored. Otherwise None. |     |

### `save`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/checkpoint/checkpoint_management.py#L766-L860)

save(
        checkpoint_number=None, check_interval=True, options=None
    )

Creates a new checkpoint and manages it.

|     |     |
| --- | --- |
| Args |     |
| `checkpoint_number` | An optional integer, or an integer-dtype `Variable` or `Tensor`, used to number the checkpoint. If `None` (default), checkpoints are numbered using `checkpoint.save_counter`. Even if `checkpoint_number` is provided, `save_counter` is still incremented. A user-provided `checkpoint_number` is not incremented even if it is a `Variable`. |
| `check_interval` | An optional boolean. The argument is only effective when `checkpoint_interval` is passed into the manager. If `True`, the manager will only save the checkpoint if the interval between checkpoints is larger than `checkpoint_interval`. Otherwise it will always save the checkpoint unless a checkpoint has already been saved for the current step. |
| `options` | Optional [`tf.train.CheckpointOptions`](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointOptions)<br> object. This argument only works with TF2 checkpoint objects. For example, options = tf.saved\_model.SaveOptions(experimental\_io\_device='/job:localhost') |

|     |
| --- |
| Returns |     |
| The path to the new checkpoint. It is also recorded in the `checkpoints` and `latest_checkpoint` properties. `None` if no checkpoint is saved. |     |

### `sync`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/checkpoint/checkpoint_management.py#L899-L902)

sync()

Wait for any outstanding save or restore operations.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.