None

[Keras 3 API documentation](https://keras.io/api/)
 [Keras 2 API documentation](https://keras.io/2/api/)

[Models API](https://keras.io/2/api/models/)
 [Layers API](https://keras.io/2/api/layers/)
 [Callbacks API](https://keras.io/2/api/callbacks/)
 [Base Callback class](https://keras.io/2/api/callbacks/base_callback/)
 [ModelCheckpoint](https://keras.io/2/api/callbacks/model_checkpoint/)
 [BackupAndRestore](https://keras.io/2/api/callbacks/backup_and_restore/)
 [TensorBoard](https://keras.io/2/api/callbacks/tensorboard/)
 [EarlyStopping](https://keras.io/2/api/callbacks/early_stopping/)
 [LearningRateScheduler](https://keras.io/2/api/callbacks/learning_rate_scheduler/)
 [ReduceLROnPlateau](https://keras.io/2/api/callbacks/reduce_lr_on_plateau/)
 [RemoteMonitor](https://keras.io/2/api/callbacks/remote_monitor/)
 [LambdaCallback](https://keras.io/2/api/callbacks/lambda_callback/)
 [TerminateOnNaN](https://keras.io/2/api/callbacks/terminate_on_nan/)
 [CSVLogger](https://keras.io/2/api/callbacks/csv_logger/)
 [ProgbarLogger](https://keras.io/2/api/callbacks/progbar_logger/)
 [Optimizers](https://keras.io/2/api/optimizers/)
 [Metrics](https://keras.io/2/api/metrics/)
 [Losses](https://keras.io/2/api/losses/)
 [Data loading](https://keras.io/2/api/data_loading/)
 [Built-in small datasets](https://keras.io/2/api/datasets/)
 [Keras Applications](https://keras.io/2/api/applications/)
 [Mixed precision](https://keras.io/2/api/mixed_precision/)
 [Utilities](https://keras.io/2/api/utils/)

► [Keras 2 API documentation](https://keras.io/2/api/)
 / [Callbacks API](https://keras.io/2/api/callbacks/)
 / BackupAndRestore

BackupAndRestore
================

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/callbacks.py#L1754)

### `BackupAndRestore` class

Copied!

`tf_keras.callbacks.BackupAndRestore(     backup_dir, save_freq="epoch", delete_checkpoint=True, save_before_preemption=False )`

Callback to back up and restore the training state.

`BackupAndRestore` callback is intended to recover training from an interruption that has happened in the middle of a `Model.fit` execution, by backing up the training states in a temporary checkpoint file (with the help of a [`tf.train.CheckpointManager`](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointManager)
), at the end of each epoch. Each backup overwrites the previously written checkpoint file, so at any given time there is at most one such checkpoint file for backup/restoring purpose.

If training restarts before completion, the training state (which includes the `Model` weights and epoch number) is restored to the most recently saved state at the beginning of a new `Model.fit` run. At the completion of a `Model.fit` run, the temporary checkpoint file is deleted.

Note that the user is responsible to bring jobs back after the interruption. This callback is important for the backup and restore mechanism for fault tolerance purpose, and the model to be restored from a previous checkpoint is expected to be the same as the one used to back up. If user changes arguments passed to compile or fit, the checkpoint saved for fault tolerance can become invalid.

Note:

1.  This callback is not compatible with eager execution disabled.
2.  A checkpoint is saved at the end of each epoch. After restoring, `Model.fit` redoes any partial work during the unfinished epoch in which the training got restarted (so the work done before the interruption doesn't affect the final model state).
3.  This works for both single worker and multi-worker modes. When `Model.fit` is used with [`tf.distribute`](https://www.tensorflow.org/api_docs/python/tf/distribute)
    , it supports [`tf.distribute.MirroredStrategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/MirroredStrategy)
    , [`tf.distribute.MultiWorkerMirroredStrategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/MultiWorkerMirroredStrategy)
    , [`tf.distribute.TPUStrategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/TPUStrategy)
    , and [`tf.distribute.experimental.ParameterServerStrategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/ParameterServerStrategy)
    .

**Example**

Copied!

`>>> class InterruptingCallback(tf.keras.callbacks.Callback): ...   def on_epoch_begin(self, epoch, logs=None): ...     if epoch == 4: ...       raise RuntimeError('Interrupting!') >>> callback = tf.keras.callbacks.BackupAndRestore(backup_dir="/tmp/backup") >>> model = tf.keras.models.Sequential([tf.keras.layers.Dense(10)]) >>> model.compile(tf.keras.optimizers.SGD(), loss='mse') >>> try: ...   model.fit(np.arange(100).reshape(5, 20), np.zeros(5), epochs=10, ...             batch_size=1, callbacks=[callback, InterruptingCallback()], ...             verbose=0) ... except: ...   pass >>> history = model.fit(np.arange(100).reshape(5, 20), np.zeros(5), ...                     epochs=10, batch_size=1, callbacks=[callback], ...                     verbose=0) >>> # Only 6 more epochs are run, since first training got interrupted at >>> # zero-indexed epoch 4, second training will continue from 4 to 9. >>> len(history.history['loss']) 6`

Besides the option to save at the end of every epoch or every N steps, if you are doing distributed training with [`tf.distribute.MultiWorkerMirroredStrategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/MultiWorkerMirroredStrategy)
 on Google Cloud Platform or Google Borg, you can also use the `save_before_preemption` argument to enable saving a checkpoint right before a worker gets preempted by other jobs and training gets interrupted. See [`tf.distribute.experimental.PreemptionCheckpointHandler`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/PreemptionCheckpointHandler)
 for more details.

**Arguments**

*   **backup\_dir**: String, path to store the checkpoint. e.g. `backup_dir = os.path.join(working_dir, 'backup')`. This is the directory in which the system stores temporary files to recover the model from jobs terminated unexpectedly. The directory cannot be reused elsewhere to store other files, e.g. by the `BackupAndRestore` callback of another training run, or by another callback (e.g. `ModelCheckpoint`) of the same training.
*   **save\_freq**: `'epoch'`, integer, or `False`. When set to `'epoch'` the callback saves the checkpoint at the end of each epoch. When set to an integer, the callback saves the checkpoint every `save_freq` batches. Set `save_freq` to `False` if only using preemption checkpointing (with `save_before_preemption=True`).
*   **delete\_checkpoint**: Boolean, default to True. This `BackupAndRestore` callback works by saving a checkpoint to back up the training state. If `delete_checkpoint=True`, the checkpoint will be deleted after training is finished. Use `False` if you'd like to keep the checkpoint for future usage.
*   **save\_before\_preemption**: A boolean value instructing whether to turn on the automatic checkpoint saving for preemption/maintenance events. This only supports [`tf.distribute.MultiWorkerMirroredStrategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/MultiWorkerMirroredStrategy)
     on Google Cloud Platform or Google Borg for now.

* * *

[BackupAndRestore](https://keras.io/2/api/callbacks/backup_and_restore/#backupandrestore)

[`BackupAndRestore` class](https://keras.io/2/api/callbacks/backup_and_restore/#backupandrestore-class)