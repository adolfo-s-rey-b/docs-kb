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
 / LambdaCallback

LambdaCallback
==============

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/callbacks/lambda_callback.py#L5)

### `LambdaCallback` class

Copied!

`keras.callbacks.LambdaCallback(     on_epoch_begin=None,     on_epoch_end=None,     on_train_begin=None,     on_train_end=None,     on_train_batch_begin=None,     on_train_batch_end=None,     **kwargs )`

Callback for creating simple, custom callbacks on-the-fly.

This callback is constructed with anonymous functions that will be called at the appropriate time (during `Model.{fit | evaluate | predict}`). Note that the callbacks expects positional arguments, as:

*   `on_epoch_begin` and `on_epoch_end` expect two positional arguments: `epoch`, `logs`
*   `on_train_begin` and `on_train_end` expect one positional argument: `logs`
*   `on_train_batch_begin` and `on_train_batch_end` expect a positional argument `batch` and a keyword argument `logs`
*   See `Callback` class definition for the full list of functions and their expected arguments.

**Arguments**

*   **on\_epoch\_begin**: called at the beginning of every epoch.
*   **on\_epoch\_end**: called at the end of every epoch.
*   **on\_train\_begin**: called at the beginning of model training.
*   **on\_train\_end**: called at the end of model training.
*   **on\_train\_batch\_begin**: called at the beginning of every train batch.
*   **on\_train\_batch\_end**: called at the end of every train batch.
*   **kwargs**: Any function in `Callback` that you want to override by passing `function_name=function`. For example, `LambdaCallback(.., on_train_end=train_end_fn)`. The custom function needs to have same arguments as the ones defined in `Callback`.

**Example**

Copied!

`# Print the batch number at the beginning of every batch. batch_print_callback = LambdaCallback(     on_train_batch_begin=lambda batch,logs: print(batch))  # Stream the epoch loss to a file in JSON format. The file content # is not well-formed JSON but rather has a JSON object per line. import json json_log = open('loss_log.json', mode='wt', buffering=1) json_logging_callback = LambdaCallback(     on_epoch_end=lambda epoch, logs: json_log.write(         json.dumps({'epoch': epoch, 'loss': logs['loss']}) + '\n'),     on_train_end=lambda logs: json_log.close() )  # Terminate some processes after having finished model training. processes = ... cleanup_callback = LambdaCallback(     on_train_end=lambda logs: [         p.terminate() for p in processes if p.is_alive()])  model.fit(...,           callbacks=[batch_print_callback,                      json_logging_callback,                      cleanup_callback])`

* * *

[LambdaCallback](https://keras.io/api/callbacks/lambda_callback/#lambdacallback)

[`LambdaCallback` class](https://keras.io/api/callbacks/lambda_callback/#lambdacallback-class)