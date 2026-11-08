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
 / Base Callback class

Base Callback class
===================

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/callbacks.py#L624)

### `Callback` class

Copied!

`tf_keras.callbacks.Callback()`

Abstract base class used to build new callbacks.

Callbacks can be passed to keras methods such as `fit`, `evaluate`, and `predict` in order to hook into the various stages of the model training and inference lifecycle.

To create a custom callback, subclass [`keras.callbacks.Callback`](https://keras.io/api/callbacks/base_callback#callback-class)
 and override the method associated with the stage of interest. See the [Custom callback](https://keras.io/guides/writing_your_own_callbacks)
 for more information.

**Example**

Copied!

`>>> training_finished = False >>> class MyCallback(tf.keras.callbacks.Callback): ...   def on_train_end(self, logs=None): ...     global training_finished ...     training_finished = True >>> model = tf.keras.Sequential([ ...     tf.keras.layers.Dense(1, input_shape=(1,))]) >>> model.compile(loss='mean_squared_error') >>> model.fit(tf.constant([[1.0]]), tf.constant([[1.0]]), ...           callbacks=[MyCallback()]) >>> assert training_finished == True`

If you want to use `Callback` objects in a custom training loop:

1.  You should pack all your callbacks into a single `callbacks.CallbackList` so they can all be called together.
2.  You will need to manually call all the `on_*` methods at the appropriate locations in your loop. Like this:

**Example**

Copied!

   `callbacks =  tf.keras.callbacks.CallbackList([...])    callbacks.append(...)    callbacks.on_train_begin(...)    for epoch in range(EPOCHS):      callbacks.on_epoch_begin(epoch)      for i, data in dataset.enumerate():        callbacks.on_train_batch_begin(i)        batch_logs = model.train_step(data)        callbacks.on_train_batch_end(i, batch_logs)      epoch_logs = ...      callbacks.on_epoch_end(epoch, epoch_logs)    final_logs=...    callbacks.on_train_end(final_logs)`

**Attributes**

*   **params**: Dict. Training parameters (eg. verbosity, batch size, number of epochs...).
*   **model**: Instance of `keras.models.Model`. Reference of the model being trained.

The `logs` dictionary that callback methods take as argument will contain keys for quantities relevant to the current batch or epoch (see method-specific docstrings).

* * *

[Base Callback class](https://keras.io/2/api/callbacks/base_callback/#base-callback-class)

[`Callback` class](https://keras.io/2/api/callbacks/base_callback/#callback-class)