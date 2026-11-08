None

[Keras 3 API documentation](https://keras.io/api/)

[Models API](https://keras.io/api/models/)
 [Layers API](https://keras.io/api/layers/)
 [Callbacks API](https://keras.io/api/callbacks/)
 [Base Callback class](https://keras.io/api/callbacks/base_callback/)
 [ModelCheckpoint](https://keras.io/api/callbacks/model_checkpoint/)
 [BackupAndRestore](https://keras.io/api/callbacks/backup_and_restore/)
 [TensorBoard](https://keras.io/api/callbacks/tensorboard/)
 [EarlyStopping](https://keras.io/api/callbacks/early_stopping/)
 [LearningRateScheduler](https://keras.io/api/callbacks/learning_rate_scheduler/)
 [ReduceLROnPlateau](https://keras.io/api/callbacks/reduce_lr_on_plateau/)
 [RemoteMonitor](https://keras.io/api/callbacks/remote_monitor/)
 [LambdaCallback](https://keras.io/api/callbacks/lambda_callback/)
 [TerminateOnNaN](https://keras.io/api/callbacks/terminate_on_nan/)
 [CSVLogger](https://keras.io/api/callbacks/csv_logger/)
 [ProgbarLogger](https://keras.io/api/callbacks/progbar_logger/)
 [SwapEMAWeights](https://keras.io/api/callbacks/swap_ema_weights/)
 [OrbaxCheckpoint](https://keras.io/api/callbacks/orbax_checkpoint/)
 [Ops API](https://keras.io/api/ops/)
 [Optimizers](https://keras.io/api/optimizers/)
 [Metrics](https://keras.io/api/metrics/)
 [Losses](https://keras.io/api/losses/)
 [Data loading](https://keras.io/api/data_loading/)
 [Tree API](https://keras.io/api/tree/)
 [Built-in small datasets](https://keras.io/api/datasets/)
 [Keras Applications](https://keras.io/api/applications/)
 [Mixed precision](https://keras.io/api/mixed_precision/)
 [Multi-device distribution](https://keras.io/api/distribution/)
 [RNG API](https://keras.io/api/random/)
 [Quantizers](https://keras.io/api/quantizers/)
 [Scope](https://keras.io/api/scope/)
 [Rematerialization](https://keras.io/api/rematerialization/)
 [Utilities](https://keras.io/api/utils/)

[Keras 2 API documentation](https://keras.io/2/api/)

► [Keras 3 API documentation](https://keras.io/api/)
 / [Callbacks API](https://keras.io/api/callbacks/)
 / BackupAndRestore

BackupAndRestore
================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/callbacks/backup_and_restore.py#L8)

### `BackupAndRestore` class

Copied!

`keras.callbacks.BackupAndRestore(     backup_dir, save_freq="epoch", double_checkpoint=False, delete_checkpoint=True )`

Callback to back up and restore the training state.

`BackupAndRestore` callback is intended to recover training from an interruption that has happened in the middle of a `Model.fit` execution, by backing up the training states in a temporary checkpoint file, at the end of each epoch. Each backup overwrites the previously written checkpoint file, so at any given time there is at most one such checkpoint file for backup/restoring purpose.

If training restarts before completion, the training state (which includes the `Model` weights and epoch number) is restored to the most recently saved state at the beginning of a new `Model.fit` run. At the completion of a `Model.fit` run, the temporary checkpoint file is deleted.

Note that the user is responsible to bring jobs back after the interruption. This callback is important for the backup and restore mechanism for fault tolerance purpose, and the model to be restored from a previous checkpoint is expected to be the same as the one used to back up. If user changes arguments passed to compile or fit, the checkpoint saved for fault tolerance can become invalid.

**Example**

Copied!

`>>> class InterruptingCallback(keras.callbacks.Callback): ...   def on_epoch_begin(self, epoch, logs=None): ...     if epoch == 4: ...       raise RuntimeError('Interrupting!') >>> callback = keras.callbacks.BackupAndRestore(backup_dir="/tmp/backup") >>> model = keras.models.Sequential([keras.layers.Dense(10)]) >>> model.compile(keras.optimizers.SGD(), loss='mse') >>> model.build(input_shape=(None, 20)) >>> try: ...   model.fit(np.arange(100).reshape(5, 20), np.zeros(5), epochs=10, ...             batch_size=1, callbacks=[callback, InterruptingCallback()], ...             verbose=0) ... except: ...   pass >>> history = model.fit(np.arange(100).reshape(5, 20), np.zeros(5), ...                     epochs=10, batch_size=1, callbacks=[callback], ...                     verbose=0) >>> # Only 6 more epochs are run, since first training got interrupted at >>> # zero-indexed epoch 4, second training will continue from 4 to 9. >>> len(history.history['loss']) >>> 6`

**Arguments**

*   **backup\_dir**: String, path of directory where to store the data needed to restore the model. The directory cannot be reused elsewhere to store other files, e.g. by the `BackupAndRestore` callback of another training run, or by another callback (e.g. `ModelCheckpoint`) of the same training run.
*   **save\_freq**: `"epoch"`, integer, or `False`. When set to `"epoch"` the callback saves the checkpoint at the end of each epoch. When set to an integer, the callback saves the checkpoint every `save_freq` batches. Set `save_freq=False` only if using preemption checkpointing (i.e. with `save_before_preemption=True`).
*   **double\_checkpoint**: Boolean. If enabled, `BackupAndRestore` callback will save 2 last training states (current and previous). After interruption if current state can't be loaded due to IO error (e.g. file corrupted) it will try to restore previous one. Such behaviour will consume twice more space on disk, but increase fault tolerance. Defaults to `False`.
*   **delete\_checkpoint**: Boolean. This `BackupAndRestore` callback works by saving a checkpoint to back up the training state. If `delete_checkpoint=True`, the checkpoint will be deleted after training is finished. Use `False` if you'd like to keep the checkpoint for future usage. Defaults to `True`.

* * *

[BackupAndRestore](https://keras.io/api/callbacks/backup_and_restore/#backupandrestore)

[`BackupAndRestore` class](https://keras.io/api/callbacks/backup_and_restore/#backupandrestore-class)