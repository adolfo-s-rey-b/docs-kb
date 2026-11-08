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
 / ReduceLROnPlateau

ReduceLROnPlateau
=================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/callbacks/reduce_lr_on_plateau.py#L11)

### `ReduceLROnPlateau` class

Copied!

`keras.callbacks.ReduceLROnPlateau(     monitor="val_loss",     factor=0.1,     patience=10,     verbose=0,     mode="auto",     min_delta=0.0001,     cooldown=0,     min_lr=0.0,     **kwargs )`

Reduce learning rate when a metric has stopped improving.

Models often benefit from reducing the learning rate by a factor of 2-10 once learning stagnates. This callback monitors a quantity and if no improvement is seen for a 'patience' number of epochs, the learning rate is reduced.

**Example**

Copied!

`reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.2,                               patience=5, min_lr=0.001) model.fit(x_train, y_train, callbacks=[reduce_lr])`

**Arguments**

*   **monitor**: String. Quantity to be monitored.
*   **factor**: Float. Factor by which the learning rate will be reduced. `new_lr = lr * factor`.
*   **patience**: Integer. Number of epochs with no improvement after which learning rate will be reduced.
*   **verbose**: Integer. 0: quiet, 1: update messages.
*   **mode**: String. One of `{'auto', 'min', 'max'}`. In `'min'` mode, the learning rate will be reduced when the quantity monitored has stopped decreasing; in `'max'` mode it will be reduced when the quantity monitored has stopped increasing; in `'auto'` mode, the direction is automatically inferred from the name of the monitored quantity.
*   **min\_delta**: Float. Threshold for measuring the new optimum, to only focus on significant changes.
*   **cooldown**: Integer. Number of epochs to wait before resuming normal operation after the learning rate has been reduced.
*   **min\_lr**: Float. Lower bound on the learning rate.

* * *

[ReduceLROnPlateau](https://keras.io/api/callbacks/reduce_lr_on_plateau/#reducelronplateau)

[`ReduceLROnPlateau` class](https://keras.io/api/callbacks/reduce_lr_on_plateau/#reducelronplateau-class)