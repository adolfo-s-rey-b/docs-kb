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
 / TensorBoard

TensorBoard
===========

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/callbacks/tensorboard.py#L17)

### `TensorBoard` class

Copied!

`keras.callbacks.TensorBoard(     log_dir="logs",     histogram_freq=0,     write_graph=True,     write_images=False,     write_steps_per_second=False,     update_freq="epoch",     profile_batch=0,     embeddings_freq=0,     embeddings_metadata=None, )`

Enable visualizations for TensorBoard.

TensorBoard is a visualization tool provided with TensorFlow. A TensorFlow installation is required to use this callback.

This callback logs events for TensorBoard, including:

*   Metrics summary plots
*   Training graph visualization
*   Weight histograms
*   Sampled profiling

When used in `model.evaluate()` or regular validation in addition to epoch summaries, there will be a summary that records evaluation metrics vs `model.optimizer.iterations` written. The metric names will be prepended with `evaluation`, with `model.optimizer.iterations` being the step in the visualized TensorBoard.

If you have installed TensorFlow with pip, you should be able to launch TensorBoard from the command line:

Copied!

`tensorboard --logdir=path_to_your_logs`

You can find more information about TensorBoard [here](https://www.tensorflow.org/get_started/summaries_and_tensorboard)
.

**Arguments**

*   **log\_dir**: the path of the directory where to save the log files to be parsed by TensorBoard. e.g., `log_dir = os.path.join(working_dir, 'logs')`. This directory should not be reused by any other callbacks.
*   **histogram\_freq**: frequency (in epochs) at which to compute weight histograms for the layers of the model. If set to 0, histograms won't be computed. Validation data (or split) must be specified for histogram visualizations.
*   **write\_graph**: (Not supported at this time) Whether to visualize the graph in TensorBoard. Note that the log file can become quite large when `write_graph` is set to `True`.
*   **write\_images**: whether to write model weights to visualize as image in TensorBoard.
*   **write\_steps\_per\_second**: whether to log the training steps per second into TensorBoard. This supports both epoch and batch frequency logging.
*   **update\_freq**: `"batch"` or `"epoch"` or integer. When using `"epoch"`, writes the losses and metrics to TensorBoard after every epoch. If using an integer, let's say `1000`, all metrics and losses (including custom ones added by `Model.compile`) will be logged to TensorBoard every 1000 batches. `"batch"` is a synonym for 1, meaning that they will be written every batch. Note however that writing too frequently to TensorBoard can slow down your training, especially when used with distribution strategies as it will incur additional synchronization overhead. Batch-level summary writing is also available via `train_step` override. Please see [TensorBoard Scalars tutorial](https://www.tensorflow.org/tensorboard/scalars_and_keras#batch-level_logging)
     for more details.
*   **profile\_batch**: Profile the batch(es) to sample compute characteristics. profile\_batch must be a non-negative integer or a tuple of integers. A pair of positive integers signify a range of batches to profile. By default, profiling is disabled.
*   **embeddings\_freq**: frequency (in epochs) at which embedding layers will be visualized. If set to 0, embeddings won't be visualized.
*   **embeddings\_metadata**: Dictionary which maps embedding layer names to the filename of a file in which to save metadata for the embedding layer. In case the same metadata file is to be used for all embedding layers, a single filename can be passed.

**Examples**

Copied!

`tensorboard_callback = keras.callbacks.TensorBoard(log_dir="./logs") model.fit(x_train, y_train, epochs=2, callbacks=[tensorboard_callback]) # Then run the tensorboard command to view the visualizations.`

Custom batch-level summaries in a subclassed Model:

Copied!

``class MyModel(keras.Model):      def build(self, _):         self.dense = keras.layers.Dense(10)      def call(self, x):         outputs = self.dense(x)         tf.summary.histogram('outputs', outputs)         return outputs  model = MyModel() model.compile('sgd', 'mse')  # Make sure to set `update_freq=N` to log a batch-level summary every N # batches.  In addition to any [`tf.summary`](https://www.tensorflow.org/api_docs/python/tf/summary) contained in `model.call()`, # metrics added in `Model.compile` will be logged every N batches. tb_callback = keras.callbacks.TensorBoard('./logs', update_freq=1) model.fit(x_train, y_train, callbacks=[tb_callback])``

Custom batch-level summaries in a Functional API Model:

Copied!

``def my_summary(x):     tf.summary.histogram('x', x)     return x  inputs = keras.Input(10) x = keras.layers.Dense(10)(inputs) outputs = keras.layers.Lambda(my_summary)(x) model = keras.Model(inputs, outputs) model.compile('sgd', 'mse')  # Make sure to set `update_freq=N` to log a batch-level summary every N # batches. In addition to any [`tf.summary`](https://www.tensorflow.org/api_docs/python/tf/summary) contained in `Model.call`, # metrics added in `Model.compile` will be logged every N batches. tb_callback = keras.callbacks.TensorBoard('./logs', update_freq=1) model.fit(x_train, y_train, callbacks=[tb_callback])``

Profiling:

Copied!

`# Profile a single batch, e.g. the 5th batch. tensorboard_callback = keras.callbacks.TensorBoard(     log_dir='./logs', profile_batch=5) model.fit(x_train, y_train, epochs=2, callbacks=[tensorboard_callback])  # Profile a range of batches, e.g. from 10 to 20. tensorboard_callback = keras.callbacks.TensorBoard(     log_dir='./logs', profile_batch=(10,20)) model.fit(x_train, y_train, epochs=2, callbacks=[tensorboard_callback])`

* * *

[TensorBoard](https://keras.io/api/callbacks/tensorboard/#tensorboard)

[`TensorBoard` class](https://keras.io/api/callbacks/tensorboard/#tensorboard-class)