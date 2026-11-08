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
 / RemoteMonitor

RemoteMonitor
=============

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/callbacks.py#L2178)

### `RemoteMonitor` class

Copied!

`tf_keras.callbacks.RemoteMonitor(     root="http://localhost:9000",     path="/publish/epoch/end/",     field="data",     headers=None,     send_as_json=False, )`

Callback used to stream events to a server.

Requires the `requests` library. Events are sent to `root + '/publish/epoch/end/'` by default. Calls are HTTP POST, with a `data` argument which is a JSON-encoded dictionary of event data. If `send_as_json=True`, the content type of the request will be `"application/json"`. Otherwise the serialized JSON will be sent within a form.

**Arguments**

*   **root**: String; root url of the target server.
*   **path**: String; path relative to `root` to which the events will be sent.
*   **field**: String; JSON field under which the data will be stored. The field is used only if the payload is sent within a form (i.e. send\_as\_json is set to False).
*   **headers**: Dictionary; optional custom HTTP headers.
*   **send\_as\_json**: Boolean; whether the request should be sent as `"application/json"`.

* * *

[RemoteMonitor](https://keras.io/2/api/callbacks/remote_monitor/#remotemonitor)

[`RemoteMonitor` class](https://keras.io/2/api/callbacks/remote_monitor/#remotemonitor-class)