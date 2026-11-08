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
 / LambdaCallback

LambdaCallback
==============

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/callbacks.py#L3262)

### `LambdaCallback` class

Copied!

`tf_keras.callbacks.LambdaCallback(     on_epoch_begin=None,     on_epoch_end=None,     on_batch_begin=None,     on_batch_end=None,     on_train_begin=None,     on_train_end=None,     **kwargs )`

Callback for creating simple, custom callbacks on-the-fly.

This callback is constructed with anonymous functions that will be called at the appropriate time (during `Model.{fit | evaluate | predict}`). Note that the callbacks expects positional arguments, as:

*   `on_epoch_begin` and `on_epoch_end` expect two positional arguments: `epoch`, `logs`
*   `on_batch_begin` and `on_batch_end` expect two positional arguments: `batch`, `logs`
*   `on_train_begin` and `on_train_end` expect one positional argument: `logs`

**Arguments**

*   **on\_epoch\_begin**: called at the beginning of every epoch.
*   **on\_epoch\_end**: called at the end of every epoch.
*   **on\_batch\_begin**: called at the beginning of every batch.
*   **on\_batch\_end**: called at the end of every batch.
*   **on\_train\_begin**: called at the beginning of model training.
*   **on\_train\_end**: called at the end of model training.

**Example**

Copied!

`# Print the batch number at the beginning of every batch. batch_print_callback = LambdaCallback(     on_batch_begin=lambda batch,logs: print(batch))  # Stream the epoch loss to a file in JSON format. The file content # is not well-formed JSON but rather has a JSON object per line. import json json_log = open('loss_log.json', mode='wt', buffering=1) json_logging_callback = LambdaCallback(     on_epoch_end=lambda epoch, logs: json_log.write(         json.dumps({'epoch': epoch, 'loss': logs['loss']}) + '\n'),     on_train_end=lambda logs: json_log.close() )  # Terminate some processes after having finished model training. processes = ... cleanup_callback = LambdaCallback(     on_train_end=lambda logs: [         p.terminate() for p in processes if p.is_alive()])  model.fit(...,           callbacks=[batch_print_callback,                      json_logging_callback,                      cleanup_callback])`

* * *

[LambdaCallback](https://keras.io/2/api/callbacks/lambda_callback/#lambdacallback)

[`LambdaCallback` class](https://keras.io/2/api/callbacks/lambda_callback/#lambdacallback-class)