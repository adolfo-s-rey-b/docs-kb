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
 / ProgbarLogger

ProgbarLogger
=============

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/callbacks.py#L1010)

### `ProgbarLogger` class

Copied!

`tf_keras.callbacks.ProgbarLogger(count_mode: str = "samples", stateful_metrics=None)`

Callback that prints metrics to stdout.

**Arguments**

*   **count\_mode**: One of `"steps"` or `"samples"`. Whether the progress bar should count samples seen or steps (batches) seen.
*   **stateful\_metrics**: Iterable of string names of metrics that should _not_ be averaged over an epoch. Metrics in this list will be logged as-is. All others will be averaged over time (e.g. loss, etc). If not provided, defaults to the `Model`'s metrics.

**Raises**

*   **ValueError**: In case of invalid `count_mode`.

* * *

[ProgbarLogger](https://keras.io/2/api/callbacks/progbar_logger/#progbarlogger)

[`ProgbarLogger` class](https://keras.io/2/api/callbacks/progbar_logger/#progbarlogger-class)