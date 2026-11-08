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
 / Base Callback class

Base Callback class
===================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/callbacks/callback.py#L6)

### `Callback` class

Copied!

`keras.callbacks.Callback()`

Base class used to build new callbacks.

Callbacks can be passed to keras methods such as `fit()`, `evaluate()`, and `predict()` in order to hook into the various stages of the model training, evaluation, and inference lifecycle.

To create a custom callback, subclass [`keras.callbacks.Callback`](https://keras.io/api/callbacks/base_callback#callback-class)
 and override the method associated with the stage of interest.

**Example**

Copied!

`>>> training_finished = False >>> class MyCallback(Callback): ...   def on_train_end(self, logs=None): ...     global training_finished ...     training_finished = True >>> model = Sequential([ ...     layers.Dense(1, input_shape=(1,))]) >>> model.compile(loss='mean_squared_error') >>> model.fit(np.array([[1.0]]), np.array([[1.0]]), ...           callbacks=[MyCallback()]) >>> assert training_finished == True`

If you want to use `Callback` objects in a custom training loop:

1.  You should pack all your callbacks into a single `callbacks.CallbackList` so they can all be called together.
2.  You will need to manually call all the `on_*` methods at the appropriate locations in your loop. Like this:

**Example**

Copied!

`callbacks =  keras.callbacks.CallbackList([...]) callbacks.append(...) callbacks.on_train_begin(...) for epoch in range(EPOCHS):     callbacks.on_epoch_begin(epoch)     for i, data in dataset.enumerate():     callbacks.on_train_batch_begin(i)     batch_logs = model.train_step(data)     callbacks.on_train_batch_end(i, batch_logs)     epoch_logs = ...     callbacks.on_epoch_end(epoch, epoch_logs) final_logs=... callbacks.on_train_end(final_logs)`

**Attributes**

*   **params**: Dict. Training parameters (eg. verbosity, batch size, number of epochs...).
*   **model**: Instance of `Model`. Reference of the model being trained.

The `logs` dictionary that callback methods take as argument will contain keys for quantities relevant to the current batch or epoch (see method-specific docstrings).

* * *

[Base Callback class](https://keras.io/api/callbacks/base_callback/#base-callback-class)

[`Callback` class](https://keras.io/api/callbacks/base_callback/#callback-class)