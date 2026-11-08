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
 / LearningRateScheduler

LearningRateScheduler
=====================

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/callbacks.py#L2249)

### `LearningRateScheduler` class

Copied!

`tf_keras.callbacks.LearningRateScheduler(schedule, verbose=0)`

Learning rate scheduler.

At the beginning of every epoch, this callback gets the updated learning rate value from `schedule` function provided at `__init__`, with the current epoch and current learning rate, and applies the updated learning rate on the optimizer.

**Arguments**

*   **schedule**: a function that takes an epoch index (integer, indexed from 0) and current learning rate (float) as inputs and returns a new learning rate as output (float).
*   **verbose**: int. 0: quiet, 1: update messages.

**Example**

Copied!

`>>> # This function keeps the initial learning rate for the first ten epochs >>> # and decreases it exponentially after that. >>> def scheduler(epoch, lr): ...   if epoch < 10: ...     return lr ...   else: ...     return lr * tf.math.exp(-0.1) >>> >>> model = tf.keras.models.Sequential([tf.keras.layers.Dense(10)]) >>> model.compile(tf.keras.optimizers.SGD(), loss='mse') >>> round(model.optimizer.lr.numpy(), 5) 0.01`

Copied!

`>>> callback = tf.keras.callbacks.LearningRateScheduler(scheduler) >>> history = model.fit(np.arange(100).reshape(5, 20), np.zeros(5), ...                     epochs=15, callbacks=[callback], verbose=0) >>> round(model.optimizer.lr.numpy(), 5) 0.00607`

* * *

[LearningRateScheduler](https://keras.io/2/api/callbacks/learning_rate_scheduler/#learningratescheduler)

[`LearningRateScheduler` class](https://keras.io/2/api/callbacks/learning_rate_scheduler/#learningratescheduler-class)