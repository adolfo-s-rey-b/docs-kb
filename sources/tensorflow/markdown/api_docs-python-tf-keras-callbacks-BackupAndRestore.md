[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/BackupAndRestore#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/BackupAndRestore)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/BackupAndRestore?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/BackupAndRestore#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/BackupAndRestore#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/BackupAndRestore#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/BackupAndRestore#methods)
    *   [on\_batch\_begin](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/BackupAndRestore#on_batch_begin)
        
    *   [on\_batch\_end](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/BackupAndRestore#on_batch_end)
        
    *   [on\_epoch\_begin](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/BackupAndRestore#on_epoch_begin)
        
    *   [on\_epoch\_end](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/BackupAndRestore#on_epoch_end)
        
    *   [on\_predict\_batch\_begin](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/BackupAndRestore#on_predict_batch_begin)
        
    *   [on\_predict\_batch\_end](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/BackupAndRestore#on_predict_batch_end)
        
    *   [on\_predict\_begin](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/BackupAndRestore#on_predict_begin)
        
    *   [on\_predict\_end](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/BackupAndRestore#on_predict_end)
        
    *   [on\_test\_batch\_begin](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/BackupAndRestore#on_test_batch_begin)
        
    *   [on\_test\_batch\_end](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/BackupAndRestore#on_test_batch_end)
        
    *   [on\_test\_begin](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/BackupAndRestore#on_test_begin)
        
    *   [on\_test\_end](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/BackupAndRestore#on_test_end)
        
    *   [on\_train\_batch\_begin](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/BackupAndRestore#on_train_batch_begin)
        
    *   [on\_train\_batch\_end](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/BackupAndRestore#on_train_batch_end)
        
    *   [on\_train\_begin](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/BackupAndRestore#on_train_begin)
        
    *   [on\_train\_end](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/BackupAndRestore#on_train_end)
        
    *   [set\_model](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/BackupAndRestore#set_model)
        
    *   [set\_params](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/BackupAndRestore#set_params)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.callbacks.BackupAndRestore Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/BackupAndRestore#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/BackupAndRestore#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/BackupAndRestore#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/BackupAndRestore#methods)
    *   [on\_batch\_begin](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/BackupAndRestore#on_batch_begin)
        
    *   [on\_batch\_end](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/BackupAndRestore#on_batch_end)
        
    *   [on\_epoch\_begin](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/BackupAndRestore#on_epoch_begin)
        
    *   [on\_epoch\_end](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/BackupAndRestore#on_epoch_end)
        
    *   [on\_predict\_batch\_begin](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/BackupAndRestore#on_predict_batch_begin)
        
    *   [on\_predict\_batch\_end](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/BackupAndRestore#on_predict_batch_end)
        
    *   [on\_predict\_begin](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/BackupAndRestore#on_predict_begin)
        
    *   [on\_predict\_end](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/BackupAndRestore#on_predict_end)
        
    *   [on\_test\_batch\_begin](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/BackupAndRestore#on_test_batch_begin)
        
    *   [on\_test\_batch\_end](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/BackupAndRestore#on_test_batch_end)
        
    *   [on\_test\_begin](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/BackupAndRestore#on_test_begin)
        
    *   [on\_test\_end](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/BackupAndRestore#on_test_end)
        
    *   [on\_train\_batch\_begin](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/BackupAndRestore#on_train_batch_begin)
        
    *   [on\_train\_batch\_end](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/BackupAndRestore#on_train_batch_end)
        
    *   [on\_train\_begin](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/BackupAndRestore#on_train_begin)
        
    *   [on\_train\_end](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/BackupAndRestore#on_train_end)
        
    *   [set\_model](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/BackupAndRestore#set_model)
        
    *   [set\_params](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/BackupAndRestore#set_params)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/callbacks/backup_and_restore.py#L8-L210)

Callback to back up and restore the training state.

Inherits From: [`Callback`](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/Callback)

tf.keras.callbacks.BackupAndRestore(
        backup_dir,
        save_freq='epoch',
        double_checkpoint=False,
        delete_checkpoint=True
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Migrate the fault tolerance mechanism](https://www.tensorflow.org/guide/migrate/fault_tolerance) | *   [Multi-worker training with Keras](https://www.tensorflow.org/tutorials/distribute/multi_worker_with_keras)<br>    <br>*   [Parameter server training with ParameterServerStrategy](https://www.tensorflow.org/tutorials/distribute/parameter_server_training) |

`BackupAndRestore` callback is intended to recover training from an interruption that has happened in the middle of a [`Model.fit`](https://www.tensorflow.org/api_docs/python/tf/keras/Model#fit)
 execution, by backing up the training states in a temporary checkpoint file, at the end of each epoch. Each backup overwrites the previously written checkpoint file, so at any given time there is at most one such checkpoint file for backup/restoring purpose.

If training restarts before completion, the training state (which includes the `Model` weights and epoch number) is restored to the most recently saved state at the beginning of a new [`Model.fit`](https://www.tensorflow.org/api_docs/python/tf/keras/Model#fit)
 run. At the completion of a [`Model.fit`](https://www.tensorflow.org/api_docs/python/tf/keras/Model#fit)
 run, the temporary checkpoint file is deleted.

Note that the user is responsible to bring jobs back after the interruption. This callback is important for the backup and restore mechanism for fault tolerance purpose, and the model to be restored from a previous checkpoint is expected to be the same as the one used to back up. If user changes arguments passed to compile or fit, the checkpoint saved for fault tolerance can become invalid.

#### Example:

    class InterruptingCallback(keras.callbacks.Callback):

|     |     |
| --- | --- |
| Args<br>---- |     |
| `backup_dir` | String, path of directory where to store the data needed to restore the model. The directory cannot be reused elsewhere to store other files, e.g. by the `BackupAndRestore` callback of another training run, or by another callback (e.g. `ModelCheckpoint`) of the same training run. |
| `save_freq` | `"epoch"`, integer, or `False`. When set to `"epoch"` the callback saves the checkpoint at the end of each epoch. When set to an integer, the callback saves the checkpoint every `save_freq` batches. Set `save_freq=False` only if using preemption checkpointing (i.e. with `save_before_preemption=True`). |
| `double_checkpoint` | Boolean. If enabled, `BackupAndRestore` callback will save 2 last training states (current and previous). After interruption if current state can't be loaded due to IO error (e.g. file corrupted) it will try to restore previous one. Such behaviour will consume twice more space on disk, but increase fault tolerance. Defaults to `False`. |
| `delete_checkpoint` | Boolean. This `BackupAndRestore` callback works by saving a checkpoint to back up the training state. If `delete_checkpoint=True`, the checkpoint will be deleted after training is finished. Use `False` if you'd like to keep the checkpoint for future usage. Defaults to `True`. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `model` |     |

Methods
-------

### `on_batch_begin`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/callbacks/callback.py#L102-L104)

on_batch_begin(
        batch, logs=None
    )

A backwards compatibility alias for `on_train_batch_begin`.

### `on_batch_end`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/callbacks/callback.py#L106-L108)

on_batch_end(
        batch, logs=None
    )

A backwards compatibility alias for `on_train_batch_end`.

### `on_epoch_begin`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/callbacks/callback.py#L110-L121)

on_epoch_begin(
        epoch, logs=None
    )

Called at the start of an epoch.

Subclasses should override for any actions to run. This function should only be called during TRAIN mode.

|     |     |
| --- | --- |
| Args |     |
| `epoch` | Integer, index of epoch. |
| `logs` | Dict. Currently no data is passed to this argument for this method but that may change in the future. |

### `on_epoch_end`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/callbacks/backup_and_restore.py#L154-L158)

on_epoch_end(
        epoch, logs=None
    )

Called at the end of an epoch.

Subclasses should override for any actions to run. This function should only be called during TRAIN mode.

|     |     |
| --- | --- |
| Args |     |
| `epoch` | Integer, index of epoch. |
| `logs` | Dict, metric results for this training epoch, and for the validation epoch if validation is performed. Validation result keys are prefixed with `val_`. For training epoch, the values of the `Model`'s metrics are returned. Example: `{'loss': 0.2, 'accuracy': 0.7}`. |

### `on_predict_batch_begin`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/callbacks/callback.py#L211-L225)

on_predict_batch_begin(
        batch, logs=None
    )

Called at the beginning of a batch in `predict` methods.

Subclasses should override for any actions to run.

Note that if the `steps_per_execution` argument to `compile` in `Model` is set to `N`, this method will only be called every `N` batches.

|     |     |
| --- | --- |
| Args |     |
| `batch` | Integer, index of batch within the current epoch. |
| `logs` | Dict. Currently no data is passed to this argument for this method but that may change in the future. |

### `on_predict_batch_end`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/callbacks/callback.py#L227-L240)

on_predict_batch_end(
        batch, logs=None
    )

Called at the end of a batch in `predict` methods.

Subclasses should override for any actions to run.

Note that if the `steps_per_execution` argument to `compile` in `Model` is set to `N`, this method will only be called every `N` batches.

|     |     |
| --- | --- |
| Args |     |
| `batch` | Integer, index of batch within the current epoch. |
| `logs` | Dict. Aggregated metric results up until this batch. |

### `on_predict_begin`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/callbacks/callback.py#L288-L297)

on_predict_begin(
        logs=None
    )

Called at the beginning of prediction.

Subclasses should override for any actions to run.

|     |     |
| --- | --- |
| Args |     |
| `logs` | Dict. Currently no data is passed to this argument for this method but that may change in the future. |

### `on_predict_end`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/callbacks/callback.py#L299-L308)

on_predict_end(
        logs=None
    )

Called at the end of prediction.

Subclasses should override for any actions to run.

|     |     |
| --- | --- |
| Args |     |
| `logs` | Dict. Currently no data is passed to this argument for this method but that may change in the future. |

### `on_test_batch_begin`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/callbacks/callback.py#L174-L191)

on_test_batch_begin(
        batch, logs=None
    )

Called at the beginning of a batch in `evaluate` methods.

Also called at the beginning of a validation batch in the `fit` methods, if validation data is provided.

Subclasses should override for any actions to run.

Note that if the `steps_per_execution` argument to `compile` in `Model` is set to `N`, this method will only be called every `N` batches.

|     |     |
| --- | --- |
| Args |     |
| `batch` | Integer, index of batch within the current epoch. |
| `logs` | Dict. Currently no data is passed to this argument for this method but that may change in the future. |

### `on_test_batch_end`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/callbacks/callback.py#L193-L209)

on_test_batch_end(
        batch, logs=None
    )

Called at the end of a batch in `evaluate` methods.

Also called at the end of a validation batch in the `fit` methods, if validation data is provided.

Subclasses should override for any actions to run.

Note that if the `steps_per_execution` argument to `compile` in `Model` is set to `N`, this method will only be called every `N` batches.

|     |     |
| --- | --- |
| Args |     |
| `batch` | Integer, index of batch within the current epoch. |
| `logs` | Dict. Aggregated metric results up until this batch. |

### `on_test_begin`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/callbacks/callback.py#L265-L274)

on_test_begin(
        logs=None
    )

Called at the beginning of evaluation or validation.

Subclasses should override for any actions to run.

|     |     |
| --- | --- |
| Args |     |
| `logs` | Dict. Currently no data is passed to this argument for this method but that may change in the future. |

### `on_test_end`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/callbacks/callback.py#L276-L286)

on_test_end(
        logs=None
    )

Called at the end of evaluation or validation.

Subclasses should override for any actions to run.

|     |     |
| --- | --- |
| Args |     |
| `logs` | Dict. Currently the output of the last call to `on_test_batch_end()` is passed to this argument for this method but that may change in the future. |

### `on_train_batch_begin`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/callbacks/callback.py#L139-L155)

on_train_batch_begin(
        batch, logs=None
    )

Called at the beginning of a training batch in `fit` methods.

Subclasses should override for any actions to run.

Note that if the `steps_per_execution` argument to `compile` in `Model` is set to `N`, this method will only be called every `N` batches.

|     |     |
| --- | --- |
| Args |     |
| `batch` | Integer, index of batch within the current epoch. |
| `logs` | Dict. Currently no data is passed to this argument for this method but that may change in the future. |

### `on_train_batch_end`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/callbacks/backup_and_restore.py#L160-L162)

on_train_batch_end(
        batch, logs=None
    )

Called at the end of a training batch in `fit` methods.

Subclasses should override for any actions to run.

Note that if the `steps_per_execution` argument to `compile` in `Model` is set to `N`, this method will only be called every `N` batches.

|     |     |
| --- | --- |
| Args |     |
| `batch` | Integer, index of batch within the current epoch. |
| `logs` | Dict. Aggregated metric results up until this batch. |

### `on_train_begin`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/callbacks/backup_and_restore.py#L113-L128)

on_train_begin(
        logs=None
    )

Called at the beginning of training.

Subclasses should override for any actions to run.

|     |     |
| --- | --- |
| Args |     |
| `logs` | Dict. Currently no data is passed to this argument for this method but that may change in the future. |

### `on_train_end`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/callbacks/backup_and_restore.py#L208-L210)

on_train_end(
        logs=None
    )

Called at the end of training.

Subclasses should override for any actions to run.

|     |     |
| --- | --- |
| Args |     |
| `logs` | Dict. Currently the output of the last call to `on_epoch_end()` is passed to this argument for this method but that may change in the future. |

### `set_model`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/callbacks/callback.py#L74-L75)

set_model(
        model
    )

### `set_params`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/callbacks/callback.py#L71-L72)

set_params(
        params
    )

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.