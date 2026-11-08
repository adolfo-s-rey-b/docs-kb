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
 / EarlyStopping

EarlyStopping
=============

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/callbacks.py#L2001)

### `EarlyStopping` class

Copied!

`tf_keras.callbacks.EarlyStopping(     monitor="val_loss",     min_delta=0,     patience=0,     verbose=0,     mode="auto",     baseline=None,     restore_best_weights=False,     start_from_epoch=0, )`

Stop training when a monitored metric has stopped improving.

Assuming the goal of a training is to minimize the loss. With this, the metric to be monitored would be `'loss'`, and mode would be `'min'`. A `model.fit()` training loop will check at end of every epoch whether the loss is no longer decreasing, considering the `min_delta` and `patience` if applicable. Once it's found no longer decreasing, `model.stop_training` is marked True and the training terminates.

The quantity to be monitored needs to be available in `logs` dict. To make it so, pass the loss or metrics at `model.compile()`.

**Arguments**

*   **monitor**: Quantity to be monitored.
*   **min\_delta**: Minimum change in the monitored quantity to qualify as an improvement, i.e. an absolute change of less than min\_delta, will count as no improvement.
*   **patience**: Number of epochs with no improvement after which training will be stopped.
*   **verbose**: Verbosity mode, 0 or 1. Mode 0 is silent, and mode 1 displays messages when the callback takes an action.
*   **mode**: One of `{"auto", "min", "max"}`. In `min` mode, training will stop when the quantity monitored has stopped decreasing; in `"max"` mode it will stop when the quantity monitored has stopped increasing; in `"auto"` mode, the direction is automatically inferred from the name of the monitored quantity.
*   **baseline**: Baseline value for the monitored quantity. Training will stop if the model doesn't show improvement over the baseline.
*   **restore\_best\_weights**: Whether to restore model weights from the epoch with the best value of the monitored quantity. If False, the model weights obtained at the last step of training are used. An epoch will be restored regardless of the performance relative to the `baseline`. If no epoch improves on `baseline`, training will run for `patience` epochs and restore weights from the best epoch in that set.
*   **start\_from\_epoch**: Number of epochs to wait before starting to monitor improvement. This allows for a warm-up period in which no improvement is expected and thus training will not be stopped.

**Example**

Copied!

`>>> callback = tf.keras.callbacks.EarlyStopping(monitor='loss', patience=3) >>> # This callback will stop the training when there is no improvement in >>> # the loss for three consecutive epochs. >>> model = tf.keras.models.Sequential([tf.keras.layers.Dense(10)]) >>> model.compile(tf.keras.optimizers.SGD(), loss='mse') >>> history = model.fit(np.arange(100).reshape(5, 20), np.zeros(5), ...                     epochs=10, batch_size=1, callbacks=[callback], ...                     verbose=0) >>> len(history.history['loss'])  # Only 4 epochs are run. 4`

* * *

[EarlyStopping](https://keras.io/2/api/callbacks/early_stopping/#earlystopping)

[`EarlyStopping` class](https://keras.io/2/api/callbacks/early_stopping/#earlystopping-class)