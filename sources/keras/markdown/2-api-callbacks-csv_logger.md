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
 / CSVLogger

CSVLogger
=========

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/callbacks.py#L3169)

### `CSVLogger` class

Copied!

`tf_keras.callbacks.CSVLogger(filename, separator=",", append=False)`

Callback that streams epoch results to a CSV file.

Supports all values that can be represented as a string, including 1D iterables such as `np.ndarray`.

**Example**

Copied!

`csv_logger = CSVLogger('training.log') model.fit(X_train, Y_train, callbacks=[csv_logger])`

**Arguments**

*   **filename**: Filename of the CSV file, e.g. `'run/log.csv'`.
*   **separator**: String used to separate elements in the CSV file. Separator string ("delimiter") must be a 1-character string.
*   **append**: Boolean. True: append if file exists (useful for continuing training). False: overwrite existing file.

* * *

[CSVLogger](https://keras.io/2/api/callbacks/csv_logger/#csvlogger)

[`CSVLogger` class](https://keras.io/2/api/callbacks/csv_logger/#csvlogger-class)