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
 / ModelCheckpoint

ModelCheckpoint
===============

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/callbacks/model_checkpoint.py#L14)

### `ModelCheckpoint` class

Copied!

`keras.callbacks.ModelCheckpoint(     filepath,     monitor="val_loss",     verbose=0,     save_best_only=False,     save_weights_only=False,     mode="auto",     save_freq="epoch",     initial_value_threshold=None, )`

Callback to save the Keras model or model weights at some frequency.

`ModelCheckpoint` callback is used in conjunction with training using `model.fit()` to save a model or weights (in a checkpoint file) at some interval, so the model or weights can be loaded later to continue the training from the state saved.

A few options this callback provides include:

*   Whether to only keep the model that has achieved the "best performance" so far, or whether to save the model at the end of every epoch regardless of performance.
*   Definition of "best"; which quantity to monitor and whether it should be maximized or minimized.
*   The frequency it should save at. Currently, the callback supports saving at the end of every epoch, or after a fixed number of training batches.
*   Whether only weights are saved, or the whole model is saved.

**Example**

Copied!

`# Define a learning rate schedule initial_learning_rate = 0.1 lr_schedule = keras.optimizers.schedules.ExponentialDecay(     initial_learning_rate,     decay_steps=100000,     decay_rate=0.96,     staircase=True, )  model.compile(     optimizer=keras.optimizers.RMSprop(learning_rate=lr_schedule),     loss="sparse_categorical_crossentropy",     metrics=["accuracy"], )  checkpoint_filepath = '/tmp/ckpt/checkpoint.model.keras' model_checkpoint_callback = keras.callbacks.ModelCheckpoint(     filepath=checkpoint_filepath,     monitor='val_accuracy',     mode='max',     save_best_only=True)  # Model is saved at the end of every epoch, if it's the best seen so far. model.fit(     x_train, y_train, epochs=10, callbacks=[model_checkpoint_callback] )  # The model (that are considered the best) can be loaded as - keras.models.load_model(checkpoint_filepath)  # Alternatively, one could checkpoint just the model weights as - checkpoint_filepath = '/tmp/ckpt/checkpoint.weights.h5' model_checkpoint_callback = keras.callbacks.ModelCheckpoint(     filepath=checkpoint_filepath,     save_weights_only=True,     monitor='val_accuracy',     mode='max',     save_best_only=True)  # Model weights are saved at the end of every epoch, if it's the best seen # so far. model.fit(     x_train, y_train, epochs=10, callbacks=[model_checkpoint_callback] )  # The model weights (that are considered the best) can be loaded as - model.load_weights(checkpoint_filepath)`

Resuming training from weight-only checkpoints:

When using `save_weights_only=True`, the weights file includes the state of the optimizer (including iteration count and learning rate state) if the model is compiled at the time of saving.

To correctly resume training and restore the optimizer state (e.g., to continue a learning rate schedule without resetting it), you must **compile the model before loading the weights**.

Copied!

`# Define a learning rate schedule initial_learning_rate = 0.1 lr_schedule = keras.optimizers.schedules.ExponentialDecay(     initial_learning_rate,     decay_steps=100000,     decay_rate=0.96,     staircase=True, )  # 1. Create a fresh model instance model = get_model()  # 2. Compile the model *before* loading weights model.compile(     optimizer=keras.optimizers.RMSprop(learning_rate=lr_schedule),     loss="sparse_categorical_crossentropy",     metrics=["accuracy"], )  # 3. Load weights (optimizer state is restored automatically) model.load_weights(checkpoint_filepath)  # 4. Continue training model.fit(x_train, y_train, epochs=10)`

**Arguments**

*   **filepath**: string or `PathLike`, path to save the model file. `filepath` can contain named formatting options, which will be filled the value of `epoch` and keys in `logs` (passed in `on_epoch_end`). The `filepath` name needs to end with `".weights.h5"` when `save_weights_only=True` or should end with `".keras"` or `".h5"` when checkpoint saving the whole model (default). For example: if `filepath` is `"{epoch:02d}-{val_loss:.2f}.keras"` or "{epoch:02d}-{val\_loss:.2f}.weights.h5"\`, then the model checkpoints will be saved with the epoch number and the validation loss in the filename. The directory of the filepath should not be reused by any other callbacks to avoid conflicts.
*   **monitor**: The metric name to monitor. Typically the metrics are set by the `Model.compile` method. Note:
    *   Prefix the name with `"val_"` to monitor validation metrics.
    *   Use `"loss"` or `"val_loss"` to monitor the model's total loss.
    *   If you specify metrics as strings, like `"accuracy"`, pass the same string (with or without the `"val_"` prefix).
    *   If you pass `metrics.Metric` objects, `monitor` should be set to `metric.name`
    *   If you're not sure about the metric names you can check the contents of the `history.history` dictionary returned by `history = model.fit()`
    *   Multi-output models set additional prefixes on the metric names.
*   **verbose**: Verbosity mode, 0 or 1. Mode 0 is silent, and mode 1 displays messages when the callback takes an action.
*   **save\_best\_only**: if `save_best_only=True`, it only saves when the model is considered the "best" and the latest best model according to the quantity monitored will not be overwritten. If `filepath` doesn't contain formatting options like `{epoch}` then `filepath` will be overwritten by each new better model.
*   **mode**: one of {`"auto"`, `"min"`, `"max"`}. If `save_best_only=True`, the decision to overwrite the current save file is made based on either the maximization or the minimization of the monitored quantity. For `val_acc`, this should be `"max"`, for `val_loss` this should be `"min"`, etc. In `"auto"` mode, the direction is automatically inferred from the name of the monitored quantity.
*   **save\_weights\_only**: if `True`, then only the model's weights will be saved (`model.save_weights(filepath)`), else the full model is saved (`model.save(filepath)`).
*   **save\_freq**: `"epoch"` or integer. When using `"epoch"`, the callback saves the model after each epoch. When using integer, the callback saves the model at end of this many batches. If the `Model` is compiled with `steps_per_execution=N`, then the saving criteria will be checked every Nth batch. Note that if the saving isn't aligned to epochs, the monitored metric may potentially be less reliable (it could reflect as little as 1 batch, since the metrics get reset every epoch). Defaults to `"epoch"`.
*   **initial\_value\_threshold**: Floating point initial "best" value of the metric to be monitored. Only applies if `save_best_value=True`. Only overwrites the model weights already saved if the performance of current model is better than this value.

* * *

[ModelCheckpoint](https://keras.io/api/callbacks/model_checkpoint/#modelcheckpoint)

[`ModelCheckpoint` class](https://keras.io/api/callbacks/model_checkpoint/#modelcheckpoint-class)