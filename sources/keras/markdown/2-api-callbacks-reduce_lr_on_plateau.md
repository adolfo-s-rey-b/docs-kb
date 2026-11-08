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
 / ReduceLROnPlateau

ReduceLROnPlateau
=================

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/callbacks.py#L3029)

### `ReduceLROnPlateau` class

Copied!

`tf_keras.callbacks.ReduceLROnPlateau(     monitor="val_loss",     factor=0.1,     patience=10,     verbose=0,     mode="auto",     min_delta=0.0001,     cooldown=0,     min_lr=0,     **kwargs )`

Reduce learning rate when a metric has stopped improving.

Models often benefit from reducing the learning rate by a factor of 2-10 once learning stagnates. This callback monitors a quantity and if no improvement is seen for a 'patience' number of epochs, the learning rate is reduced.

**Example**

Copied!

`reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.2,                               patience=5, min_lr=0.001) model.fit(X_train, Y_train, callbacks=[reduce_lr])`

**Arguments**

*   **monitor**: quantity to be monitored.
*   **factor**: factor by which the learning rate will be reduced. `new_lr = lr * factor`.
*   **patience**: number of epochs with no improvement after which learning rate will be reduced.
*   **verbose**: int. 0: quiet, 1: update messages.
*   **mode**: one of `{'auto', 'min', 'max'}`. In `'min'` mode, the learning rate will be reduced when the quantity monitored has stopped decreasing; in `'max'` mode it will be reduced when the quantity monitored has stopped increasing; in `'auto'` mode, the direction is automatically inferred from the name of the monitored quantity.
*   **min\_delta**: threshold for measuring the new optimum, to only focus on significant changes.
*   **cooldown**: number of epochs to wait before resuming normal operation after lr has been reduced.
*   **min\_lr**: lower bound on the learning rate.

* * *

[ReduceLROnPlateau](https://keras.io/2/api/callbacks/reduce_lr_on_plateau/#reducelronplateau)

[`ReduceLROnPlateau` class](https://keras.io/2/api/callbacks/reduce_lr_on_plateau/#reducelronplateau-class)