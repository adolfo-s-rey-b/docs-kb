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
 / OrbaxCheckpoint

OrbaxCheckpoint
===============

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/callbacks/orbax_checkpoint.py#L57)

### `OrbaxCheckpoint` class

Copied!

`keras.callbacks.OrbaxCheckpoint(     directory,     monitor="val_loss",     verbose=0,     save_best_only=False,     mode="auto",     save_freq="epoch",     initial_value_threshold=None,     max_to_keep=1,     save_on_background=True,     save_weights_only=False, )`

Callback to save and load model state using Orbax with a similar API to ModelCheckpoint.

This callback saves the model's weights and optimizer state asynchronously using Orbax, allowing training to continue without blocking for I/O.

**Multi-host Support**: When running in a multi-host distributed training environment with JAX backend, this callback automatically coordinates checkpointing across all hosts to ensure consistency and proper synchronization. Multi-host checkpointing is only supported on JAX.

**Example**

Copied!

`model.compile(loss=..., optimizer=..., metrics=['accuracy'])  EPOCHS = 10 checkpoint_dir = '/tmp/ckpt' orbax_checkpoint_callback = keras.callbacks.OrbaxCheckpoint(     directory=checkpoint_dir,     monitor='val_accuracy',     mode='max',     save_best_only=True)  # Model is saved at the end of every epoch, if it's the best seen so far. model.fit(epochs=EPOCHS, callbacks=[orbax_checkpoint_callback])  # Alternatively, save checkpoints every N batches - orbax_checkpoint_callback = keras.callbacks.OrbaxCheckpoint(     directory=checkpoint_dir,     save_freq=100)  # Save every 100 batches  model.fit(epochs=EPOCHS, callbacks=[orbax_checkpoint_callback])`

**Arguments**

*   **directory**: path to the directory where to save the checkpoints.
*   **monitor**: The metric name to monitor (e.g., 'val\_loss').
*   **verbose**: Verbosity mode, 0 or 1.
*   **save\_best\_only**: if `save_best_only=True`, it only saves when the model is considered the "best" based on the monitored quantity.
*   **mode**: one of {'auto', 'min', 'max'}. Used with `save_best_only`.
*   **save\_freq**: `'epoch'` or integer. Frequency to save checkpoints.
*   **max\_to\_keep**: Integer, maximum number of recent checkpoints to keep. If None, keeps all. Defaults to 1.
*   **save\_on\_background**: Boolean, whether to save asynchronously in the background. Defaults to True.
*   **initial\_value\_threshold**: Floating point initial "best" value for the monitor, used with `save_best_only`.

* * *

[OrbaxCheckpoint](https://keras.io/api/callbacks/orbax_checkpoint/#orbaxcheckpoint)

[`OrbaxCheckpoint` class](https://keras.io/api/callbacks/orbax_checkpoint/#orbaxcheckpoint-class)